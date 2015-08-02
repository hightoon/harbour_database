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
      <div id="vehicle-manage-page" class="col-9">
        <h4>数据库管理 >>> 添加车辆信息</h4>
        <form action="/add_vehicle" method="POST">
          <p>尾部带<strong><abbr title="required">*</abbr></strong>为必填项。</p>
          <p>
            <label for="wycph">
              <span>唯一车牌号: </span>
              <input type="text" id="wycph" name="wycph" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="gsqc">
              <span>公司全称: </span>
              <input type="text" id="gsqc" name="gsqc" />
            </label>
          </p>
          <p>
            <label for="jwcph">
              <span>境外车牌号: </span>
              <input type="text" id="jwcph" name="jwcph" />
            </label>
            <label for="jncph">
              <span>境内车牌号: </span>
              <input type="text" id="jncph" name="jncph" />
            </label>
          </p>
          <p>
            <label for="ssgjdm">
              <span>所属国籍: </span>
              <input type="text" id="ssgjdm" name="ssgjdm" />
            </label>
            <label for="cllxdm">
              <span>车辆类型代码: </span>
              <select id="cllxdm" name="cllxdm">
                <option value="41" selected>货车</option>
                <option value="42">客车</option>
                <option value="43">小车</option>
                <option value="49">其他</option>
              </select>
            </label>
            <label for="clgd">
              <span>车辆高度: </span>
              <input type="text" id="clgd" name="clgd" />
            </label>
          </p>
          <p>
            <label for="tw">
              <span>肽位: </span>
              <!--input type="text" id="tw" name="tw" /-->
              <select id="tw" name="tw">
                <option value="l" selected>左</option>
                <option value="r">右</option>
              </select>
            </label>
            <label for="pwyxq">
              <span>批文有效期: </span>
              <input type="text" id="pwyxq" name="pwyxq" />
            </label>
            <label for="txkadm">
              <span>通行口岸代码: </span>
              <input type="text" id="txkadm" name="txkadm" />
            </label>
          </p>
          <p>
            <label for="txyxq">
              <span>通行有效期: </span>
              <input type="text" id="txyxq" name="txyxq" />
            </label>
            <label for="sqbh">
              <span>申请表号: </span>
              <input type="text" id="sqbh" name="sqbh" />
            </label>
            <label for="pwh">
              <span>现批文号码: </span>
              <input type="text" id="pwh" name="pwh" />
            </label>
          </p>
          <p>
            <label for="ksys">
              <span>款式颜色: </span>
              <input type="text" id="ksys" name="ksys" />
            </label>
            <label for="ctz">
              <span>车头字: </span>
              <input type="text" id="ctz" name="ctz" />
            </label>
            <label for="zzdw">
              <span>载重吨位: </span>
              <input type="text" id="zzdw" name="zzdw" />
            </label>
          </p>
          <p>
            <label for="cbdw">
              <span>内地承办单位(合营单位): </span>
              <input type="text" id="cbdw" name="cbdw" />
            </label>
            <label for="czy">
              <span>录入检查员代码: </span>
              <input type="text" id="czy" name="czy" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="czsj">
              <span>录入时间: </span>
              <input type="text" id="czsj" name="czsj" placeholder="2011-12-13 10:00"/>
              <strong><abbr title="required">*</abbr></strong>
            </label>
          </p>
          <p>
            <label for="czkadm">
              <span>操作口岸代码: </span>
              <input type="text" id="czkadm" name="czkadm" />
            </label>
            <label for="pd">
              <span>主司机: </span>
              <input type="text" id="pd" name="pd" />
            </label>
            <label for="sd">
              <span>副司机: </span>
              <input type="text" id="sd" name="sd" />
            </label>
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
