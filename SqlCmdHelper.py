"""
  sql command helper
"""

sql_cmds = {
    'create_vehicle_info_table':\
    '''
    CREATE TABLE vehicleinfo
        (
          WYCPH   VARCHAR2(30 BYTE)               CONSTRAINT vhl_pk PRIMARY KEY,
          GSQC    VARCHAR2(100 BYTE)              NOT NULL,
          JWCPH   VARCHAR2(30 BYTE),
          JNCPH   VARCHAR2(30 BYTE),
          SSGJDM  VARCHAR2(3 BYTE)                NOT NULL,
          CLLXDM  VARCHAR2(2 BYTE)                NOT NULL,
          CLGD    NUMBER(3),
          TW      CHAR(1 BYTE)                    NOT NULL,
          PWYXQ   VARCHAR2(8 BYTE),
          TXKADM  VARCHAR2(40 BYTE)               NOT NULL,
          TXYXQ   VARCHAR2(90 BYTE)               NOT NULL,
          SQBH    VARCHAR2(10 BYTE)               NOT NULL,
          PWH     VARCHAR2(30 BYTE),
          KSYS    VARCHAR2(50 BYTE),
          CTZ     VARCHAR2(10 BYTE),
          ZZDW    NUMBER(3),
          CBDW    VARCHAR2(100 BYTE),
          CZY     VARCHAR2(8 BYTE)                NOT NULL,
          CZSJ    VARCHAR2(14 BYTE)               NOT NULL,
          CZKADM  CHAR(3 BYTE)                    NOT NULL,
          BZ      VARCHAR2(200 BYTE),
          PD      VARCHAR2(100 BYTE),
          SD      VARCHAR2(100 BYTE)
        )
    ''',

    'create_driver_info_table':\
    '''
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
      TLQ       VARCHAR2(3 BYTE),
      PRIMARY KEY (ZJHM, ZJLBDM, GJDQDM)
    )
    ''',

    'create_veh_drvr_rel_table':\
    '''
    CREATE TABLE vhl_drvr_relat
    (
      WYCPH      VARCHAR2(30 BYTE)                  NOT NULL CONSTRAINT vdr_pk PRIMARY KEY,
      ZSJZJHM    VARCHAR2(20 BYTE)                  NOT NULL,
      ZSJZJLBDM  VARCHAR2(2 BYTE)                   NOT NULL,
      ZSJGJDQDM  CHAR(3 BYTE)                       NOT NULL,
      FSJXX      VARCHAR2(300 BYTE)
    )
    ''',

    'create_cruise_ship_table':\
    '''
    CREATE TABLE crs_shp_table
    (
      HC        VARCHAR2(32 BYTE)                   NOT NULL,
      CBJSBS    VARCHAR2(30 BYTE)                   NOT NULL,
      CBDH      VARCHAR2(20 BYTE),
      JTGJLXDM  VARCHAR2(2 BYTE),
      CBZLDM    VARCHAR2(2 BYTE),
      ZWCBM     VARCHAR2(30 BYTE),
      YWCBM     VARCHAR2(30 BYTE),
      IMO       VARCHAR2(8 BYTE),
      GJHH      VARCHAR2(15 BYTE),
      GJDQDM    VARCHAR2(3 BYTE)                    NOT NULL,
      CYBGBS    VARCHAR2(1 BYTE),
      ZDGZBS    VARCHAR2(1 BYTE),
      DQJCFL    CHAR(1 BYTE)                        NOT NULL,
      DQJCZT    CHAR(1 BYTE)                        NOT NULL,
      KADM      VARCHAR2(3 BYTE)                    NOT NULL,
      CZY       VARCHAR2(8 BYTE)                    NOT NULL,
      CZBM      VARCHAR2(6 BYTE)                    NOT NULL,
      CZSJ      VARCHAR2(14 BYTE)                   NOT NULL,
      CJG       VARCHAR2(30 BYTE),
      DQTKMT    VARCHAR2(2 BYTE),
      DQTKBW    VARCHAR2(7 BYTE),
      JDXGZT    VARCHAR2(1 BYTE),
      JFR       VARCHAR2(20 BYTE),
      JFSJ      VARCHAR2(14 BYTE),
      QFR       VARCHAR2(20 BYTE),
      QFSJ      VARCHAR2(14 BYTE),
      WQDY      VARCHAR2(100 BYTE),
      JFKADM    VARCHAR2(3 BYTE),
      QFKADM    VARCHAR2(3 BYTE),
      YJBZ      VARCHAR2(1 BYTE),
      STATUS    CHAR(1 BYTE)
    )
    PCTUSED    40
    PCTFREE    10
    INITRANS   1
    MAXTRANS   255
    STORAGE    (
                INITIAL          132K
                MINEXTENTS       2
                MAXEXTENTS       UNLIMITED
                PCTINCREASE      0
                BUFFER_POOL      DEFAULT
               )
    LOGGING
    NOCOMPRESS
    NOCACHE
    NOPARALLEL
    NOMONITORING
    ''',

    'create_company_table':\
    '''
    CREATE TABLE company_table
    (
      GSDM    VARCHAR2(6 BYTE)                      NOT NULL,
      GSQC    VARCHAR2(100 BYTE)                    NOT NULL,
      GSJC    VARCHAR2(50 BYTE)                     NOT NULL,
      LXDM    CHAR(1 BYTE)                          NOT NULL,
      SSGJ    VARCHAR2(3 BYTE),
      FZR     VARCHAR2(50 BYTE),
      YWFW    VARCHAR2(30 BYTE),
      SYBJ    CHAR(1 BYTE)                          NOT NULL,
      CZY     VARCHAR2(8 BYTE)                      NOT NULL,
      CZSJ    VARCHAR2(14 BYTE)                     NOT NULL,
      CZKADM  CHAR(3 BYTE)                          NOT NULL,
      BZ      VARCHAR2(500 BYTE)
    )
    PCTUSED    40
    PCTFREE    10
    INITRANS   1
    MAXTRANS   255
    STORAGE    (
                INITIAL          132K
                MINEXTENTS       2
                MAXEXTENTS       UNLIMITED
                PCTINCREASE      0
                BUFFER_POOL      DEFAULT
               )
    LOGGING
    NOCOMPRESS
    NOCACHE
    NOPARALLEL
    NOMONITORING
    ''',

    'create_shp_lcc_info_table':\
    '''
    CREATE TABLE shp_lcc_info_table
    (
      ZJLB    VARCHAR2(2 BYTE)                      NOT NULL,
      ZJBH    VARCHAR2(15 BYTE)                     NOT NULL,
      ZWCBM   VARCHAR2(30 BYTE),
      YWCBM   VARCHAR2(30 BYTE),
      HC      VARCHAR2(32 BYTE),
      CBZLDM  VARCHAR2(2 BYTE),
      CH      VARCHAR2(20 BYTE),
      SSDW    VARCHAR2(100 BYTE),
      CJG     VARCHAR2(100 BYTE),
      DW      NUMBER(10,2),
      ML      NUMBER(7,2),
      YT      VARCHAR2(20 BYTE),
      DY      NUMBER(4),
      ZMSH    VARCHAR2(15 BYTE),
      PFWH    VARCHAR2(50 BYTE),
      DKCB    VARCHAR2(30 BYTE),
      PCDW    VARCHAR2(50 BYTE),
      XM      VARCHAR2(50 BYTE),
      XBDM    VARCHAR2(1 BYTE),
      GJDQDM  VARCHAR2(3 BYTE),
      CSRQ    VARCHAR2(8 BYTE),
      ZJLBDM  VARCHAR2(2 BYTE),
      ZJHM    VARCHAR2(20 BYTE),
      ZWDM    VARCHAR2(20 BYTE),
      ZSTS    NUMBER(3),
      DLZSBZ  VARCHAR2(1 BYTE),
      QXLX    VARCHAR2(1 BYTE),
      YXQQ    VARCHAR2(8 BYTE),
      YXQZ    VARCHAR2(8 BYTE),
      SQRQ    VARCHAR2(8 BYTE),
      SQSY    VARCHAR2(100 BYTE),
      BZ      VARCHAR2(500 BYTE),
      LDSPYJ  VARCHAR2(500 BYTE),
      SPLD    VARCHAR2(8 BYTE),
      SPRQ    VARCHAR2(8 BYTE),
      ZJZT    VARCHAR2(1 BYTE),
      CZY     VARCHAR2(8 BYTE),
      CZSJ    VARCHAR2(14 BYTE),
      CZBM    VARCHAR2(6 BYTE),
      KADM    VARCHAR2(3 BYTE),
      QFJG    VARCHAR2(3 BYTE),
      YCYXBZ  VARCHAR2(1 BYTE),
      TWSFZH  VARCHAR2(50 BYTE),
      TWZZ    VARCHAR2(100 BYTE)
    )
    PCTUSED    40
    PCTFREE    10
    INITRANS   1
    MAXTRANS   255
    STORAGE    (
                INITIAL          132K
                MINEXTENTS       2
                MAXEXTENTS       UNLIMITED
                PCTINCREASE      0
                BUFFER_POOL      DEFAULT
               )
    LOGGING
    NOCOMPRESS
    NOCACHE
    NOPARALLEL
    NOMONITORING
    ''',

    'create_crew_info_table':\
    '''
    CREATE TABLE crew_info_table
    (
      HC        VARCHAR2(32 BYTE)                   NOT NULL,
      XM        VARCHAR2(150 BYTE)                  NOT NULL,
      XBDM      VARCHAR2(1 BYTE)                    NOT NULL,
      CSRQ      VARCHAR2(8 BYTE)                    NOT NULL,
      GJDQDM    VARCHAR2(3 BYTE)                    NOT NULL,
      ZJLBDM    VARCHAR2(2 BYTE)                    NOT NULL,
      ZJHM      VARCHAR2(20 BYTE)                   NOT NULL,
      FZJGDM    VARCHAR2(4 BYTE),
      D2XM      VARCHAR2(50 BYTE),
      D2CSRQ    VARCHAR2(8 BYTE),
      D2ZJLBDM  VARCHAR2(2 BYTE),
      D2ZJHM    VARCHAR2(20 BYTE),
      QZZLDM    VARCHAR2(2 BYTE),
      ZWDM      VARCHAR2(2 BYTE),
      SCCJ      VARCHAR2(1 BYTE),
      DLZBLZT   VARCHAR2(1 BYTE),
      ZSZBLZT   VARCHAR2(1 BYTE),
      BZ        VARCHAR2(500 BYTE),
      LCBZ      VARCHAR2(1 BYTE),
      CKZT      VARCHAR2(1 BYTE),
      WYBS      CHAR(24 BYTE),
      CZY       VARCHAR2(8 BYTE),
      CZBM      VARCHAR2(6 BYTE),
      CZSJ      VARCHAR2(14 BYTE),
      YJCZY     VARCHAR2(8 BYTE),
      YJCZBM    VARCHAR2(6 BYTE),
      YJSJ      VARCHAR2(14 BYTE),
      ZJCZY     VARCHAR2(8 BYTE),
      ZJCZBM    VARCHAR2(6 BYTE),
      ZJSJ      VARCHAR2(14 BYTE),
      CRBZ      VARCHAR2(1 BYTE)                    NOT NULL,
      MZDM      VARCHAR2(2 BYTE),
      ZDYDM     VARCHAR2(2 BYTE),
      CRJSYDM   VARCHAR2(1 BYTE),
      ZSZBH     VARCHAR2(15 BYTE),
      DLZBH     VARCHAR2(15 BYTE),
      XZWP      VARCHAR2(300 BYTE),
      LCDJR     VARCHAR2(8 BYTE),
      LCDJSJ    VARCHAR2(14 BYTE),
      LCDJBM    VARCHAR2(6 BYTE),
      RYLB      VARCHAR2(2 BYTE),
      QWLZG     VARCHAR2(3 BYTE),
      LCSM      VARCHAR2(100 BYTE),
      RYXH      VARCHAR2(4 BYTE),
      JCFL      CHAR(1 BYTE),
      QZH       VARCHAR2(20 BYTE),
      TLQ       VARCHAR2(3 BYTE)
    )
    PCTUSED    40
    PCTFREE    10
    INITRANS   1
    MAXTRANS   255
    STORAGE    (
                INITIAL          132K
                MINEXTENTS       2
                MAXEXTENTS       UNLIMITED
                PCTINCREASE      0
                BUFFER_POOL      DEFAULT
               )
    LOGGING
    NOCOMPRESS
    NOCACHE
    NOPARALLEL
    NOMONITORING
    ''',

    'create_temp_passport_table':\
    '''
    CREATE TABLE temp_passport_table
    (
      ZJBH    VARCHAR2(15 BYTE)                     NOT NULL,
      ZJHM    VARCHAR2(20 BYTE)                     NOT NULL,
      ZJLBDM  VARCHAR2(2 BYTE)                      NOT NULL,
      XM      VARCHAR2(50 BYTE)                     NOT NULL,
      GJDQDM  VARCHAR2(3 BYTE)                      NOT NULL,
      FWCBMC  VARCHAR2(30 BYTE),
      HC      VARCHAR2(32 BYTE),
      RJKADM  VARCHAR2(3 BYTE),
      RJSJ    VARCHAR2(14 BYTE),
      ZJZT    VARCHAR2(1 BYTE)                      NOT NULL,
      CZY     VARCHAR2(8 BYTE),
      CZSJ    VARCHAR2(14 BYTE),
      CZBM    VARCHAR2(6 BYTE),
      KADM    VARCHAR2(3 BYTE),
      BZ      VARCHAR2(100 BYTE),
      XBDM    VARCHAR2(1 BYTE),
      CSRQ    VARCHAR2(8 BYTE)
    )
    PCTUSED    40
    PCTFREE    10
    INITRANS   1
    MAXTRANS   255
    STORAGE    (
                INITIAL          132K
                MINEXTENTS       2
                MAXEXTENTS       UNLIMITED
                PCTINCREASE      0
                BUFFER_POOL      DEFAULT
               )
    LOGGING
    NOCOMPRESS
    NOCACHE
    NOPARALLEL
    NOMONITORING
    ''',

    'create_driver_rec_table':\
    '''
    CREATE TABLE driver_rec_table
    ( DN	 	VARCHAR2(10 BYTE)  NOT NULL
    , CAT 	VARCHAR2(20 BYTE)  NOT NULL
    , ID 		VARCHAR2(20 BYTE)  NOT NULL CONSTRAINT id_pk PRIMARY KEY
    , VCHL 	VARCHAR2(20 BYTE)
    , DT	 	VARCHAR2(20 BYTE)
    , HAR		VARCHAR2(15 BYTE)
    , DIRCT VARCHAR2(15 BYTE)
    , PIC 	VARCHAR2(20 BYTE)
    )
    ''',

    'create_vechicle_rec_table':\
    '''
    CREATE TABLE vech_rec_table
    ( PLATE 	VARCHAR2(10 BYTE)  NOT NULL
    , COMPANY VARCHAR2(20 BYTE)  NOT NULL
    , DRIVER 	VARCHAR2(20 BYTE)  NOT NULL
    , IDTYPE 	VARCHAR2(10 BYTE)
    , IDNUM 	VARCHAR2(20 BYTE)
    , DT	 		VARCHAR2(20 BYTE)
    , HARBOUR VARCHAR2(15 BYTE)
    , DIRCT 	VARCHAR2(15 BYTE)
    , PIC 		VARCHAR2(30 BYTE)
    )
    '''
}
