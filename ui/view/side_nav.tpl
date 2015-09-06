<div class="col-2" id="side-nav-bar">
    <ul class="block-list">
      %if "query" in privs:
      <li><div class="nav-item"><a href="#">查询</a></div>
        <ul class="sub-block-list">
          <li><div class="sub-nav-item"><a href="/query_driver_recs">人员进出纪录</a></div></li>
          <li><div class="sub-nav-item"><a href="/query_vehicle_recs">车辆进出纪录</a></div></li>
        </ul>
      </li>
      %end
      %if "vehicle" in privs:
      <li><div class="nav-item"><a href="/vehicles">车辆管理</a></div></li>
      %end
      %if "driver" in privs:
      <li><div class="nav-item"><a href="/drivers">司机管理</a></div></li>
      %end
      %if "company" in privs:
      <li><div class="nav-item"><a href="/companies">公司管理</a></div></li>
      %end
      %if "ship" in privs:
      <li><div class="nav-item"><a href="/ships">船舶管理</a></div></li>
      %end
      %if "sys" in privs:
      <li><div class="nav-item"><a href="#">系统管理</a></div>
        <ul class="sub-block-list">
          <li><div class="sub-nav-item"><a href="/user_roles">角色管理</a></div></li>
          <li><div class="sub-nav-item"><a href="/access_control">权限管理</a></div></li>
          <li><div class="sub-nav-item"><a href="/account_mngn">账号管理</a></div></li>
          <li><div class="sub-nav-item"><a href="/change_passwd">修改密码</a></div></li>
        </ul>
      </li>
      %end 
      <li><div class="nav-item"><a href="/logout">退出登陆</a></div></li>
    </ul>
</div>
