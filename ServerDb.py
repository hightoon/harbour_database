#-*- coding: utf-8 -*-
'''
  file: VisitorDb.py
  description:
'''

import cx_Oracle, socket

dbconn = None
DB_URL = socket.gethostbyname(socket.gethostname()) + '/XE'

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
    except cx_Oracle.DatabaseError:
      pass # table exists
    cur.close()

def create_vehicle_info_table():
  """
  COMMENT ON TABLE QGTG.BJ_YW_T_CLZL IS '�������Ͽ�';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.WYCPH IS 'Ψһ���ƺ�';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.GSQC IS '��˾ȫ��';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.JWCPH IS '���⳵�ƺ�';�����⾳�ڳ��ƶ�ѡһ��

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.JNCPH IS '���ڳ��ƺ�';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.SSGJDM IS '��������';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CLLXDM IS '�������ʹ���';������41���ͳ���42��С����43������49

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CLGD IS '�����߶�';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.TW IS '��λ��1����0���ң�';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.PWYXQ IS '������Ч��';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.TXKADM IS 'ͨ�пڰ�����(���10��';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.TXYXQ IS 'ͨ����Ч��(���10��';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.SQBH IS '������';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.PWH IS '�����ĺ���';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.KSYS IS '��ʽ��ɫ';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CTZ IS '��ͷ��';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.ZZDW IS '���ض�λ';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CBDW IS '�ڵسа쵥λ(��Ӫ��λ';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CZY IS '¼����Ա����';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CZSJ IS '¼��ʱ��';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CZKADM IS '�����ڰ�����'��������373��;

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.BZ IS '��ע';

  COMMENT ON COLUMN PD                   IS 'primary driver';

  COMMENT ON COLUMN SD                   IS 'secondary driver';
  """
  sql = '''
    CREATE TABLE vehicleinfo
    (
      WYCPH   VARCHAR2(30 BYTE)                     NOT NULL,
      GSQC    VARCHAR2(100 BYTE)                    NOT NULL,
      JWCPH   VARCHAR2(30 BYTE),
      JNCPH   VARCHAR2(30 BYTE),
      SSGJDM  VARCHAR2(3 BYTE)                      NOT NULL,
      CLLXDM  VARCHAR2(2 BYTE)                      NOT NULL,
      CLGD    NUMBER(3),
      TW      CHAR(1 BYTE)                          NOT NULL,
      PWYXQ   VARCHAR2(8 BYTE),
      TXKADM  VARCHAR2(40 BYTE)                     NOT NULL,
      TXYXQ   VARCHAR2(90 BYTE)                     NOT NULL,
      SQBH    VARCHAR2(10 BYTE)                     NOT NULL,
      PWH     VARCHAR2(30 BYTE),
      KSYS    VARCHAR2(50 BYTE),
      CTZ     VARCHAR2(10 BYTE),
      ZZDW    NUMBER(3),
      CBDW    VARCHAR2(100 BYTE),
      CZY     VARCHAR2(8 BYTE)                      NOT NULL,
      CZSJ    VARCHAR2(14 BYTE)                     NOT NULL,
      CZKADM  CHAR(3 BYTE)                          NOT NULL,
      BZ      VARCHAR2(200 BYTE)
      PD      VARCHAR2(100 BYTE)
      SD      VARCHAR2(100 BYTE)
    )
  '''
  execute_sql(sql)

def drop_vehicle_info_table():
  execute_sql('drop table vehicleinfo')

def create_driver_info_table():
  """
    COMMENT ON TABLE QGTG.BJ_YW_T_SJZL IS '˾�����Ͽ�';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.TLQ IS 'ͣ����';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.QWGDM IS 'ǰ����';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.LZGDM IS '���Թ�';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.XKZH IS '���֤��';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.SFZH IS '���֤��';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.D2XM IS '��2����';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.D2CSRQ IS '��2��������';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.D2ZJHM IS '�ڶ�֤������';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.D2ZJLBDM IS '�ڶ�֤��������';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.MZDM IS '�������';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.TYBZ IS 'ͨ�ñ�־��1�ɿ���˾���г�����0���ܿ���˾���г���';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.CZY IS '�����˴���';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.CZSJ IS '������¼�룩ʱ��';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.CZKADM IS '�����ڰ�';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.BZ IS '��ע';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.QZH IS 'ǩ֤��';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.ZJHM IS '֤������';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.ZJLBDM IS '֤������';������14�����֤10��

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.XM IS '����';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.XBDM IS '�Ա�';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.CSRQ IS '��������';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.GJDQDM IS '��������';���й�CHN��

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.ZJYXQ IS '֤����Ч����';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.SQBH IS '������';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.ZJQZYXQ IS '׼��ǩע��Ч��';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.GSQC IS '��˾ȫ��';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.QZQZDM IS 'ǩ֤ǩע����';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.FZJGDM IS '��֤���ش���';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.QZQZYXQ IS 'ǩ֤ǩע��Ч��';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.ICKH IS 'IC����';
  """
  sql = '''
    CREATE TABLE driverinfo
    (
      ZJHM      VARCHAR2(20 BYTE)                   NOT NULL,
      ZJLBDM    CHAR(2 BYTE)                        NOT NULL,
      XM        VARCHAR2(50 BYTE)                   NOT NULL,
      XBDM      CHAR(1 BYTE)                        NOT NULL,
      CSRQ      VARCHAR2(8 BYTE)                    NOT NULL,
      GJDQDM    VARCHAR2(3 BYTE)                    NOT NULL,
      ZJYXQ     VARCHAR2(8 BYTE)                    NOT NULL,
      SQBH      VARCHAR2(10 BYTE)                   NOT NULL,
      ZJQZYXQ   VARCHAR2(8 BYTE)                    NOT NULL,
      GSQC      VARCHAR2(100 BYTE)                  NOT NULL,
      QZQZDM    VARCHAR2(2 BYTE),
      FZJGDM    VARCHAR2(4 BYTE),
      QZQZYXQ   VARCHAR2(8 BYTE),
      ICKH      VARCHAR2(10 BYTE),
      QWGDM     VARCHAR2(3 BYTE),
      LZGDM     VARCHAR2(3 BYTE),
      XKZH      VARCHAR2(20 BYTE),
      SFZH      VARCHAR2(20 BYTE),
      D2XM      VARCHAR2(50 BYTE),
      D2CSRQ    VARCHAR2(8 BYTE),
      D2ZJHM    VARCHAR2(20 BYTE),
      D2ZJLBDM  VARCHAR2(2 BYTE),
      MZDM      VARCHAR2(2 BYTE),
      TYBZ      CHAR(1 BYTE)                        DEFAULT '0'                   NOT NULL,
      CZY       VARCHAR2(8 BYTE)                    NOT NULL,
      CZSJ      VARCHAR2(14 BYTE)                   NOT NULL,
      CZKADM    CHAR(3 BYTE)                        NOT NULL,
      BZ        VARCHAR2(200 BYTE),
      QZH       VARCHAR2(20 BYTE),
      TLQ       VARCHAR2(3 BYTE)
    )
  '''
  execute_sql(sql)

def drop_driver_info_table():
  execute_sql('drop table driverinfo')

def init_db():
  create_vehicle_info_table()
  create_driver_info_table()

def main():
  global dbconn
  if dbconn is None:
    dbconn = connect_orclex('haitong', '111111', DB_URL)
  print dbconn.version
  #drop_vehicle_info_table()
  #drop_driver_info_table()
  init_db()
  dbconn.close()

main()
    
