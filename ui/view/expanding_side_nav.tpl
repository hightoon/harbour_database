<div class="col-2" id="side-nav-bar">
      %if "query" in privs:
      <a class="side-menu" onclick="showHide('query_items');location.href='/tempstate/query_items/'+document.getElementById('query_items').className">+查询</a>
      <div id="query_items" class="{{querydisp}}">
        <a class="side-submenu" href="/query_driver_recs">- 人员进出纪录</a>
        <a class="side-submenu" href="/query_vehicle_recs">- 车辆进出纪录</a>
        <a class="side-submenu" href="/query_company">- 公司信息</a>
        <a class="side-submenu" href="/query_vehicle_info">- 车辆信息</a>
        <a class="side-submenu" href="/query_driver_info">- 司机信息</a>
        <a class="side-submenu" href="/query_ship">- 船舶信息</a>
      </div>
      %end
      %if "vehicle" in privs:
      <a class="side-menu" href="/vehicles" >车辆管理</a>
      %end
      %if "driver" in privs:
      <a class="side-menu" href="/drivers">司机管理</a>
      %end
      %if "company" in privs:
      <a class="side-menu" href="/companies">公司管理</a>
      %end
      %if "ship" in privs:
      <a class="side-menu" href="/ships">船舶管理</a>
      %end
      %if "sys" in privs:
      <a class="side-menu" onclick="showHide('setting_items');location.href='/tempstate/setting_items/'+document.getElementById('setting_items').className">+系统管理</a>
      <div id="setting_items" class="{{settingdisp}}">
        <a class="side-submenu" href="/user_roles">- 角色管理</a>
        <a class="side-submenu" href="/access_control">- 权限管理</a>
        <a class="side-submenu" href="/account_mngn">- 账号管理</a>
        <a class="side-submenu" href="/change_passwd">- 修改密码</a>
      </div>
      %end
      <a class="side-menu" href="/logout">退出登陆</a>
</div>
