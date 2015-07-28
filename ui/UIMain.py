#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
  Simple web server for local application management, based on bottle framework
  Author: haitong.chen@gmail.com
"""
import sys
sys.path.append('..')

import time, urllib2, sqlite3
#import ServerDb as sdb
from datetime import datetime
from subprocess import Popen
from bottle import route, request, redirect, template,static_file, run

driver_query_header = (
  u'姓名', u'类别', u'证件编号', u'所属船舶',
  u'进出时间', u'区域', u'进出状态', u'照片',
)

vehicle_query_header = (
  u'车牌号', u'公司', u'司机', u'证件类型',
  u'证件编号', u'进出时间', u'区域', u'进出状态',
)

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
  return template('./view/query.tpl',
          query_results=[driver_query_header, (u'陈海通', 'OK', '12344','343243aaa','待定','待定','未知','未知')])

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
  print wycph, gsqc, jwcph, jncph, ssgjdm
  #sdb.execute_sql('''INSERT vehicleinfo ()
  #''')

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
  run(host='0.0.0.0', port=80, Debug=True, reloader=False)
  #run(host='localhost', port=80, Debug=True)

if __name__ == '__main__':
  main()
