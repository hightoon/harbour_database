#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
  Simple web server for local application management, based on bottle framework
  Author: haitong.chen@gmail.com
"""
import sys
sys.path.append('..')

import time, urllib2, sqlite3, re
import ServerDb as sdb
import SqlCmdHelper as sch
from datetime import datetime
from subprocess import Popen
from multiprocessing import Process
from bottle import route, request, redirect, template,static_file, run

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
  name = request.forms.get('name').decode('utf-8')
  shipname = request.forms.get('shipname')
  status = request.forms.get('status')
  print name
  dbconn = sdb.connect_orclex('haitong', '111111', sdb.DB_URL)
  cur = dbconn.cursor()
  cur.execute('SELECT * FROM driver_rec_table WHERE DB=%s'%(name,))
  res = cur.fetchall()
  return template('./view/query.tpl',
          query_results=[driver_query_header]+res)

@route('/query_vehicles', method='POST')
def query_vehicle():
  return template('./view/query.tpl',
          query_results=[vehicle_query_header])

@route('/vehicles')
def add_vehicle():
  return template('./view/vehicle.tpl')

@route('/add_vehicle', method='POST')
def add_vehicle():
  wycph = request.forms.get('wycph')
  gsqc = request.forms.get('gsqc')
  jwcph = request.forms.get('jwcph')
  jncph = request.forms.get('jncph')
  ssgjdm = request.forms.get('ssgjdm')
  cllxdm = request.forms.get('cllxdm')
  clgd = request.forms.get('clgd')
  tw = request.forms.get('tw')
  pwyxq = request.forms.get('pwyxq')
  txkadm = request.forms.get('txkadm')
  txyxq = request.forms.get('txyxq')
  sqbh = request.forms.get('sqbh')
  pwh = request.forms.get('pwh')
  ksys = request.forms.get('ksys')
  ctz = request.forms.get('ctz')
  zzdw = request.forms.get('zzdw')
  cbdw = request.forms.get('cbdw')
  czy = request.forms.get('czy')
  czsj = request.forms.get('czsj')
  czkadm = request.forms.get('czkadm')
  bz = request.forms.get('bz')
  pd = request.forms.get('pd')
  sd = request.forms.get('sd')
  
  tab_cols = sch.sql_table_columns['vehicleinfo']
  print tab_cols
  user_input = []
  cols = re.findall('([A-Z]+)', tab_cols)
  print cols
  for col in cols:
    colname = col.lower()
    print colname
    user_input.append(request.forms.get(colname))
  print user_input
  sdb.execute_sql('INSERT vehicleinfo %s VALUES %s'%(tab_cols, str(tuple(user_input))))
  print 'insert done'

@route('/drivers')
def add_driver():
  return template('./view/driver.tpl')

@route('/add_driver', method='POST')
def add_driver():
  print 'add driver'

@route('/companies')
def add_company():
  return template('./view/company.tpl')

@route('/add_company', method='POST')
def add_company():
  print 'add company'

@route('/static/<filename:path>')
def send_static(filename):
  return static_file(filename, root='./')

def main():
  dbporc = Process(target=sdb.main, args=())
  dbporc.start()
  websvr = Process(target=run, args=(None, 'wsgiref', '10.140.163.132', '8081'))
  websvr.start()
  dbporc.join()
  websvr.join()
  #run(host='localhost', port=8081, Debug=True, reloader=False)
  #run(host='localhost', port=80, Debug=True)
  

if __name__ == '__main__':
  main()
