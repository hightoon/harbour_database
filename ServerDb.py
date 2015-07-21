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
  COMMENT ON TABLE QGTG.BJ_YW_T_CLZL IS '车辆资料库';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.WYCPH IS '唯一车牌号';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.GSQC IS '公司全称';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.JWCPH IS '境外车牌号';（境外境内车牌二选一）

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.JNCPH IS '境内车牌号';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.SSGJDM IS '所属国籍';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CLLXDM IS '车辆类型代码';货车：41，客车，42，小车，43，其他49

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CLGD IS '车辆高度';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.TW IS '肽位（1：左；0：右）';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.PWYXQ IS '批文有效期';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.TXKADM IS '通行口岸代码(最多10个';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.TXYXQ IS '通行有效期(最多10个';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.SQBH IS '申请表号';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.PWH IS '现批文号码';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.KSYS IS '款式颜色';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CTZ IS '车头字';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.ZZDW IS '载重吨位';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CBDW IS '内地承办单位(合营单位';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CZY IS '录入检查员代码';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CZSJ IS '录入时间';

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CZKADM IS '操作口岸代码'（崇明：373）;

  COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.BZ IS '备注';

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
    COMMENT ON TABLE QGTG.BJ_YW_T_SJZL IS '司机资料库';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.TLQ IS '停留期';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.QWGDM IS '前往国';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.LZGDM IS '来自国';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.XKZH IS '许可证号';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.SFZH IS '身份证号';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.D2XM IS '第2姓名';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.D2CSRQ IS '第2出生日期';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.D2ZJHM IS '第二证件号码';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.D2ZJLBDM IS '第二证件类别代码';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.MZDM IS '民族代码';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.TYBZ IS '通用标志：1可开公司所有车辆；0不能开公司所有车辆';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.CZY IS '操作人代码';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.CZSJ IS '操作（录入）时间';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.CZKADM IS '操作口岸';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.BZ IS '备注';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.QZH IS '签证号';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.ZJHM IS '证件号码';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.ZJLBDM IS '证件种类';（护照14，身份证10）

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.XM IS '姓名';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.XBDM IS '性别';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.CSRQ IS '出生日期';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.GJDQDM IS '国籍代码';（中国CHN）

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.ZJYXQ IS '证件有效日期';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.SQBH IS '申请表号';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.ZJQZYXQ IS '准驾签注有效期';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.GSQC IS '公司全称';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.QZQZDM IS '签证签注代码';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.FZJGDM IS '发证机关代码';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.QZQZYXQ IS '签证签注有效期';

    COMMENT ON COLUMN QGTG.BJ_YW_T_SJZL.ICKH IS 'IC卡号';
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
    
