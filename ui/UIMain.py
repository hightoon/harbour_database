#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
  Simple web server for local application management, based on bottle framework
  Author: haitong.chen@gmail.com
"""
import sys
sys.path.append('..')

import time, urllib2, sqlite3, re, socket, os
import ServerDbLite as sdb
import SqlCmdHelper as sch
import time, urllib2, sqlite3
import SqlCmdHelper
from datetime import datetime
from subprocess import Popen
from multiprocessing import Process
from bottle import route, request, redirect, template,static_file, run, app, hook
from ftplib import FTP
from beaker.middleware import SessionMiddleware
import UserDb


session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

def set_act_user(usrname):
  request.session['logged_in'] = usrname

def get_act_user():
  if 'logged_in' in request.session:
    return request.session['logged_in']
  else:
    return None

def retr_img_from_ftp(filename):
  usr, passwd = '111111', '111111'
  hosts = ['172.16.0.101', '172.16.0.108']
  ret = True
  print '从卡口电脑获取照片...'
  with open(filename, 'wb') as lf:
    for host in hosts:
      try:
        ftp = FTP(host, timeout=0.5)
        ftp.login(usr, passwd)
      except Exception as e:
        print e
        ret = False
      else:
        try:
          ftp.retrbinary('RETR ' + filename, lf.write)
        except Exception as e:
          print e
          ret = False
        finally:
          ftp.quit()
    if not ret:
      os.remove(filename)
    return ret

def get_hosts():
  fd = open('hosts.txt')
  hosts = fd.read().split(',')
  fd.close()
  return hosts

def send_sql(sql):
  HOST, PORT = '172.16.0.101', 9998
  sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
      sock1.connect((HOST, PORT))
      sock1.sendall('sql:' + sql + "\n")
  finally:
      sock1.close()

  HOST, PORT = '172.16.0.108', 9998
  sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
      sock2.connect((HOST, PORT))
      sock2.sendall('sql:' + sql + "\n")
  finally:
      sock2.close()

def convert_table_value(s):
  if s == '':
    return '\'\''
  else:
    return '\'%s\''%s

def cons_query_where_clause(query_mapping):
  conds = ['=:'.join([col, col]) for col in query_mapping.keys()]
  cond_str = ' and '.join(conds)
  return cond_str

def cons_query_interval(start, end):
  timefmt = '%Y-%m-%d'
  try:
    [datetime.strptime(t, timefmt) for t in (start, end)]
  except ValueError:
    return None
  else:
    return start + ' 00:00:00', end + ' 23:59:59'

def validate_from_db(usr, passwd):
  user = UserDb.get(usr)
  if user is not None and user.usrname == usr and user.password == passwd:
    ret = True, user
  else:
    ret = False, user
  return ret

def init_db():
  UserDb.create_user_table()
  UserDb.create_role_table()
  UserDb.add_root()
  UserDb.put_admin()

@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']

@route('/')
def root():
  if get_act_user() is None:
    redirect('/login')
  else:
    redirect('/index')

@route('/login')
def login():
  return template('./view/login.tpl')

@route('/login', method='POST')
def do_login():
  global act_user
  print request.get('REMOTE_ADDR'), ' connected'
  forgot = None
  username = request.forms.get('username')
  password = request.forms.get('password')

  isvalid, user = validate_from_db(username, password)
  if isvalid:
    #act_user = user
    set_act_user(username)
    redirect('/index')
  else:
    redirect('/')

@route('/logout')
def logout():
  request.session.delete()
  redirect('/')

@route('/index')
def page_index():
  redirect('/query')

@route('/query')
def query_home():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  privs = UserDb.get_privilege(UserDb.get(act_user).role)
  return template('./view/query.tpl', query_results=[], query_tbl='',
                  privs=privs, curr_user=get_act_user())

@route('/query_driver_recs')
def query():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  stations = sdb.get_stations_from_driver_recs()
  stations = list(set(stations))
  return template('./view/query.tpl', query_results=[], query_tbl='driver_recs',
                  stations=stations, privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/query_vehicle_recs')
def query():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/query.tpl', query_results=[], query_tbl='vehicle_recs',
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/query_drivers', method='POST')
def query_driver():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  driver_rec_hdr = (u'姓名', u'类别', u'身份证号', u'车辆', u'进出时间', u'边检站', u'港口', u'进出状态', u'报警状态', u'照片', )
  tab_query_cols = ('name', 'cat', 'vechicle', 'station', 'harbour', 'direction', 'alarm')
  query_cond = {}
  for kw in tab_query_cols:
    input = request.forms.get(kw)
    if input: query_cond[kw] = input
  where_str = cons_query_where_clause(query_cond)
  # add query interval
  interval = cons_query_interval(request.forms.get('start'), request.forms.get('end'))
  if interval:
    start, end = interval
    query_cond['start'] = start
    query_cond['end'] = end
    interval_str = ' datetime(date) BETWEEN datetime(:start) and datetime(:end)'
  else:
    interval_str = ''
  #dbconn = sdb.connect_orclex('haitong', '111111', sdb.DB_URL)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  final_cond = ' and '.join([subcond for subcond in (where_str, interval_str) if subcond])
  final_query_str = "SELECT * FROM driver_rec_table"
  if final_cond:
    final_query_str += " WHERE " + final_cond
  cur.execute(final_query_str, query_cond)
  res = cur.fetchall()
  cur.close()
  dbconn.close()
  for drvrec in res:
    if not os.path.isfile(drvrec[-1]):
      if drvrec[-1].endswith('.jpg'):
        retr_img_from_ftp(drvrec[-1])
  return template('./view/query.tpl',
          query_results=[driver_rec_hdr]+res, query_tbl='driver_recs',
          stations=list(set(sdb.get_stations_from_driver_recs())),
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user())

@route('/query_vehicles', method='POST')
def query_vehicle():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  veh_rec_hdr = (u'车牌号', u'公司全称', u'司机', u'证件类型', u'证件号码',
                 u'进出时间', u'港口', u'进出状态', u'司机照片', u'车辆照片')
  tab_query_cols = ('plate', 'idnum', 'direction')
  query_cond = {}
  for kw in tab_query_cols:
    input = request.forms.get(kw)
    if input: query_cond[kw] = input
  where_str = cons_query_where_clause(query_cond)
  # add query interval
  interval = cons_query_interval(request.forms.get('start'), request.forms.get('end'))
  if interval:
    print interval
    start, end = interval
    query_cond['start'] = start
    query_cond['end'] = end
    interval_str = ' datetime(date) BETWEEN datetime(:start) and datetime(:end)'
  else:
    interval_str = ''
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  final_cond = ' and '.join([subcond for subcond in (where_str, interval_str) if subcond])
  final_query_str = "SELECT * FROM vehicle_rec_table"
  if final_cond:
    final_query_str += " WHERE " + final_cond
  cur.execute(final_query_str, query_cond)
  res = cur.fetchall()
  cur.close()
  dbconn.close()
  for vhlrec in res:
    if not os.path.isfile(vhlrec[-1]):
      if vhlrec[-1].endswith('.jpg'):
        retr_img_from_ftp(vhlrec[-1])
    if not os.path.isfile(vhlrec[-2]):
      if vhlrec[-2].endswith('.jpg'):
        retr_img_from_ftp(vhlrec[-2])
  return template('./view/query.tpl',
          query_results=[veh_rec_hdr]+res, query_tbl='vehicle_recs',
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user())

@route('/query_company', method='POST')
def query_company():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  fullname = request.forms.get('fullname')
  print fullname
  #dbconn = sdb.connect_orclex('haitong', '111111', sdb.DB_URL)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  #cur.execute("SELECT * FROM company_table WHERE GSQC=:name", {'name':fullname})
  #cur.execute("SELECT * FROM company_table")
  cur.execute('SELECT * FROM company_table WHERE GSQC=?', (fullname,))
  res = cur.fetchall()
  print res
  cur.close()
  dbconn.close()
  return template('./view/query.tpl',
          query_results=res, query_tbl='company',
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user())

@route('/query_vehicle_info', method='POST')
def query_vhl_info():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  plate = request.forms.get('plate')
  print plate
  #dbconn = sdb.connect_orclex('haitong', '111111', sdb.DB_URL)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute("SELECT * FROM vehicleinfo WHERE WYCPH=?", (plate,))
  res = cur.fetchall()
  print res
  #cur.execute("SELECT * FROM vehicleinfo")
  #res = cur.fetchall()
  #print res
  cur.close()
  dbconn.close()
  return template('./view/query.tpl',
          query_results=res, query_tbl='vehicle',
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user())

@route('/query_driver_info', method='POST')
def query_driver_info():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  name = request.forms.get('name')
  #dbconn = sdb.connect_orclex('haitong', '111111', sdb.DB_URL)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute("SELECT * FROM driverinfo_use WHERE XM=?", (name,))
  #cur.execute("SELECT * FROM driverinfo")
  res = cur.fetchall()
  print res
  cur.close()
  dbconn.close()
  return template('./view/query.tpl',
          query_results=res, query_tbl='driver',
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user())

@route('/query_ship', method='POST')
def query_ship():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  cruise = request.forms.get('cruise')
  #dbconn = sdb.connect_orclex('haitong', '111111', sdb.DB_URL)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute("SELECT * FROM crs_shp_table WHERE HC=?", (cruise,))
  res = cur.fetchall()
  print res
  cur.close()
  dbconn.close()
  return template('./view/query.tpl',
          query_results=res, query_tbl='ship',
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user())

@route('/vehicles')
def add_vehicle():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/vehicle.tpl', privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/add_vehicle', method='POST')
def add_vehicle():
  tab_cols = sch.sql_table_columns['vehicleinfo']
  user_input = []
  cols = re.findall('([A-Z]+)', tab_cols)
  for col in cols:
    colname = col.lower()
    user_input.append(request.forms.get(colname))
  print user_input
  #sql = 'INSERT INTO vehicleinfo %s VALUES %s'%(tab_cols, str(tuple(user_input)))
  #dbconn = sdb.connect_orclex('haitong', '111111', sdb.DB_URL)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  sql = 'insert into vehicleinfo values (%s)'%(('?,'*len(cols))[:-1],)
  print sql
  cur.execute(sql, tuple(user_input))
  dbconn.commit()
  cur.close()
  dbconn.close()
  #sql = 'insert into vehicleinfo values %s'%(str(tuple(user_input)),)
  user_input = [convert_table_value(item) for item in user_input]
  sql = 'insert into vehicleinfo(%s) values (%s)'%(','.join(cols), ','.join(user_input),)
  print sql
  send_sql(sql)

@route('/drivers')
def add_driver():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/driver.tpl', privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/add_driver', method='POST')
def add_driver():
  tab_cols = sch.sql_table_columns['driverinfo_use']
  user_input = []
  cols = re.findall('([A-Z1-9]+)', tab_cols)
  print cols
  for col in cols:
    colname = col.lower()
    user_input.append(request.forms.get(colname))
  print user_input
  #sql = 'INSERT INTO driverinfo_use %s VALUES %s'%(tab_cols, str(tuple(user_input)))
  #dbconn = sdb.connect_orclex('haitong', '111111', sdb.DB_URL)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute('insert into driverinfo_use values (%s)'%(('?,'*len(cols))[:-1]), tuple(user_input))
  dbconn.commit()
  cur.close()
  dbconn.close()
  print 'insert driver done'
  user_input = [convert_table_value(item) for item in user_input]
  sql = 'insert into driverinfo_use values (%s)'%(','.join(user_input),)
  send_sql(sql)

@route('/companies')
def add_company():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/company.tpl',
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/add_company', method='POST')
def add_company():
  tab_cols = sch.sql_table_columns['company_table']
  user_input = []
  cols = re.findall('([A-Z]+)', tab_cols)
  print cols
  for col in cols:
    colname = col.lower()
    user_input.append(request.forms.get(colname))
  print user_input
  #sql = 'INSERT INTO company_table %s VALUES %s'%(tab_cols, str(tuple(user_input)))
  #dbconn = sdb.connect_orclex('haitong', '111111', sdb.DB_URL)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute('insert into company_table values (%s)'%(('?,'*len(cols))[:-1]), tuple(user_input))
  dbconn.commit()
  cur.close()
  dbconn.close()
  print 'insert company done'
  user_input = [convert_table_value(item) for item in user_input]
  sql = 'insert into company_table values (%s)'%(','.join(user_input),)
  send_sql(sql)

@route('/ships')
def add_ship():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/ship.tpl', privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/add_ship', method='POST')
def add_ship():
  tab_cols = sch.sql_table_columns['crs_shp_table']
  user_input = []
  cols = re.findall('([A-Z1-9]+)', tab_cols)
  print cols
  for col in cols:
    colname = col.lower()
    user_input.append(request.forms.get(colname))
  print user_input
  #sql = 'INSERT INTO crs_shp_table %s VALUES %s'%(tab_cols, str(tuple(user_input)))
  #dbconn = sdb.connect_orclex('haitong', '111111', sdb.DB_URL)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute('insert into crs_shp_table values (%s)'%(('?,'*len(cols))[:-1]), tuple(user_input))
  dbconn.commit()
  cur.close()
  dbconn.close()
  print 'insert ship done'
  user_input = [convert_table_value(item) for item in user_input]
  sql = 'insert into crs_shp_table values (%s)'%(','.join(user_input),)
  send_sql(sql)

@route('/user_roles')
def role_mng():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting='role_mng',
                  roles=UserDb.get_roles(),
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/add_role', method='POST')
def add_role():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  rolename = request.forms.get('rn')
  op = request.forms.get('create')
  if op and rolename:
    r = UserDb.Role(rolename=rolename)
    #UserDb.add_role(r)
    r.put()
    redirect('/user_roles')
  else:
    op = request.forms.get('query')
    if op:
      redirect('/user_roles')

@route('/del_role/<rolename>')
def del_role(rolename):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  UserDb.del_role(rolename)
  return rolename, '已删除'

@route('/edit_role/<rolename>')
def edit_role(rolename):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting='edit_role',
                  roles=UserDb.get_roles(), privs=UserDb.get_privilege(act_user.role),
                  role2edit=rolename, curr_user=get_act_user())

@route('/edit_role/<rolename>', method='POST')
def edit_role(rolename):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  desc = request.forms.get('desc')
  status = request.forms.get('status')
  print desc, status, rolename
  UserDb.update_role_status_desc(rolename, status, desc)
  redirect('/user_roles')

@route('/access_control')
def access_control():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting='access_granting',
                  roles=UserDb.get_roles(),
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/access_grant', method='POST')
def grant():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  privs = ['sys', 'query', 'vehicle', 'driver', 'company', 'ship']
  granted = []
  for priv in privs:
    if request.forms.get(priv):
      granted.append(priv)
  role = request.forms.get('grant')
  print role
  UserDb.update_privilege(role, granted)

@route('/account_mngn')
def account_mngn():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  users = UserDb.fetch_users()
  return template('./view/setting.tpl', setting='accounts',
                  users=users,
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),)

@route('/del_user/<usrname>', method='POST')
def del_user(usrname):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  UserDb.del_user(usrname)
  redirect('/account_mngn')

@route('/edit_user/<usrname>')
def edit_user(usrname):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting='edit_user',
                  privs=UserDb.get_privilege(act_user.role),
                  usrname=usrname, roles=UserDb.get_roles(),
                  curr_user=get_act_user())

@route('/edit_user/<usrname>', method='POST')
def edit_user(usrname):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  nickname = request.forms.get('nickname')
  desc = request.forms.get('desc')
  role = request.forms.get('role')
  print usrname, nickname, desc, role
  UserDb.change_user_info(usrname, desc, role, nickname)
  redirect('/account_mngn')

@route('/account_query', method="POST")
def account_query():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  user = request.forms.get('account')
  if request.forms.get('query'):
    return template('./view/setting.tpl', setting="accounts",
                    users=[UserDb.get(user)],
                    privs=UserDb.get_privilege(act_user.role),
                    curr_user=get_act_user())
  elif request.forms.get('create'):
    redirect('/user_update')

@route('/user_update')
def update_user():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting="adduser",
                  roles=UserDb.get_roles(),
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/update_user', method='POST')
def update_user():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  usrname = request.forms.get('usrname')
  passwd  = request.forms.get('passwd')
  role    = request.forms.get('role')
  desc    = request.forms.get('desc')
  nickname= request.forms.get('nickname')
  status  = request.forms.get('status')
  newuser = UserDb.User(usrname, passwd, role=='系统管理员', nickname, desc, status=status, role=role)
  newuser.put()
  redirect('/account_mngn')

@route('/del_user/<usrname>')
def del_user(usrname):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  UserDb.del_user(usrname)
  redirect('/account_mngn')

@route('/change_passwd')
def change_passwd():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting="change_password",
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user())

@route('/change_passwd', method='POST')
def update_passwd():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  passwd = request.forms.get('newpass')
  cnfm_passwd = request.forms.get('confirmedpass')
  if passwd != cnfm_passwd:
    return '新密码两次输入不一致，请返回重试!'
  UserDb.change_passwd(act_user.usrname, passwd)
  redirect('/account_mngn')

@route('/static/<filename:path>')
def send_static(filename):
  return static_file(filename, root='./')

def test_ftp():
  retr_img_from_ftp('2015-08-06.csv')


def main():
  sdb.main()
  init_db()
  dbporc = Process(target=sdb.run_sock_svr, args=())
  dbporc.start()
  websvr = Process(target=run, args=(app, 'wsgiref', '0.0.0.0', '8081'))
  websvr.start()
  dbporc.join()
  websvr.join()
  #run(host='localhost', port=8081, Debug=True, reloader=False)
  #run(host='localhost', port=80, Debug=True)


if __name__ == '__main__':
  main()
  #test_ftp()
