# -*- coding: utf-8 -*-
'''
  filename: VehicleDbFe.py
  description: deamon running in front end,
               read/sync entry records.
               Database is checked once an hour,
               and new data will be send to server side,
               to be restore to sql server db.
'''

import sqlite3
from datetime import datetime
from SqlCmdHelper import sqlite_cmds

rec_db = None

def connect(dbfile='records.db'):
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

def create_driver_rec_tab():
  tabname = 'drivers'
  tabfrmt = """
  ( name text
  , cat text
  , id text primary key
  , vechicle text
  , date text
  , harbour text
  , direction text
  , pic text
  )
  """
  create_table(tabname, tabfrmt)

def drop_driver_rec_db(self):
  pass

def create_vehicle_rec_tab():
  tabname = 'vehicles'
  tabfrmt = """
  ( plate text
  , company text
  , driver text
  , idtype text
  , idnum text primary key
  , date text
  , harbour text
  , direction text
  )
  """
  create_table(tabname, tabfrmt)

def db_init():
  global rec_db
  if rec_db is None:
    rec_db = connect()
    rec_db.text_factory = bytes
    for tn in sqlite_cmds.keys():
      create_table(tn, sqlite_cmds[tn])
    rec_db.commit()

def drop_all():
  for tn in sqlite_cmds.keys():
    drop_table(tn)

def main():
  if rec_db is None:
    db_init()
    drop_all()
  #while True:
  #  pass

def main_test():
  if rec_db is None:
    db_init()
  c = rec_db.cursor()
  photo = open('../wws.jpg')
  try:
    c.execute("insert into driver_rec_table values (?, ?, ?, ?, ?, ?, ?, ?)",
      ("维维", "d", "1234567", "", "", "", "", photo.read()))
    rec_db.commit()
  except sqlite3.IntegrityError:
    print "primary key already exists"
  photo.close()
  c.execute("select * from drivers where name=?", ("维维",))
  res = c.fetchone()
  print res[0]
  f = open("wws_backup.jpg", 'wb')
  f.write(res[-1])
  print len(res[-1])
  f.close()

if __name__ == '__main__':
  main()
