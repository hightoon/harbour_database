# -*- coding=utf-8 -*-

import sqlite3
from datetime import datetime

class User:
  IS_ADMIN = 1
  NOT_ADMIN = 0
  db_file = 'users.db'

  def __init__(self, usrname, password, is_admin=NOT_ADMIN,
              nickname='guest', desc='', role='', status='启用', regts='',
              access="边检1"):
    self._usrname = usrname
    self._password = password
    self._nickname = nickname
    self._desc = desc
    self._is_admin = is_admin
    self.access = access
    self.regtime = regts
    self.status = status
    self.role = role

  @property
  def usrname(self):
    return self._usrname

  @usrname.setter
  def usrname(self, name):
    self._usrname = name

  @property
  def password(self):
    return self._password

  @password.setter
  def password(self, passwd):
    self._password = passwd

  @property
  def nickname(self):
    return self._nickname

  @nickname.setter
  def nickname(self, nickname):
    self._nickname = nickname

  @property
  def email(self):
    return self._email

  @email.setter
  def email(self, email):
    self._email = email

  @property
  def desc(self):
    return self._desc

  @property
  def is_admin(self):
    return self._is_admin

  @is_admin.setter
  def is_admin(self, yesorno):
    self._is_admin = yesorno

  def put(self):
    conn =  sqlite3.connect(User.db_file)
    conn.text_factory = str
    cur = conn.cursor()
    if cur.execute('SELECT * FROM users WHERE name=?', (self.usrname,)).fetchone() is None:
      ts = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
      cur.execute('INSERT INTO users VALUES (?,?,?,?,?,?,?,?)',
        (self.usrname, self.password, self.is_admin, self.status, self.nickname, self.role, self.desc, ts)
      )
    conn.commit()
    cur.close()
    conn.close()

def create_user_table():
  conn =  sqlite3.connect(User.db_file)
  conn.text_factory = str
  cur = conn.cursor()
  try:
    cur.execute('CREATE TABLE users (name text primary key, passwd text, admin integer, status text, nickname text, role text, des text, regtime text)')
    conn.commit()
  except:
    print 'table users already existing'
  cur.close()
  conn.close()

def del_user(usrname):
 conn =  sqlite3.connect(User.db_file)
 conn.text_factory = str
 cur = conn.cursor()
 cur.execute('DELETE FROM users WHERE name=?', (usrname,))
 conn.commit()
 cur.close()
 conn.close()

def put_admin():
  user = User('admin', '000000', User.IS_ADMIN, '管理员', '系统管理员', role='系统管理员')
  user.put()

def get(usrname):
  conn =  sqlite3.connect(User.db_file)
  conn.text_factory = str
  cur = conn.cursor()
  userinfo = cur.execute('SELECT * FROM users WHERE name=?', (usrname,)).fetchone()
  if userinfo is not None:
    username, passwd, isadmin, status, nickname, role, desc, regts = userinfo
    return User(username, passwd, isadmin, nickname, desc, role, status, regts)
  else:
    return None

def fetch_users():
  "get all users from database"
  conn =  sqlite3.connect(User.db_file)
  conn.text_factory = str
  cur = conn.cursor()
  userinfo = cur.execute('SELECT * FROM users').fetchall()
  cur.close()
  conn.close()
  users = []
  for u in userinfo:
    username, passwd, isadmin, status, nickname, role, desc, regts = u
    users.append(User(username, passwd, isadmin, nickname, desc, role, status, regts))
  return users

def change_user_info(usr, desc, role, nickname):
  conn =  sqlite3.connect(User.db_file)
  conn.text_factory = str
  cur = conn.cursor()
  userinfo = cur.execute('UPDATE users SET des=?,role=?,nickname=? WHERE name=?',
                         (desc, role, nickname, usr))
  conn.commit()
  cur.close()
  conn.close()

def change_passwd(u, p):
  conn =  sqlite3.connect(User.db_file)
  conn.text_factory = str
  cur = conn.cursor()
  userinfo = cur.execute('UPDATE users SET passwd=? WHERE name=?', (p, u))
  conn.commit()
  cur.close()
  conn.close()

class Role():
  dbfile = 'role.db'
  def __init__(self, rolename='', privileges=[], desc='', status=''):
    self.rolename = rolename
    self.privileges = privileges
    self.status = status
    self.desc = desc

  def put(self):
    conn =  sqlite3.connect(Role.dbfile)
    conn.text_factory = str
    cur = conn.cursor()
    try:
      cur.execute('INSERT INTO roles VALUES (?,?,?,?)',
          (self.rolename, ' '.join(self.privileges), self.status, self.desc,))
      conn.commit()
    except Exception as e:
      print e
    finally:
      cur.close()
      conn.close()

def create_role_table():
  conn =  sqlite3.connect(Role.dbfile)
  conn.text_factory = str
  cur = conn.cursor()
  try:
    cur.execute('CREATE TABLE roles (rolename text primary key, priv text, status text, des text)')
    conn.commit()
  except:
    print 'table roles already existing'
  cur.close()
  conn.close()

def add_role(role):
  conn =  sqlite3.connect(Role.dbfile)
  conn.text_factory = str
  cur = conn.cursor()
  try:
    cur.execute('INSERT INTO roles VALUES (?,?,?,?)',
        (role.rolename, ' '.join(role.privileges), role.status, role.desc,))
    conn.commit()
  except Exception as e:
    print e
  finally:
    cur.close()
    conn.close()

def add_root():
  root = Role('系统管理员',
              ['sys', 'query', 'vehicle', 'driver', 'company', 'ship'],
              '系统管理员，具备所有权限，启动时默认创建。', '启用')
  root.put()

def update_privilege(rn, priv):
  conn =  sqlite3.connect(Role.dbfile)
  conn.text_factory = str
  cur = conn.cursor()
  cur.execute('UPDATE roles SET priv=? WHERE rolename=?', (' '.join(priv), rn,))
  conn.commit()
  cur.close()
  conn.close()

def update_role_status_desc(rn, status, desc):
  conn =  sqlite3.connect(Role.dbfile)
  conn.text_factory = str
  cur = conn.cursor()
  cur.execute('UPDATE roles SET status=?, des=? WHERE rolename=?', (status, desc, rn,))
  conn.commit()
  cur.close()
  conn.close()

def get_privilege(rn):
  conn =  sqlite3.connect(Role.dbfile)
  conn.text_factory = str
  cur = conn.cursor()
  p = cur.execute('SELECT * FROM roles WHERE rolename=?', (rn,)).fetchone()

  if p and p[2]=='启用': return p[1].split()
  else: return []

def get_roles():
  conn =  sqlite3.connect(Role.dbfile)
  conn.text_factory = str
  cur = conn.cursor()
  res = cur.execute('SELECT * FROM roles').fetchall()
  cur.close()
  conn.close()
  return res

def del_role(rn):
  conn =  sqlite3.connect(Role.dbfile)
  conn.text_factory = str
  cur = conn.cursor()
  res = cur.execute('DELETE FROM roles WHERE rolename=?', (rn,))
  conn.commit()
  cur.close()
  conn.close()
