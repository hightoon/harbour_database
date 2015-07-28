#-*- coding: utf-8 -*-

"""
  sql command helper

  Comments on table columns:

    table vehicleinfo:
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

    COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.CZKADM IS '操作口岸代码';（崇明：373）

    COMMENT ON COLUMN QGTG.BJ_YW_T_CLZL.BZ IS '备注';

    COMMENT ON COLUMN PD                   IS 'primary driver';

    COMMENT ON COLUMN SD                   IS 'secondary driver';

    table driverinfo:
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

    table vhl_drvr_relat:
    COMMENT ON TABLE QGTG.BJ_YW_T_CLSJGLGX IS '车辆司机关联关系';

    COMMENT ON COLUMN QGTG.BJ_YW_T_CLSJGLGX.WYCPH IS '唯一车牌号';

    COMMENT ON COLUMN QGTG.BJ_YW_T_CLSJGLGX.ZSJZJHM IS '主司机证件号码';

    COMMENT ON COLUMN QGTG.BJ_YW_T_CLSJGLGX.ZSJZJLBDM IS '主司机证件类别';

    COMMENT ON COLUMN QGTG.BJ_YW_T_CLSJGLGX.ZSJGJDQDM IS '主司机国籍';

    COMMENT ON COLUMN QGTG.BJ_YW_T_CLSJGLGX.FSJXX IS '副司机信息';

    table crs_shp_table:
    COMMENT ON TABLE QGTG.BJ_CB_T_CBHCZB IS '船舶航次总表';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.HC IS '航次(3位口岸代码+4位年+1位服务器序号+5位流水)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.CBJSBS IS '船舶检索标识';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.CBDH IS 'MMSI号';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.JTGJLXDM IS '交通工具类型代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.CBZLDM IS '船舶种类代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.ZWCBM IS '船舶中文名称';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.YWCBM IS '船舶英文名称';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.IMO IS 'IMO号';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.GJHH IS '国际呼号';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.GJDQDM IS '国籍地区代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.CYBGBS IS '船员变更标识';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.ZDGZBS IS '重点关注标识';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.DQJCFL IS '当前检查分类（入境/出境/入港/出港/）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.DQJCZT IS '当前检查状态（1：确报、2：预检正常、3：预检异常、5：正检正常、6：正检异常、8：检查结束、9：归档）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.KADM IS '口岸代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.CZY IS '操作员';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.CZBM IS '操作部门';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.CZSJ IS '操作时间';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.CJG IS '船籍港';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.DQTKMT IS '当前停靠地（码头）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.DQTKBW IS '当前停靠地（泊位）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.JDXGZT IS '解档修改状态';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.JFR IS '加封人';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.JFSJ IS '加封时间';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.QFR IS '启封人';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.QFSJ IS '启封时间';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.WQDY IS '武器弹药';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.JFKADM IS '加封口岸';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.QFKADM IS '启封口岸';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBHCZB.YJBZ IS '优检标志';

    COMMENT ON COLUMN STATUS IS 'ON/OFF HARBOUR';

    注：加一项   船舶状态  （注：如 在港、离港）

    table company_table:
    COMMENT ON TABLE QGTG.BJ_YW_T_GSZL IS '公司资料库';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.GSDM IS '公司代码';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.GSQC IS '公司全称';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.GSJC IS '公司简称';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.LXDM IS '类型代码';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.SSGJ IS '所属国籍';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.FZR IS '负责人';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.YWFW IS '业务范围（可组织的团体类型，多个以逗号间隔）';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.SYBJ IS '使用标记 0：禁用，1：可用';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.CZY IS '操作员';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.CZSJ IS '操作时间';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.CZKADM IS '操作口岸';

    COMMENT ON COLUMN QGTG.BJ_YW_T_GSZL.BZ IS '备注';

    table shp_lcc_info_table:
    COMMENT ON TABLE QGTG.BJ_CB_T_CBZJFF IS '船舶证件发放信息库';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.ZJLB IS '发放证件类别';（48是登轮证，50是台湾船员登陆证）

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.ZJBH IS '证件编号（2位证类＋3位口岸代码＋4位年＋1位服务器序号+5位流水号）'（前两位数字可以判断证件类型）;

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.ZWCBM IS '船舶中文名（随船工作证登轮许可证证明书查验簿搭靠外轮许可证）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.YWCBM IS '船舶英文名（随船工作证登轮许可证）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.HC IS '服务船舶航次(登陆证住宿证,3位口岸代码+4位年+1位服务器序号+5位流水)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.CBZLDM IS '船舶种类代码(证明书查验簿)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.CH IS '船号（查验簿）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.SSDW IS '所属单位';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.CJG IS '船籍港(证明书查验簿搭靠外轮证)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.DW IS '吨位(证明书查验簿搭靠外轮证)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.ML IS '马力(搭靠外轮证)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.YT IS '用途(搭靠外轮证)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.DY IS '定员(证明书查验簿)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.ZMSH IS '证明书号(查验簿)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.PFWH IS '批复文号(证明书)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.DKCB IS '搭靠船舶（搭靠外轮证）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.PCDW IS '派出单位';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.XM IS '姓名';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.XBDM IS '性别代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.GJDQDM IS '国籍地区代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.CSRQ IS '出生日期';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.ZJLBDM IS '所持证件类别代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.ZJHM IS '所持证件号码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.ZWDM IS '职务代码（登轮许可证为名称）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.ZSTS IS '住宿天数(住宿证)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.DLZSBZ IS '是否登轮住宿(登轮证)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.QXLX IS '登轮证期限类型（长期、临时）(登轮证)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.YXQQ IS '有效期起';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.YXQZ IS '有效期止（特殊：登轮许可证中包括“本航次”）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.SQRQ IS '申请日期';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.SQSY IS '申请事由';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.BZ IS '备注';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.LDSPYJ IS '领导审批意见';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.SPLD IS '审批领导';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.SPRQ IS '审批日期';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.ZJZT IS '证件状态（1：发放、2：注销、3：挂失、4：回收（登陆证）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.CZY IS '操作员';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.CZSJ IS '操作时间';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.CZBM IS '操作部门';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.KADM IS '口岸代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.QFJG IS '签发机关';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.YCYXBZ IS '一次有效标志';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.TWSFZH IS '台湾身份证号';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CBZJFF.TWZZ IS '台湾住址';

    table crew_info_table:
    COMMENT ON TABLE QGTG.BJ_CB_T_CYMD IS '船员名单申报库';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.QZH IS '签证号';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.TLQ IS '停留期';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.XBDM IS '性别代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.CSRQ IS '出生日期';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.GJDQDM IS '国籍地区代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.ZJLBDM IS '证件类别代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.ZJHM IS '证件号码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.FZJGDM IS '发证机关代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.D2XM IS '第二姓名';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.D2CSRQ IS '第二出生日期';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.D2ZJLBDM IS '第二证件类别代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.D2ZJHM IS '第二证件号码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.QZZLDM IS '签证/签注种类代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.ZWDM IS '职务代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.SCCJ IS '是否首次出境';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.DLZBLZT IS '登陆证办理状态（0.未申请/回收、1.申请办理、2.已办理）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.ZSZBLZT IS '住宿证办理状态（0.未申请/回收、1.申请办理、2.已办理）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.BZ IS '疑难字说明';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.LCBZ IS '登/离船标志(0：在船1：离船、2：登船、3：在船（信息变更）)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.CKZT IS '查控状态（已查控、未查控）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.WYBS IS '出入境（港）唯一标识号';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.CZY IS '操作员';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.CZBM IS '操作部门';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.CZSJ IS '操作时间';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.YJCZY IS '预检检查员';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.YJCZBM IS '预检检查队';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.YJSJ IS '预检检查时间';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.ZJCZY IS '正检检查员';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.ZJCZBM IS '正检检查队';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.ZJSJ IS '正检检查时间';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.CRBZ IS '出入标志（1：入、2：出）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.MZDM IS '民族代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.ZDYDM IS '自定义代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.CRJSYDM IS '入出境事由';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.ZSZBH IS '住宿证编号';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.DLZBH IS '登陆证编号';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.XZWP IS '限制物品';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.LCDJR IS '离船登记人';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.LCDJSJ IS '离船登记时间';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.LCDJBM IS '离船登记部门';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.RYLB IS '人员类别';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.QWLZG IS '前往/来自国';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.LCSM IS '登/离船说明';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.RYXH IS '人员序号';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.JCFL IS '检查分类';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.HC IS '航次(3位口岸代码+4位年+1位服务器序号+5位流水)';

    COMMENT ON COLUMN QGTG.BJ_CB_T_CYMD.XM IS '姓名';

    table temp_passport_table:
    COMMENT ON TABLE QGTG.BJ_CB_T_LSRJXK IS '临时入境许可信息';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.ZJBH IS '入境许可编号（3位口岸代码+6位日期+1位服务器序号+5位流水号）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.ZJHM IS '所持证件号码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.ZJLBDM IS '所持证件种类';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.XM IS '船员姓名';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.GJDQDM IS '所属国家地区代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.FWCBMC IS '服务船舶名称';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.HC IS '服务船舶航次';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.RJKADM IS '入境口岸';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.RJSJ IS '入境时间';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.ZJZT IS '证件状态（1－有效，0－无效）';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.CZY IS '签发操作员';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.CZSJ IS '签发操作时间';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.CZBM IS '签发部门';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.KADM IS '签发口岸';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.BZ IS '备注';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.XBDM IS '性别代码';

    COMMENT ON COLUMN QGTG.BJ_CB_T_LSRJXK.CSRQ IS '出生日期';

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
      TYBZ      CHAR(1 BYTE)                        DEFAULT '0'        NOT NULL,
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

sql_table_columns = {
  'vehicleinfo': \
  '''
  ( WYCPH
  , GSQC
  , JWCPH
  , JNCPH
  , SSGJDM
  , CLLXDM
  , CLGD
  , TW
  , PWYXQ
  , TXKADM
  , TXYXQ
  , SQBH
  , PWH
  , KSYS
  , CTZ
  , ZZDW
  , CBDW
  , CZY
  , CZSJ
  , CZKADM
  , BZ
  , PD
  , SD
  ''',

  'driverinfo': \
  '''
  ( ZJHM
  , ZJLBDM
  , XM
  , XBDM
  , CSRQ
  , GJDQDM
  , ZJYXQ
  , SQBH
  , ZJQZYXQ
  , GSQC
  , QZQZDM
  , FZJGDM
  , QZQZYXQ
  , ICKH
  , QWGDM
  , LZGDM
  , XKZH
  , SFZH
  , D2XM
  , D2CSRQ
  , D2ZJHM
  , D2ZJLBDM
  , MZDM
  , TYBZ
  , CZY
  , CZSJ
  , CZKADM
  , BZ
  , QZH
  , TLQ)
  ''',

  'crs_shp_table': \
  '''
  ( HC
  , CBJSBS
  , CBDH
  , JTGJLXDM
  , CBZLDM
  , ZWCBM
  , YWCBM
  , IMO
  , GJHH
  , GJDQDM
  , CYBGBS
  , ZDGZBS
  , DQJCFL
  , DQJCZT
  , KADM
  , CZY
  , CZBM
  , CZSJ
  , CJG
  , DQTKMT
  , DQTKBW
  , JDXGZT
  , JFR
  , JFSJ
  , QFR
  , QFSJ
  , WQDY
  , JFKADM
  , QFKADM
  , YJBZ
  , STATUS
  )
  ''',

  'company_table': \
  '''
  ( GSDM
  , GSQC
  , GSJC
  , LXDM
  , SSGJ
  , FZR
  , YWFW
  , SYBJ
  , CZY
  , CZSJ
  , CZKADM
  , BZ
  )
  ''',
}

sqlite_cmds = {
  'vehicle_info_table':\
  '''
      (
        WYCPH   text PRIMARY KEY,
        GSQC    text,
        JWCPH   text,
        JNCPH   text,
        SSGJDM  text,
        CLLXDM  text,
        CLGD    integer,
        TW      text,
        PWYXQ   text,
        TXKADM  text,
        TXYXQ   text,
        SQBH    text,
        PWH     text,
        KSYS    text,
        CTZ     text,
        ZZDW    integer,
        CBDW    text,
        CZY     text,
        CZSJ    text,
        CZKADM  text,
        BZ      text,
        PD      text,
        SD      text
      )
  ''',

  'driver_info_table':\
  '''
  (
    ZJHM      text,
    ZJLBDM    text,
    XM        text,
    XBDM      text,
    CSRQ      text,
    GJDQDM    text,
    ZJYXQ     text,
    SQBH      text,
    ZJQZYXQ   text,
    GSQC      text,
    QZQZDM    text,
    FZJGDM    text,
    QZQZYXQ   text,
    ICKH      text,
    QWGDM     text,
    LZGDM     text,
    XKZH      text,
    SFZH      text,
    D2XM      text,
    D2CSRQ    text,
    D2ZJHM    text,
    D2ZJLBDM  text,
    MZDM      text,
    TYBZ      text,
    CZY       text,
    CZSJ      text,
    CZKADM    text,
    BZ        text,
    QZH       text,
    TLQ       text
  )
  ''',

  'veh_drvr_rel_table':\
  '''
  (
    WYCPH      text PRIMARY KEY,
    ZSJZJHM    text,
    ZSJZJLBDM  text,
    ZSJGJDQDM  text,
    FSJXX      text
  )
  ''',

  'crs_shp_table':\
  '''
  (
    HC        text,
    CBJSBS    text,
    CBDH      text,
    JTGJLXDM  text,
    CBZLDM    text,
    ZWCBM     text,
    YWCBM     text,
    IMO       text,
    GJHH      text,
    GJDQDM    text,
    CYBGBS    text,
    ZDGZBS    text,
    DQJCFL    text,
    DQJCZT    text,
    KADM      text,
    CZY       text,
    CZBM      text,
    CZSJ      text,
    CJG       text,
    DQTKMT    text,
    DQTKBW    text,
    JDXGZT    text,
    JFR       text,
    JFSJ      text,
    QFR       text,
    QFSJ      text,
    WQDY      text,
    JFKADM    text,
    QFKADM    text,
    YJBZ      text,
    STATUS    text
  )
  ''',

  'company_table':\
  '''
  (
    GSDM    text,
    GSQC    text,
    GSJC    text,
    LXDM    text,
    SSGJ    text,
    FZR     text,
    YWFW    text,
    SYBJ    text,
    CZY     text,
    CZSJ    text,
    CZKADM  text,
    BZ      text
  )
  ''',

  'shp_lcc_info_table':\
  '''
  (
    ZJLB    text,
    ZJBH    text,
    ZWCBM   text,
    YWCBM   text,
    HC      text,
    CBZLDM  text,
    CH      text,
    SSDW    text,
    CJG     text,
    DW      integer,
    ML      integer,
    YT      text,
    DY      integer,
    ZMSH    text,
    PFWH    text,
    DKCB    text,
    PCDW    text,
    XM      text,
    XBDM    text,
    GJDQDM  text,
    CSRQ    text,
    ZJLBDM  text,
    ZJHM    text,
    ZWDM    text,
    ZSTS    integer,
    DLZSBZ  text,
    QXLX    text,
    YXQQ    text,
    YXQZ    text,
    SQRQ    text,
    SQSY    text,
    BZ      text,
    LDSPYJ  text,
    SPLD    text,
    SPRQ    text,
    ZJZT    text,
    CZY     text,
    CZSJ    text,
    CZBM    text,
    KADM    text,
    QFJG    text,
    YCYXBZ  text,
    TWSFZH  text,
    TWZZ    text
  )
  ''',

  'crew_info_table':\
  '''
  (
    HC        text,
    XM        text,
    XBDM      text,
    CSRQ      text,
    GJDQDM    text,
    ZJLBDM    text,
    ZJHM      text,
    FZJGDM    text,
    D2XM      text,
    D2CSRQ    text,
    D2ZJLBDM  text,
    D2ZJHM    text,
    QZZLDM    text,
    ZWDM      text,
    SCCJ      text,
    DLZBLZT   text,
    ZSZBLZT   text,
    BZ        text,
    LCBZ      text,
    CKZT      text,
    WYBS      text,
    CZY       text,
    CZBM      text,
    CZSJ      text,
    YJCZY     text,
    YJCZBM    text,
    YJSJ      text,
    ZJCZY     text,
    ZJCZBM    text,
    ZJSJ      text,
    CRBZ      text,
    MZDM      text,
    ZDYDM     text,
    CRJSYDM   text,
    ZSZBH     text,
    DLZBH     text,
    XZWP      text,
    LCDJR     text,
    LCDJSJ    text,
    LCDJBM    text,
    RYLB      text,
    QWLZG     text,
    LCSM      text,
    RYXH      text,
    JCFL      text,
    QZH       text,
    TLQ       text
  )
  ''',

  'temp_passport_table':\
  '''
  (
    ZJBH    text,
    ZJHM    text,
    ZJLBDM  text,
    XM      text,
    GJDQDM  text,
    FWCBMC  text,
    HC      text,
    RJKADM  text,
    RJSJ    text,
    ZJZT    text,
    CZY     text,
    CZSJ    text,
    CZBM    text,
    KADM    text,
    BZ      text,
    XBDM    text,
    CSRQ    text
  )
  ''',

  'driver_rec_table':\
  '''
  ( name text
  , cat text
  , id text primary key
  , vechicle text
  , date text
  , harbour text
  , direction text
  , pic text
  )
  ''',

  'vehicle_rec_table':\
  '''
  ( plate text
  , company text
  , driver text
  , idtype text
  , idnum text primary key
  , date text
  , harbour text
  , direction text
  )
  '''
}
