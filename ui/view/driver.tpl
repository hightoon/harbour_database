<!DOCTYPE html>
<html>
%include('./view/html_header.tpl')
<body unresolved>
  <div id="main" class="managementpage">
    %include('./view/page_head.tpl')
    <div class="row">
      % include('./view/expanding_side_nav.tpl')
      <div id="vehicle-manage-page" class="col-10">
        <h4>数据库管理 >>> 添加司机信息</h4>
        <form action="/add_driver" method="POST">
          <p>尾部带<strong><abbr title="required">*</abbr></strong>为必填项。</p>
          <p>
            <label for="sfzh">
              <span>身份证号: </span>
              <input type="text" id="sfzh" name="sfzh" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="czr">
              <span>操作人代码: </span>
              <input type="text" id="czr" name="czr" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
          </p>
          <p>
            <label for="czsj">
              <span>操作（录入）时间: </span>
              <input type="text" id="czsj" name="czsj" placeholder="2011-12-13 14:15"/>
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="czkadm">
              <span>操作口岸: </span>
              <input type="text" id="czkadm" name="czkadm" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
          </p>
          <p>
            <label for="xm">
              <span>姓名: </span>
              <input type="text" id="xm" name="xm" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="sqbh">
              <span>申请表号: </span>
              <input type="text" id="sqbh" name="sqbh" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
          </p>
          <p>
            <label for="qzqzyxq">
              <span>签证签注有效期: </span>
              <input type="text" id="qzqzyxq" name="qzqzyxq" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="zjlbdm">
              <span>证件种类: </span>
              <!--input type="text" id="czsj" name="czsj" /-->
              <select id="zjlbdm" name="zjlbdm">
                <option value="14" selected>护照</option>
                <option value="10">身份证</option>
              </select>
            </label>
            <label for="gsqc">
              <span>公司全称: </span>
              <input type="text" id="gsqc" name="gsqc" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="zjqzyxq">
              <span>准驾签注有效期: </span>
              <input type="text" id="zjqzyxq" name="zjqzyxq" />
            </label>
          </p>
          <p>
            <label for="tlq">
              <span>停留期: </span>
              <input type="text" id="tlq" name="tlq" />
            </label>
            <label for="qwgdm">
              <span>前往国: </span>
              <input type="text" id="qwgdm" name="qwgdm" />
            </label>
          </p>
          <p>
            <label for="lzgdm">
              <span>来自国: </span>
              <input type="text" id="lzgdm" name="lzgdm" />
            </label>
            <label for="xkzh">
              <span>许可证号: </span>
              <input type="text" id="xkzh" name="xkzh" />
            </label>
          </p>
          <p>
            <label for="d2xm">
              <span>第2姓名: </span>
              <input type="text" id="d2xm" name="d2xm">
            </label>
            <label for="d2csrq">
              <span>第2出生日期: </span>
              <input type="text" id="d2csrq" name="d2csrq" />
            </label>
          </p>
          <p>
            <label for="d2zjhm">
              <span>第二证件号码: </span>
              <input type="text" id="d2zjhm" name="d2zjhm" />
            </label>
            <label for="d2zjlbdm">
              <span>第二证件类别代码: </span>
              <input type="text" id="d2zjlbdm" name="d2zjlbdm" />
            </label>
          </p>
          <p>
            <label for="mzdm">
              <span>民族代码: </span>
              <input type="text" id="mzdm" name="mzdm" />
            </label>
            <label for="tybz">
              <span>通用标志: </span>
              <!--input type="text" id="sqbh" name="sqbh" /-->
              <select id="tybz" name="tybz">
                <option value="0" selected>不能开公司所有车辆</option>
                <option value="1">可开公司所有车辆</option>
              </select>
            </label>
          </p>
          <p>
            <label for="txkadm">
              <span>通行口岸代码: </span>
              <input type="text" id="txkadm" name="txkadm" />
            </label>
            <label for="bz">
              <span>备注: </span>
              <input type="text" id="bz" name="bz" />
            </label>
          </p>
          <p>
            <label for="qzh">
              <span>签证号: </span>
              <input type="text" id="qzh" name="qzh" />
            </label>
            <label for="zjhm">
              <span>证件号码: </span>
              <input type="text" id="zjhm" name="zjhm" />
            </label>
          </p>
          <p>
            <label for="csrq">
              <span>出生日期: </span>
              <input type="text" id="csrq" name="csrq" />
            </label>
            <label for="gjdm">
              <span>国籍代码: </span>
              <input type="text" id="gjdm" name="gjdm" />
            </label>
          </p>
          <p>
            <label for="qzqzdm">
              <span>签证签注代码: </span>
              <input type="text" id="qzqzdm" name="qzqzdm" />
            </label>
            <label for="fzjgdm">
              <span>发证机关代码: </span>
              <input type="text" id="fzjgdm" name="fzjgdm" />
            </label>
          </p>
          <p>
            <label for="xbdm">
              <span>性别: </span>
              <input type="text" id="xbdm" name="xbdm" />
            </label>
            <label for="ickh">
              <span>IC卡号: </span>
              <input type="text" id="ickh" name="ickh" />
            </label>
          </p>
          <input type="submit" value="添加" />
        </form>
      </div>
    </div>
  </div>
  <script type="text/javascript">
  </script>
</body>
</html>
