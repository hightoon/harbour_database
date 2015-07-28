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
        <h4>车辆管理 >>> 添加公司信息</h4>
        <form action="/add_company" method="POST">
          <p>
            <label for="gsdm">
              <span>公司代码: </span>
              <input type="text" id="gsdm" name="gsdm" />
            </label>
            <label for="gsqc">
              <span>公司全称: </span>
              <input type="text" id="gsqc" name="gsqc" />
            </label>
            <label for="gsjc">
              <span>公司简称: </span>
              <input type="text" id="gsjc" name="gsjc" />
            </label>
            <label for="lxdm">
              <span>类型代码: </span>
              <input type="text" id="lxdm" name="lxdm" />
            </label>
          </p>
          <p>
            <label for="ssgj">
              <span>所属国籍: </span>
              <input type="text" id="ssgj" name="ssgj" />
            </label>
            <label for="fzr">
              <span>负责人: </span>
              <input type="text" id="fzr" name="fzr" />
            </label>
          </p>
          <p>
            <label for="ywfw">
              <span>业务范围（可组织的团体类型，多个以逗号间隔）: </span>
              <input type="text" id="ywfw" name="ywfw" />
            </label>
            <label for="sybj">
              <span>使用标记: </span>
              <select id="sybj" name="sybj">
                <option value="0" selected>禁用</option>
                <option value="1">可用</option>
              </select>
            </label>
          </p>
          <p>
            <label for="czy">
              <span>录入检查员代码: </span>
              <input type="text" id="czy" name="czy" />
            </label>
            <label for="czsj">
              <span>录入时间: </span>
              <input type="text" id="czsj" name="czsj" />
            </label>
            <label for="czkadm">
              <span>操作口岸代码: </span>
              <input type="text" id="czkadm" name="czkadm" />
            </label>
          </p>
          <p>
            <label for="bz">
              <span>备注: </span>
              <input type="text" id="bz" name="bz" />
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
