<!DOCTYPE html>
<html>
%include('./view/html_header.tpl')
<body unresolved>
  <div id="main" class="managementpage">
    %include('./view/page_head.tpl')
    <div class="row">
      % include('./view/expanding_side_nav.tpl')
      <div id="vehicle-manage-page" class="col-10">
        <h4>数据库管理 >>> 更新司机信息</h4>
        <form action="/driver/{{rowid}}" method="POST">
          <p>
            <label for="tlq">
              <span>停留期: </span>
              <input type="text" id="tlq" name="tlq" value={{default_data['tlq']}}>
            </label>
            <label for="qwgdm">
              <span>前往国: </span>
              <input type="text" id="qwgdm" name="qwgdm" value={{default_data['qwgdm']}}>
            </label>
            <label for="lzgdm">
              <span>来自国: </span>
              <input type="text" id="lzgdm" name="lzgdm" value={{default_data['lzgdm']}}>
            </label>
            <label for="xkzh">
              <span>许可证号: </span>
              <input type="text" id="xkzh" name="xkzh" value={{default_data['xkzh']}}>
            </label>
          </p>
          <p>
            <label for="sfzh">
              <span>身份证号: </span>
              <input type="text" id="sfzh" name="sfzh" value={{default_data['sfzh']}}>
            </label>
            <label for="d2xm">
              <span>第2姓名: </span>
              <input type="text" id="d2xm" name="d2xm" value={{default_data['d2xm']}}>
            </label>
            <label for="d2csrq">
              <span>第2出生日期: </span>
              <input type="text" id="d2csrq" name="d2csrq" value={{default_data['d2csrq']}}>
            </label>
          </p>
          <p>
            <label for="d2zjhm">
              <span>第二证件号码: </span>
              <input type="text" id="d2zjhm" name="d2zjhm" value={{default_data['d2zjhm']}}>
            </label>
            <label for="d2zjlbdm">
              <span>第二证件类别代码: </span>
              <input type="text" id="d2zjlbdm" name="d2zjlbdm" value={{default_data['d2zjlbdm']}}>
            </label>
            <label for="txkadm">
              <span>通行口岸代码: </span>
              <input type="text" id="txkadm" name="txkadm" value={{default_data['txkadm']}}>
            </label>
          </p>
          <p>
            <label for="mzdm">
              <span>民族代码: </span>
              <input type="text" id="mzdm" name="mzdm" value={{default_data['mzdm']}}>
            </label>
            <label for="tybz">
              <span>通用标志: </span>
              <!--input type="text" id="sqbh" name="sqbh" /-->
              <select id="tybz" name="tybz">
                <option value="0">不能开公司所有车辆</option>
                <option value="1">可开公司所有车辆</option>
                <option value="" selected>不更改</option>
              </select>
            </label>
            <label for="czr">
              <span>操作人代码: </span>
              <input type="text" id="czr" name="czr" />
            </label>
          </p>
          <p>
            <label for="czsj">
              <span>操作（录入）时间: </span>
              <input type="text" id="czsj" name="czsj" value={{default_data['czsj']}}>
            </label>
            <label for="czkadm">
              <span>操作口岸: </span>
              <input type="text" id="czkadm" name="czkadm" value={{default_data['czkadm']}}>
            </label>
            <label for="bz">
              <span>备注: </span>
              <input type="text" id="bz" name="bz" value={{default_data['bz']}}>
            </label>
          </p>
          <p>
            <label for="qzh">
              <span>签证号: </span>
              <input type="text" id="qzh" name="qzh" value={{default_data['qzh']}}>
            </label>
            <label for="zjhm">
              <span>证件号码: </span>
              <input type="text" id="zjhm" name="zjhm" value={{default_data['zjhm']}}>
            </label>
            <label for="zjlbdm">
              <span>证件种类: </span>
              <!--input type="text" id="czsj" name="czsj" /-->
              <select id="zjlbdm" name="zjlbdm">
                <option value="14">护照</option>
                <option value="10">身份证</option>
                <option value="" selected>不更改</option>
              </select>
            </label>
          </p>
          <p>
            <label for="xm">
              <span>姓名: </span>
              <input type="text" id="xm" name="xm" value={{default_data['xm']}}>
            </label>
            <label for="xbdm">
              <span>性别: </span>
              <input type="text" id="xbdm" name="xbdm" value={{default_data['xbdm']}}>
            </label>
            <label for="csrq">
              <span>出生日期: </span>
              <input type="text" id="csrq" name="csrq" value={{default_data['csrq']}}>
            </label>
            <label for="gjdm">
              <span>国籍代码: </span>
              <input type="text" id="gjdm" name="gjdm" value={{default_data['gjdm']}}>
            </label>
          </p>
          <p>
            <label for="sqbh">
              <span>申请表号: </span>
              <input type="text" id="sqbh" name="sqbh" value={{default_data['sqbh']}}>
            </label>
            <label for="zjqzyxq">
              <span>准驾签注有效期: </span>
              <input type="text" id="zjqzyxq" name="zjqzyxq" value={{default_data['zjqzyxq']}}>
            </label>
            <label for="gsqc">
              <span>公司全称: </span>
              <input type="text" id="gsqc" name="gsqc" value={{default_data['gsqc']}}>
            </label>
          </p>
          <p>
            <label for="qzqzdm">
              <span>签证签注代码: </span>
              <input type="text" id="qzqzdm" name="qzqzdm" value={{default_data['qzqzdm']}}>
            </label>
            <label for="fzjgdm">
              <span>发证机关代码: </span>
              <input type="text" id="fzjgdm" name="fzjgdm" value={{default_data['fzjgdm']}}>
            </label>
          </p>
          <p>
            <label for="qzqzyxq">
              <span>签证签注有效期: </span>
              <input type="text" id="qzqzyxq" name="qzqzyxq" value={{default_data['qzqzyxq']}}>
            </label>
            <label for="ickh">
              <span>IC卡号: </span>
              <input type="text" id="ickh" name="ickh" value={{default_data['ickh']}}>
            </label>
          </p>
          <input type="submit" value="更新" />
        </form>
      </div>
    </div>
  </div>
  <script type="text/javascript">
  </script>
</body>
</html>
