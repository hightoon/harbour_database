#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
  Simple web server for local application management, based on bottle framework
  Author: haitong.chen@gmail.com
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('..')

import time, urllib2, sqlite3, re, socket, os, csv
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
    'session.cookie_expires': 1800,
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

def get_query_disp():
  if 'querydisp' in request.session:
    return request.session['querydisp']
  else:
    return 'hide'

def set_query_disp(val):
  request.session['querydisp'] = val

def get_setting_disp():
  if 'settingdisp' in request.session:
    return request.session['settingdisp']
  else:
    return 'hide'

def set_setting_disp(val):
  request.session['settingdisp'] = val

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
  sock1.settimeout(3.0)
  try:
      sock1.connect((HOST, PORT))
      sock1.sendall('sql:' + sql + "\n")
  except:
      print 'sock1 connect failed'
  finally:
      sock1.close()

  HOST, PORT = '172.16.0.108', 9998
  sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock2.settimeout(3.0)
  try:
      sock2.connect((HOST, PORT))
      sock2.sendall('sql:' + sql + "\n")
  except:
      print 'sock2 connect failed'
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

def cons_like_clause(like_kv):
  conds = ['%s like \'%%%s%%\''%(k, v) for k, v in like_kv.items()]
  cond_str = ' and '.join(conds)
  return cond_str

def cons_set_clause(kv):
  values = ['%s=\'%s\''%(k, v) for k, v in kv.items()]
  set_str = ','.join(values)
  return set_str

def cons_query_interval(start, end):
  print start, end
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
                  privs=privs, curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/query_vehicle_recs')
def query():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/query.tpl', query_results=[], query_tbl='vehicle_recs',
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/query_company')
def query():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/query.tpl', query_results=[], query_tbl='company',
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/query_drivers', method='POST')
def query_driver():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  driver_rec_hdr = (u'姓名', u'类别', u'身份证号', u'船舶', u'进出时间', u'港口', u'边检站', u'进出状态', u'报警状态', u'照片', )
  tab_query_cols = ('cat', 'station', 'harbour', 'direction', 'alarm')
  like_query_cols = ('name', 'vechicle')
  query_cond = {}
  isalarm = False
  for kw in tab_query_cols:
    input = request.forms.get(kw)
    if kw == 'alarm' and input == '船舶离港报警':
        isalarm = True
        input = ''
    if input:
        query_cond[kw] = input
  where_str = cons_query_where_clause(query_cond)
  like_cond = {}
  for kw in like_query_cols:
    input = request.forms.get(kw)
    if input: like_cond[kw] = input
  like_str = cons_like_clause(like_cond)
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
  final_cond = ' and '.join([subcond for subcond in (where_str, like_str, interval_str) if subcond])
  final_query_str = "SELECT * FROM driver_rec_table "

  if final_cond:
    final_query_str += " WHERE " + final_cond

  cur.execute(final_query_str + " ORDER by date DESC", query_cond)
  res = cur.fetchall()
  # get ships moving off
  cur.execute("SELECT ZWCBM, YWCBM FROM crs_shp_table WHERE STATUS like \'%%%s%%\'"%('离港',))
  off_ships = cur.fetchall()
  off_ship = [ship[0] or ship[1] for ship in off_ships]
  print off_ship
  dbconn.close()

  if isalarm:
    arecs = []
    checked = []
    for r in res:
      if r[0] in checked:
        continue
      else:
        checked.append(r[0])
      if r[3] in off_ships:
        if (r[1]=='临时登轮证' or r[1]=='长期登轮证') and ('出门' in r[7]):
          arecs.append(r)
        elif (r[1]=='船员登陆证' or r[1]=='台湾船员登陆证' or r[1]=='临时入境许可')\
              and ('进门' in r[7]):
          arecs.append(r)
        else:
          pass
    res = arecs

    print checked

  for drvrec in res:
    if not os.path.isfile(drvrec[-1]):
      if drvrec[-1].endswith('.jpg'):
        retr_img_from_ftp(drvrec[-1])

  # export results to csv file
  if request.forms.get('export'):
    csvname = datetime.strftime(datetime.now(), '%Y%m%dT%H%M%S') + '.csv'
    with open(csvname, 'wb') as csvfile:
      writer = csv.writer(csvfile, dialect='excel')
      writer.writerow(driver_rec_hdr)
      writer.writerows(res)
    return '<p>数据已导出，点击下载文件<a href="/static/%s">%s</a></p>'%(csvname, csvname)

  return template('./view/query.tpl',
          query_results=[driver_rec_hdr]+res, query_tbl='driver_recs',
          stations=list(set(sdb.get_stations_from_driver_recs())),
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user(),
          querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/query_vehicles', method='POST')
def query_vehicle():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  veh_rec_hdr = (u'车牌号', u'公司全称', u'司机', u'证件类型', u'证件号码',
                 u'进出时间', u'港口', u'进出状态', u'司机照片', u'车辆照片')
  tab_query_cols = ('direction')
  like_query_cols = ('plate', 'idnum', 'company')
  query_cond = {}
  for kw in tab_query_cols:
    input = request.forms.get(kw)
    if input: query_cond[kw] = input
  where_str = cons_query_where_clause(query_cond)
  like_cond = {}
  for kw in like_query_cols:
    input = request.forms.get(kw)
    if input: like_cond[kw] = input
  like_str = cons_like_clause(like_cond)
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
  final_cond = ' and '.join([subcond for subcond in (where_str, like_str, interval_str) if subcond])
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
  if request.forms.get('export'):
    csvname = datetime.strftime(datetime.now(), '%Y%m%dT%H%M%S') + '.csv'
    with open(csvname, 'wb') as csvfile:
      writer = csv.writer(csvfile, dialect='excel')
      writer.writerow(veh_rec_hdr)
      writer.writerows(res)
    return '<p>数据已导出，点击下载文件<a href="/static/%s">%s</a></p>'%(csvname, csvname)
  return template('./view/query.tpl',
          query_results=[veh_rec_hdr]+res, query_tbl='vehicle_recs',
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user(),
          querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
  cur.execute('SELECT rowid, * FROM company_table WHERE GSQC like \'%%%s%%\''%(fullname,))
  tab_hdr = [('序号', '公司代码', '公司全称', '公司简称', '类型代码', '所属国籍', '负责人', '业务范围',
            '使用标记', '操作员', '操作时间', '操作口岸', '备注')]
  res = tab_hdr + cur.fetchall()
  cur.close()
  dbconn.close()
  return template('./view/query.tpl',
          query_results=res, query_tbl='company',
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user(),
          querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/delcompany/<rowid>')
def delcomp(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  print rowid
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute('DELETE FROM company_table WHERE rowid=%s'%(rowid,))
  dbconn.commit()
  dbconn.close()
  redirect('/query_company')

@route('/query_vehicle_info')
def query_veh_info():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/query.tpl', query_results=[], query_tbl='vehicle',
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
  cur.execute("SELECT rowid, * FROM vehicleinfo WHERE WYCPH like \'%%%s%%\'"%(plate,))
  res = [('序号', '车牌号', '公司全称', '境外车牌号', '境内车牌号', '所属国籍', '车辆类型代码',
          '车辆高度', '肽位', '批文有效期', '通行口岸代码', '通行有效期', '申请表号', '现批文号码',
          '款式颜色', '车头字', '载重吨位', '内地承办单位', '录入检查员代码', '录入时间', '操作口岸代码',
          '备注', '主驾驶', '副驾驶')]
  res += cur.fetchall()
  #cur.execute("SELECT * FROM vehicleinfo")
  #res = cur.fetchall()
  cur.close()
  dbconn.close()
  return template('./view/query.tpl',
          query_results=res, query_tbl='vehicle',
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user(),
          querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/delvehicle/<rowid>')
def delvehicle(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  print rowid
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute('DELETE FROM vehicleinfo WHERE rowid=%s'%(rowid,))
  dbconn.commit()
  dbconn.close()
  send_sql('DELETE FROM vehicleinfo WHERE rowid=%s'%(rowid,))
  redirect('/query_vehicle_info')

@route('/query_driver_info')
def query_veh_info():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/query.tpl', query_results=[], query_tbl='driver',
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
  cur.execute("SELECT rowid, * FROM driverinfo_use WHERE XM like \'%%%s%%\'"%(name,))
  res = [('序号', '停留期', '前往国', '来自国', '许可证号', '身份证号', '第2姓名', '第2出生日期',
          '第二证件号码', '第二证件类别代码', '通行口岸代码', '民族代码', '通用标志', '操作人代码', '操作时间',
          '操作口岸', '备注', '签证号', '证件号码', '证件种类', '姓名', '性别', '出生日期',
          '国籍代码', '申请表号', '准驾签注有效期', '公司全称', '签证签注代码',
          '发证机关代码', '签证签注有效期', 'IC卡号')]
  res += cur.fetchall()
  cur.close()
  dbconn.close()
  return template('./view/query.tpl',
          query_results=res, query_tbl='driver',
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user(),
          querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/deldriver/<rowid>')
def deldriver(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  print rowid
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute('DELETE FROM driverinfo_use WHERE rowid=%s'%(rowid,))
  dbconn.commit()
  dbconn.close()
  send_sql('DELETE FROM driverinfo_use WHERE rowid=%s'%(rowid,))
  redirect('/query_driver_info')

@route('/query_ship')
def query_ship():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/query.tpl', query_results=[], query_tbl='ship',
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())


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
  cur.execute("SELECT rowid, * FROM crs_shp_table WHERE HC like \'%%%s%%\'"%(cruise,))
  res = [('序号', '航次', '船舶检索标识', 'MMSI号', '交通工具类型代码', '船舶种类代码', '船舶中文名称',
          '船舶英文名称', 'IMO号', '国际呼号', '国籍地区代码', '船员变更标识', '重点关注标识',
          '当前检查分类', '当前检查状态', '口岸代码', '操作员', '操作部门', '操作时间', '船籍港', '当前停靠地（码头）',
          '当前停靠地（泊位）', '解档修改状态', '加封人', '加封时间', '启封人', '启封时间', '武器弹药',
          '加封口岸', '启封口岸', '优检标志', '船舶状态')]
  res += cur.fetchall()
  cur.close()
  dbconn.close()
  return template('./view/query.tpl',
          query_results=res, query_tbl='ship',
          privs=UserDb.get_privilege(act_user.role),
          curr_user=get_act_user(),
          querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/delship/<rowid>')
def deldriver(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  print rowid
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute('DELETE FROM crs_shp_table WHERE rowid=%s'%(rowid,))
  dbconn.commit()
  dbconn.close()
  send_sql('DELETE FROM crs_shp_table WHERE rowid=%s'%(rowid,))
  redirect('/query_ship')

@route('/vehicles')
def add_vehicle():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/vehicle.tpl', privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
  redirect('/vehicles')

@route('/vehicle/<rowid>')
def update(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  print 'update vehicle @row ', rowid
  return template('./view/update_vehicle.tpl', privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(), rowid=rowid,
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/vehicle/<rowid>', method='POST')
def update(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  tab_cols = sch.sql_table_columns['vehicleinfo']
  user_input = {}
  cols = re.findall('([A-Z]+)', tab_cols)
  for col in cols:
    colname = col.lower()
    colval = request.forms.get(colname)
    if colval:
      user_input[col] = colval
  print  'update', rowid
  sql = 'UPDATE vehicleinfo SET ' + cons_set_clause(user_input) + ' WHERE rowid=%s'%(rowid,)
  print sql
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute(sql)
  dbconn.commit()
  dbconn.close()
  send_sql(sql)
  redirect('/query_vehicle')

@route('/drivers')
def add_driver():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/driver.tpl', privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
  redirect('/drivers')

@route('/driver/<rowid>')
def update(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/update_driver.tpl', privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(), rowid=rowid,
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/driver/<rowid>', method='POST')
def update(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  tab_cols = sch.sql_table_columns['driverinfo_use']
  user_input = {}
  cols = re.findall('([A-Z]+)', tab_cols)
  for col in cols:
    colname = col.lower()
    colval = request.forms.get(colname)
    if colval:
      user_input[col] = colval
  sql = 'UPDATE driverinfo_use SET ' + cons_set_clause(user_input) + ' WHERE rowid=%s'%(rowid,)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute(sql)
  dbconn.commit()
  dbconn.close()
  send_sql(sql)
  redirect('/query_driver_info')

@route('/companies')
def add_company():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/company.tpl',
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
  redirect('/companies')

@route('/company/<rowid>')
def update(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/update_company.tpl', privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(), rowid=rowid,
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/company/<rowid>', method='POST')
def update(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  tab_cols = sch.sql_table_columns['company_table']
  user_input = {}
  cols = re.findall('([A-Z]+)', tab_cols)
  for col in cols:
    colname = col.lower()
    colval = request.forms.get(colname)
    if colval:
      user_input[col] = colval
  sql = 'UPDATE company_table SET ' + cons_set_clause(user_input) + ' WHERE rowid=%s'%(rowid,)
  print sql
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute(sql)
  dbconn.commit()
  dbconn.close()
  send_sql(sql)
  redirect('/query_company')

@route('/ships')
def add_ship():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/ship.tpl', privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
  redirect('/ships')

@route('/ship/<rowid>')
def update(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/update_ship.tpl', privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(), rowid=rowid,
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/ship/<rowid>', method='POST')
def update(rowid):
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  tab_cols = sch.sql_table_columns['crs_shp_table']
  user_input = {}
  cols = re.findall('([A-Z]+)', tab_cols)
  for col in cols:
    colname = col.lower()
    colval = request.forms.get(colname)
    if colval:
      user_input[col] = colval
  sql = 'UPDATE crs_shp_table SET ' + cons_set_clause(user_input) + ' WHERE rowid=%s'%(rowid,)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute(sql)
  dbconn.commit()
  dbconn.close()
  send_sql(sql)
  redirect('/query_ship')

@route('/setting')
def setting():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting='setting',
                  roles=UserDb.get_roles(),
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

@route('/user_roles')
def role_mng():
  act_user = get_act_user()
  if act_user is None:
    redirect('/')
  act_user = UserDb.get(act_user)
  return template('./view/setting.tpl', setting='role_mng',
                  roles=UserDb.get_roles(),
                  privs=UserDb.get_privilege(act_user.role),
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
                  role2edit=rolename, curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
                    curr_user=get_act_user(),
                    querydisp=get_query_disp(), settingdisp=get_setting_disp())
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
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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
                  curr_user=get_act_user(),
                  querydisp=get_query_disp(), settingdisp=get_setting_disp())

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

@route('/tempstate/query_items/<state>')
def query_items_state(state):
  print state
  if get_query_disp() == 'show':
    set_query_disp('hide')
  else:
    set_query_disp('show')
  redirect('/query')

@route('/tempstate/setting_items/<state>')
def query_items_state(state):
  print state
  if get_setting_disp() == 'show':
    set_setting_disp('hide')
  else:
    set_setting_disp('show')
  redirect('/setting')

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
