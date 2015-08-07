#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
  Simple web server for local application management, based on bottle framework
  Author: haitong.chen@gmail.com
"""
import sys
sys.path.append('..')

import time, urllib2, sqlite3, re, socket, os
#import ServerDb as sdb
import ServerDbLite as sdb
import SqlCmdHelper as sch
import time, urllib2, sqlite3
import SqlCmdHelper
from datetime import datetime
from subprocess import Popen
from multiprocessing import Process
from bottle import route, request, redirect, template,static_file, run
from ftplib import FTP

def retr_img_from_ftp(filename):
  usr, passwd = '111111', '111111'
  hosts = ['172.16.0.101', '172.16.0.108']
  with open(filename, 'wb') as lf:
    for host in hosts:
      try:
        ftp = FTP(host, timeout=5)
        ftp.login(usr, passwd)
      except Exception as e:
        print e
      else:
        try:
          ftp.retrbinary('RETR ' + filename, lf.write)
        except Exception as e:
          print e
          ftp.quit()
        else:
          ftp.quit()
          return True
    return False
      

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

@route('/')
def root():
  redirect('/index')

@route('/index')
def page_index():
  redirect('/query')

@route('/query')
def query():
  return template('./view/query.tpl', query_results=[])

@route('/query_drivers', method='POST')
def query_driver():
  driver_rec_hdr = (u'姓名', u'类别', u'身份证号', u'车辆', u'司机类型', u'港口', u'进出', u'照片', )
  name = request.forms.get('name')
  shipname = request.forms.get('shipname')
  status = request.forms.get('status')
  print name
  #dbconn = sdb.connect_orclex('haitong', '111111', sdb.DB_URL)
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  #cur.execute("SELECT * FROM driver_rec_table WHERE DN=:drvname", {'drvname':name})
  cur.execute("SELECT * FROM driver_rec_table WHERE name=?", (name,))
  #cur.execute("SELECT * FROM driver_rec_table")
  res = cur.fetchall()
  cur.close()
  dbconn.close()
  for drvrec in res:
    if not os.path.isfile(drvrec[-1]):
      retr_img_from_ftp(drvrec[-1])    
  return template('./view/query.tpl',
          query_results=[driver_rec_hdr]+res)

@route('/query_vehicles', method='POST')
def query_vehicle():
  veh_rec_hdr = (u'车牌号', u'公司全称', u'司机', u'证件类型', u'证件号码',
                 u'进出时间', u'港口', u'进出状态', u'司机照片', u'车辆照片')
  plate = request.forms.get('plate')
  dbconn = sdb.connect()
  dbconn.text_factory = str
  cur = dbconn.cursor()
  cur.execute('select * from vehicle_rec_table where plate=?', (plate,))
  res = cur.fetchall()
  cur.close()
  dbconn.close()
  for vhlrec in res:
    if not os.path.isfile(vhlrec[-1]):
      retr_img_from_ftp(vhlrec[-1])
    if not os.path.isfile(vhlrec[-2]):
      retr_img_from_ftp(vhlrec[-2])
  return template('./view/query.tpl',
          query_results=res)

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
          query_results=res)

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
          query_results=res)

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
          query_results=res)

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
          query_results=res)

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

@route('/static/<filename:path>')
def send_static(filename):
  return static_file(filename, root='./')

def test_ftp():
  retr_img_from_ftp('2015-08-06.csv')
  
def main():
  sdb.main()
  dbporc = Process(target=sdb.run_sock_svr, args=())
  dbporc.start()
  websvr = Process(target=run, args=(None, 'wsgiref', '0.0.0.0', '8081'))
  websvr.start()
  dbporc.join()
  websvr.join()
  #run(host='localhost', port=8081, Debug=True, reloader=False)
  #run(host='localhost', port=80, Debug=True)


if __name__ == '__main__':
  #main()
  test_ftp()
