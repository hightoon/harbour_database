<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>数据库管理系统</title>
  <link rel="stylesheet" type="text/css" href="/static/view/style.css">
</head>
<body unresolved>
  <div id="main" class="managementpage">
    <div id="page-hdr" class="row">
      <h2>数据库管理系统</h2>
    </div>
    <div class="row">
      <div class="col-2">
        <ul class="block-list">
          <li><h4><a href="/query">查询</a></h4></li>
          <li><h4><a href="/vehicles">车辆管理</a></h4></li>
          <li><h4><a href="/drivers">司机管理</a></h4></li>
          <li><h4><a href="/companies">公司管理</a></h4></li>
          <li><h4><a href="/ships">船舶管理</a></h4></li>
          <li><h4><a href="/setting">设置</a></h4></li>
        </ul>
      </div>
      <div id="vehicle-manage-page" class="col-10">
        <h4>车辆管理 >>> 添加司机信息</h4>
        <form action="/add_driver" method="POST">
          <p>
            <label for="tlq">
              <span>停留期: </span>
              <input type="text" id="tlq" name="tlq" />
            </label>
            <label for="qwgdm">
              <span>前往国: </span>
              <input type="text" id="qwgdm" name="qwgdm" />
            </label>
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
            <label for="sfzh">
              <span>身份证号: </span>
              <input type="text" id="sfzh" name="sfzh" />
            </label>
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
              <!--select id="tw" name="tw">
                <option value="l" selected>左</option>
                <option value="r">右</option>
              </select-->
            </label>
            <label for="d2zjlbdm">
              <span>第二证件类别代码: </span>
              <input type="text" id="d2zjlbdm" name="d2zjlbdm" />
            </label>
            <label for="txkadm">
              <span>通行口岸代码: </span>
              <input type="text" id="txkadm" name="txkadm" />
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
            <label for="czr">
              <span>操作人代码: </span>
              <input type="text" id="czr" name="czr" />
            </label>
          </p>
          <p>
            <label for="czsj">
              <span>操作（录入）时间: </span>
              <input type="text" id="czsj" name="czsj" />
            </label>
            <label for="czkadm">
              <span>操作口岸: </span>
              <input type="text" id="czkadm" name="czkadm" />
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
            <label for="zjlbdm">
              <span>证件种类: </span>
              <!--input type="text" id="czsj" name="czsj" /-->
              <select id="zjlbdm" name="zjlbdm">
                <option value="14" selected>护照</option>
                <option value="10">身份证</option>
              </select>
            </label>
          </p>
          <p>
            <label for="xm">
              <span>姓名: </span>
              <input type="text" id="xm" name="xm" />
            </label>
            <label for="xbdm">
              <span>性别: </span>
              <input type="text" id="xbdm" name="xbdm" />
            </label>
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
            <label for="sqbh">
              <span>申请表号: </span>
              <input type="text" id="sqbh" name="sqbh" />
            </label>
            <label for="zjqzyxq">
              <span>准驾签注有效期: </span>
              <input type="text" id="zjqzyxq" name="zjqzyxq" />
            </label>
            <label for="gsqc">
              <span>公司全称: </span>
              <input type="text" id="gsqc" name="gsqc" />
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
            <label for="qzqzyxq">
              <span>签证签注有效期: </span>
              <input type="text" id="qzqzyxq" name="qzqzyxq" />
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
