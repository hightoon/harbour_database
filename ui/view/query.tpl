<!DOCTYPE html>
<html>
%include('./view/html_header.tpl')
<body unresolved>
  <div id="main" class="managementpage">
    <div id="page-hdr" class="row">
      <h2>数据库管理系统</h2>
    </div>
    <div class="row">
      % include ("./view/side_nav.tpl")
      <div id="query-page" class="col-10">
        %if query_tbl == 'driver_recs':
          <h4 id="query-drivers">查询 >>> 人员进出纪录</h4>
          <form action="/query_drivers" method="POST">
            <p>
              <label for="startdate">
                <span>开始日期: </span>
                <input type="date" id="startdate" name="start" />
              </label>
              <label for="enddate">
                <span>结束日期: </span>
                <input type="date" id="enddate" name="end" />
              </label>
              <label for="name">
                <span>姓名: </span>
                <input type="text" id="name" name="name" />
              </label>
            </p>
            <p>
              <label for="vehicle">
                <span>车辆信息: </span>
                <input type="text" id="vehicle" name="vehicle" />
              </label>
              <label for="catlog">
                <span>类别: </span>
                <input type="text" id="catlog" name="cat" />
              </label>
              <label for="harbour">
                <span>港口: </span>
                <input type="text" id="harbour" name="harbour" />
              </label>
            </p>
            <p>
              <label for="direction">
                <span>进出状态: </span>
                <select id="direction" name="direction">
                  <option value="进门">进门</option>
                  <option value="出门">出门</option>
                  <option value="">全部</option>
                </select>
              </label>
            </p>
            <input type="submit" value="查询" />
          </form>
        %elif query_tbl == 'vehicle_recs':
        <h4 id="query-vehicles">查询 >>> 车辆进出纪录</h4>
        <form action="/query_vehicles" method="POST">
          <p>
              <label for="start">
                <span>开始日期: </span>
                <input type="date" id="start" name="start" />
              </label>
              <label for="end">
                <span>结束日期: </span>
                <input type="date" id="end" name="end" />
              </label>
              <label for="plate">
                <span>车牌: </span>
                <input type="text" id="plate" name="plate" />
              </label>
          </p>
          <p>
              <label for="idnum">
                <span>证件号: </span>
                <input type="text" id="idnum" name="idnum" />
              </label>
              <label for="direction">
                <span>进出状态: </span>
                <select id="direction" name="direction">
                  <option value="进门">进门</option>
                  <option value="出门">出门</option>
                  <option value="">全部</option>
                </select>
              </label>
          </p>
          <input type="submit" value="查询" />
        </form>
        %elif query_tbl == 'company':
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
        %elif query_tbl == 'vehicle':
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
        %elif query_tbl == 'driver':
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
        %elif query_tbl == 'ship':
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
        %end
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
