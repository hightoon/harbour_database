# -*- coding: utf-8 -*-
'''
  filename: VehicleDbFe.py
  description: deamon running in front end,
               read/sync entry records.
               Database is checked once an hour,
               and new data will be send to server side,
               to be restore to sql server db.
'''

import sqlite3, socket, SocketServer
from datetime import datetime
from SqlCmdHelper import sqlite_cmds

rec_db = None

def connect(dbfile='serverDb.db'):
  return sqlite3.connect(dbfile)

def create_table(tabname, tabfmt):
  if rec_db:
    c = rec_db.cursor()
    try:
      c.execute("CREATE TABLE %s %s"%(tabname, tabfmt))
      rec_db.commit()
    except sqlite3.OperationalError as e:
      print e
    c.close()

def drop_table(tabname):
  if rec_db:
    c = rec_db.cursor()
    c.execute("DROP TABLE IF EXISTS %s"%(tabname,))
    rec_db.commit()
    c.close()

def execute_sql(sql):
  if rec_db is not None:
    c = rec_db.cursor()
    try:
      c.execute(sql)
      rec_db.commit()
    except Exception as e:
      print e
    c.close()

def db_init():
  global rec_db
  if rec_db is None:
    rec_db = connect()
    rec_db.text_factory = str
    for tn in sqlite_cmds.keys():
      create_table(tn, sqlite_cmds[tn])
    rec_db.commit()

def drop_all():
  for tn in sqlite_cmds.keys():
    drop_table(tn)

class ClientSockSvr(SocketServer.BaseRequestHandler):
  def handle(self):
    # self.request is the TCP socket connected to the client
    self.data = self.request.recv(1024).strip().decode('utf-8')
    print "{} wrote:".format(self.client_address[0])
    self._process_data()
    
  def _process_data(self):
    print self.data
    if self.data.startswith('sql:'):
      sql = self.data[4:].strip()
      dbconn = connect()
      c = dbconn.cursor()
      c.execute(sql)
      dbconn.commit()
      c.close()
      dbconn.close()
      print 'table updated'
	
def run_sock_svr():
  HOST, PORT = socket.gethostbyname(socket.gethostname()), 9999
  server = SocketServer.TCPServer((HOST, PORT), ClientSockSvr)
  server.serve_forever()

def main():
  if rec_db is None:
    db_init()

if __name__ == '__main__':
  main()
