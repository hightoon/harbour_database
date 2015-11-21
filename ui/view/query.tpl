<!DOCTYPE html>
<html>
%include('./view/html_header.tpl')
<body unresolved>
  <div id="main" class="managementpage">
    %include('./view/page_head.tpl')
    <div class="row">
      % include('./view/expanding_side_nav.tpl')
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
              <label for="vechicle">
                <span>船舶信息: </span>
                <input type="text" id="vechicle" name="vechicle" />
              </label>
              <label for="catlog">
                <span>类别: </span>
                <select id="catlog" name="cat">
                  <option value="登轮证">登轮证</option>
                  <option value="临时登轮证">临时登轮证</option>
                  <option value="长期登轮证">长期登轮证</option>
                  <option value="船员登陆证">船员登陆证</option>
                  <option value="登陆证">登陆证</option>
                  <option value="台湾船员登陆证">台湾船员登陆证</option>
                  <option value="临时入境许可">临时入境许可</option>
                  <option value="随船工作证">随船工作证</option>
                  <option value="海员证">海员证</option>
                  <option value="身份证">身份证</option>
                  <option value="驾照">驾照</option>
                  <option value="护照">护照</option>
                  <option value="" selected>全部</option>
                </select>
              </label>
              <label for="harbour">
                <span>港口: </span>
                  <select id="harbour" name="harbour">
                    <option value="横沙渔港1号">横沙渔港1号</option>
                    <option value="横沙渔港2号">横沙渔港2号</option>
                    <option value="" selected>全部</option>
                  </select>
              </label>
            </p>
            <p>
              <label for="station">
                <span>边检站: </span>
                <select id="station" name="station">
                    <option value="崇明边检站">崇明边检站</option>
                    <option value="" selected>全部</option>
                </select>
              </label>
              <label for="direction">
                <span>进出状态: </span>
                <select id="direction" name="direction">
                  <option value="进门">进门</option>
                  <option value="出门">出门</option>
                  <option value="连续两次进门">连续两次进门</option>
                  <option value="连续两次出门">连续两次出门</option>
                  <option value="第一次非法进门">第一次非法进门</option>
                  <option value="第一次非法出门">第一次非法出门</option>
                  <option value="" selected>全部</option>
                </select>
              </label>
              <label for="alarm">
                <span>报警状态:</span>
                <select id="alarm" name="alarm">
                  <option value="连续两次进门">连续两次进门</option>
                  <option value="连续两次出门">连续两次出门</option>
                  <option value="第一次非法进门">第一次非法进门</option>
                  <option value="第一次非法出门">第一次非法出门</option>
                  <option value="船舶离港报警">船舶离港报警</option>
                  <option value="" selected>全部</option>
                </select>
              </label>
            </p>
            <input type="submit" value="查询" />
            <button type="submit" name="export" value="yes">导出</button>
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
              <label for="company">
                <span>车牌: </span>
                <input type="text" id="company" name="company" />
              </label>
              <label for="idnum">
                <span>证件号: </span>
                <input type="text" id="idnum" name="idnum" />
              </label>
              <label for="direction">
                <span>进出状态: </span>
                <select id="direction" name="direction">
                  <option value="进门">进门</option>
                  <option value="出门">出门</option>
                  <option value="" selected>全部</option>
                </select>
              </label>
          </p>
          <input type="submit" value="查询" />
          <button type="submit" name="export" value="yes">导出</button>
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
        %if query_results:
        <h5>查询结果</h5>
        <!--table class="query-results"-->
        <table class="table table-bordered table-condensed">
          <tr>
            %for field in query_results[0]:
              <th class="nowrap">{{field}}</th>
            %end
            <th class="nowrap">操作</th>
          </tr>
          %for item in query_results[1:]:
            <tr>
            %for field in item:
              <td class="nowrap">
                %if str(field).endswith("jpg") or str(field).endswith("JPG"):
                  <a href="/static/./{{field}}">点击查看</a>
                %else:
                  {{field}}
                %end
              </td>
            %end
            %if 'recs' not in query_tbl:
            <td class="nowrap">
              <button type="button" onclick="if (confirm('操作无法撤销!确认删除?')){location.href='/del{{query_tbl}}/{{item[0]}}';}">删除</button>
              <button onclick="window.open('/{{query_tbl}}/{{item[0]}}', '记录更新', ' scrollbars=yes, width=900, height=800');">更新</button>
            </td>
            %else:
            <td class="nowrap">无可用操作</td>
            %end
            </tr>
          %end
        </table>
        %end
      </div>
    </div>
  </div>
</body>
</html>
