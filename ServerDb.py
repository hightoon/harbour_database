#-*- coding: utf-8 -*-
'''
  file: ServerDb.py
  description: handle DB operation on server side
'''

import cx_Oracle, socket, SocketServer
from SqlCmdHelper import sql_cmds

dbconn = None
DB_URL = socket.gethostbyname(socket.gethostname()) + '/XE'

class SvrSockSvr(SocketServer.BaseRequestHandler):
  def handle(self):
    # self.request is the TCP socket connected to the client
    self.data = self.request.recv(1024).strip()
    print "{} wrote:".format(self.client_address[0])
    print self.data

def connect_orclex(usr, passwd, url):
  return cx_Oracle.connect(usr, passwd, url)

def create_table_from_script(file):
  if dbconn is None:
    return None
  try:
    fd = open(file)
  except:
    return None
  else:
    sql = fd.read()
    cur = dbconn.cursor()
    cur.execute(sql)
    cur.commit()
    cur.close()

def execute_sql(sql):
  if dbconn is not None:
    cur = dbconn.cursor()
    try:
      cur.execute(sql)
      dbconn.commit()
    except cx_Oracle.DatabaseError as e:
      print e
    cur.close()

def create_vehicle_info_table():
  execute_sql(sql_cmds['create_vehicle_info_table'])

def drop_vehicle_info_table():
  execute_sql('drop table vehicleinfo')

def create_driver_info_table():
  execute_sql(sql_cmds['create_driver_info_table'])

def drop_driver_info_table():
  execute_sql('drop table driverinfo')

def create_veh_drvr_rel_table():
  execute_sql(sql_cmds['create_veh_drvr_rel_table'])

def drop_vdr_table():
  execute_sql('drop table vhl_drvr_relat')

def create_cruise_ship_table():
  execute_sql(sql_cmds['create_cruise_ship_table'])

def drop_crs_shp_table():
  execute_sql('drop table crs_shp_table')

def create_company_table():
  execute_sql(sql_cmds['create_company_table'])

def drop_company_table():
  execute_sql('drop table company_table')

def create_shp_lcc_info_table():
  execute_sql(sql_cmds['create_shp_lcc_info_table'])

def drop_shp_lcc_info_table():
  execute_sql('drop table shp_lcc_info_table')

def create_crew_info_table():
  execute_sql(sql_cmds['create_crew_info_table'])

def drop_crew_info_table():
  execute_sql('drop table crew_info_table')

def create_temp_passport_table():
  execute_sql(sql_cmds['create_temp_passport_table'])

def drop_temp_passport_table():
  execute_sql('drop table temp_passport_table;')

def create_table_space(spname):
  #execute_sql('')
	pass

def create_driver_rec_table():
  execute_sql(sql_cmds['create_driver_rec_table'])

def drop_driver_rec_table():
  execute_sql('drop table driver_rec_table')

def create_vechicle_rec_table():
  execute_sql(sql_cmds['create_vechicle_rec_table'])

def drop_vehicle_rec_table():
  execute_sql('drop table vech_rec_table')

def init_db():
  create_vehicle_info_table()
  create_driver_info_table()
  create_veh_drvr_rel_table()
  create_cruise_ship_table()
  create_company_table()
  create_shp_lcc_info_table()
  create_crew_info_table()
  create_temp_passport_table()
  create_driver_rec_table()
  create_vechicle_rec_table()

def create_all_tables():
  print globals().update(locals()).get('create_vehicle_info_table')

def run_sock_svr():
  HOST, PORT = socket.gethostbyname(socket.gethostname()), 9999
  server = SocketServer.TCPServer((HOST, PORT), SvrSockSvr)
  server.serve_forever()

def main():
  global dbconn
  if dbconn is None:
    dbconn = connect_orclex('haitong', '111111', DB_URL)
  print dbconn.version
  #drop_vehicle_info_table()
  #drop_driver_info_table()
  init_db()
  cur = dbconn.cursor()
  res = cur.execute('SELECT ZJBH from temp_passport_table')
  print res.fetchone()
  cur.close()
  dbconn.close()
  while True:
    pass

main()
