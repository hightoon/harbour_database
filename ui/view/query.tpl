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
      <div id="query-page" class="col-10">
        <h4 id="query-drivers">查询 >>> 人员进出</h4>
        <form action="/query_drivers" method="POST">
          <p>
            <label for="startdate">
              <span>开始日期: </span>
              <input type="text" id="startdate" name="startdate" />
            </label>
            <label for="enddate">
              <span>结束日期: </span>
              <input type="text" id="enddate" name="enddate" />
            </label>
            <label for="name">
              <span>姓名: </span>
              <input type="text" id="name" name="name" />
            </label>
          </p>
          <p>
            <!--label for="shipname">
              <span>船舶名称: </span>
              <input type="text" id="shipname" name="shipname" />
            </label-->
            <!--label for="status">
              <span>进出状态: </span>
              <input type="text" id="status" name="status" />
            </label-->
          </p>
          <input type="submit" value="查询" />
        </form>
        <h4 id="query-vehicles">查询 >>> 车辆进出</h4>
        <form action="/query_vehicles" method="POST">
          <p>
              <label for="startdate">
                <span>开始日期: </span>
                <input type="text" id="startdate" name="startdate" />
              </label>
              <label for="enddate">
                <span>结束日期: </span>
                <input type="text" id="enddate" name="enddate" />
              </label>
              <label for="plate">
                <span>车牌: </span>
                <input type="text" id="plate" name="plate" />
              </label>
          </p>
          <input type="submit" value="查询" />
        </form>
        <h4 id="query-company">查询 >>> 公司信息</h4>
        <form action="/query_company" method="POST">
          <p>
              <label for="fullname">
                <span>公司全称: </span>
                <input type="text" id="fullname" name="fullname" />
              </label>
          </p>
          <input type="submit" value="查询" />
        </form>
        <h4 id="query-vehicle-info">查询 >>> 车辆信息</h4>
        <form action="/query_vehicle_info" method="POST">
          <p>
              <label for="plate">
                <span>车牌号: </span>
                <input type="text" id="plate" name="plate" />
              </label>
          </p>
          <input type="submit" value="查询" />
        </form>
        <h4 id="query-driver-info">查询 >>> 司机信息</h4>
        <form action="/query_driver_info" method="POST">
          <p>
              <label for="name">
                <span>姓名: </span>
                <input type="text" id="name" name="name" />
              </label>
          </p>
          <input type="submit" value="查询" />
        </form>
        <h4 id="query-ship">查询 >>> 船舶信息</h4>
        <form action="/query_ship" method="POST">
          <p>
              <label for="cruise">
                <span>航次: </span>
                <input type="text" id="cruise" name="cruise" />
              </label>
          </p>
          <input type="submit" value="查询" />
        </form>
        <br/><br/>
        <h5>查询结果</h5>
        <table class="query-results">
          %for item in query_results:
            <tr>
            %for field in item:
              <td>
                %if field.endswith("jpg") or field.endswith("JPG"):
                  <img src="/static/./{{field}}" alt={{field}} width="140" height="100">
                %else:
                  {{field}}
                %end
              </td>
            %end
            </tr>
          %end
        </table>
      </div>
    </div>
  </div>
  <script type="text/javascript">
  </script>
</body>
</html>
