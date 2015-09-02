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
from bottle import route, request, redirect, template,static_file, run
from ftplib import FTP
import UserDb

act_user = None


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
    ret = True, user.is_admin
  else:
    ret = False, UserDb.User.NOT_ADMIN
  return ret

def init_db():
  UserDb.create_user_table()
  UserDb.create_role_table()
  UserDb.put_admin()

@route('/')
def root():
  if act_user is None:
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
  print username, password

  isvalid, isadmin = validate_from_db(username, password)
  print isvalid, isadmin
  if isvalid:
    act_user = UserDb.User(username, password, isadmin)
    redirect('/index')
  else:
    redirect('/')

@route('/logout')
def logout():
  global act_user
  act_user = None
  redirect('/')

@route('/index')
def page_index():
  redirect('/query')

@route('/query')
def query_home():
  if act_user is None:
    redirect('/')
  return template('./view/query.tpl', query_results=[], query_tbl='')

@route('/query_driver_recs')
def query():
  if act_user is None:
    redirect('/')
  return template('./view/query.tpl', query_results=[], query_tbl='driver_recs')

@route('/query_vehicle_recs')
def query():
  if act_user is None:
    redirect('/')
  return template('./view/query.tpl', query_results=[], query_tbl='vehicle_recs')

@route('/query_drivers', method='POST')
def query_driver():
  driver_rec_hdr = (u'姓名', u'类别', u'身份证号', u'车辆', u'进出时间', u'港口', u'进出状态', u'照片', )
  tab_query_cols = ('name', 'cat', 'vechicle', 'harbour', 'direction')
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
          query_results=[driver_rec_hdr]+res, query_tbl='driver_recs')

@route('/query_vehicles', method='POST')
def query_vehicle():
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
          query_results=[veh_rec_hdr]+res, query_tbl='vehicle_recs')

@route('/query_company', method='POST')
def query_company():
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
          query_results=res, query_tbl='company')

@route('/query_vehicle_info', method='POST')
def query_vhl_info():
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
          query_results=res, query_tbl='vehicle')

@route('/query_driver_info', method='POST')
def query_driver_info():
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
          query_results=res, query_tbl='driver')

@route('/query_ship', method='POST')
def query_ship():
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
          query_results=res, query_tbl='ship')

@route('/vehicles')
def add_vehicle():
  return template('./view/vehicle.tpl')

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
  return template('./view/driver.tpl')

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
  return template('./view/company.tpl')

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
  return template('./view/ship.tpl')

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
  if act_user is None:
    redirect('/')
  return template('./view/setting.tpl', setting='role_mng',
                  roles=UserDb.get_roles())

@route('/add_role', method='POST')
def add_role():
  if act_user is None:
    redirect('/')
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
  if act_user is None:
    redirect('/')
  UserDb.del_role(rolename)
  return rolename, '已删除'

@route('/access_control')
def access_control():
  if act_user is None:
    redirect('/')
  return template('./view/setting.tpl', setting='access_granting',
                  roles=UserDb.get_roles())

@route('/access_grant', method='POST')
def grant():
  if act_user is None:
    redirect('/')
  webacc = request.forms.get('web')
  if webacc: print 'web access'
  sysacc = request.forms.get('sys')
  if sysacc: print 'sys access'
  query = request.forms.get('query')
  if query: print 'query'
  grnt = request.forms.get('grant')
  print grnt

@route('/account_mngn')
def account_mngn():
  if act_user is None:
    redirect('/')
  users = UserDb.fetch_users()
  return template('./view/setting.tpl', setting='accounts',
                  users=users)

@route('/del_user/<usrname>', method='POST')
def del_user(usrname):
  if act_user is None:
    redirect('/')
  UserDb.del_user(usrname)
  redirect('/account_mngn')

@route('/account_query', method="POST")
def account_query():
  if act_user is None: redirect('/')
  user = request.forms.get('account')
  if request.forms.get('query'):
    return template('./view/setting.tpl', setting="accounts", users=[UserDb.get(user)])
  elif request.forms.get('create'):
    redirect('/user_update')

@route('/user_update')
def update_user():
  if act_user is None: redirect('/')
  return template('./view/setting.tpl', setting="adduser")

@route('/update_user', method='POST')
def update_user():
  if act_user is None: redirect('/')
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
  if act_user is None: redirect('/')
  UserDb.del_user(usrname)
  redirect('/account_mngn')

@route('/change_passwd')
def change_passwd():
  if act_user is None: redirect('/')
  return template('./view/setting.tpl', setting="change_password")

@route('/change_passwd', method='POST')
def update_passwd():
  if act_user is None: redirect('/')
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
  websvr = Process(target=run, args=(None, 'wsgiref', '0.0.0.0', '8081'))
  websvr.start()
  dbporc.join()
  websvr.join()
  #run(host='localhost', port=8081, Debug=True, reloader=False)
  #run(host='localhost', port=80, Debug=True)


if __name__ == '__main__':
  main()
  #test_ftp()
