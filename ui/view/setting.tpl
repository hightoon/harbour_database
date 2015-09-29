<!DOCTYPE html>
<html>
%include('./view/html_header.tpl')
<body>
  <div id="main" class="managementpage">
    %include('./view/page_head.tpl')
    <div class="row">
      % include('./view/expanding_side_nav.tpl')
      <div id="system-setting-page" class="col-10">
        %if setting == 'role_mng':
          <h4>系统管理 >>> 角色管理</h4>
          <form action="/add_role" method="POST">
            <div class="row" id="role-setting-form">
              <div class="col-8" id="user-input-setting">
              <label>角色名称: <input type="text" name="rn" /></label>
              <input type="checkbox" name="status" value="已启用">已启用
              <input type="checkbox" name="status" value="已停用">已停用
              <input type="checkbox" name="status" value="已删除">已删除
              </div>
              <div class="col-4" id="user-submit-setting">
              <input type="submit" name="query" value="查询" />
              <input type="submit" name="create" value="添加" />
              </div>
            </div>
          </form>
          <br/>
          <table class="role-mng-table">
            <tbody>
              <tr>
                <th>角色名称</th>
                <th>角色说明</th>
                <th>角色状态</th>
                <th>操作</th>
              </tr>
              %for role in roles:
                <tr>
                  <td>{{role[0]}}</td>
                  <td>{{role[3]}}</td>
                  <td>{{role[2]}}</td>
                  <td><a href="/edit_role/{{role[0]}}">编辑</a> &nbsp
                      <a href="/del_role/{{role[0]}}">删除</a></td>
                </tr>
              %end
            </tbody>
          </table>
        %elif setting == "edit_role":
          <h4>系统管理 >>> 角色管理 >>> 编辑</h4>
          <form action="/edit_role/{{role2edit}}", method="POST">
            <label>角色名称: {{role2edit}}</label>
            <label for="desc">角色描述:
              <input type="text" name="desc" id="desc"/>
            </label>
            <label>
              <select name="status" id="status">
                <option value="启用">启用</option>
                <option value="未启用">未启用</option>
              </select>
            </label>
            <input type="submit" value="提交" />
          </form>
        %elif setting == "access_granting":
          <h4>系统管理 >>> 角色管理</h4>
          <form action="/access_grant" method="POST">
            <div class="row" id="role-access-grant">
              <div class="col-8" id="grant-role-choice">
                <label>选择角色:
                  <select name="grant">
                    %for role in roles:
                      <option value="{{role[0]}}">{{role[0]}}</option>
                    %end
                  </select>
                </label>
              </div>
              <div class="col-4" id="grant-submit">
                <input type="submit" value="提交" />
              </div>
            </div>
            <div class="row" id="access-items">
              <ul class="access-list" id="access-tree">
                <li><input type="checkbox" name="web">边检网站系统
                  <ul>
                    <li><input type="checkbox" name="sys"><span>系统管理</span></li>
                    <!--li><input type="checkbox" name="basic"><span>基础设置</span></li-->
                    <li><input type="checkbox" name="query"><span>查询</span></li>
                    <li><input type="checkbox" name="vehicle"><span>车辆管理</span></li>
                    <li><input type="checkbox" name="driver"><span>司机管理</span></li>
                    <li><input type="checkbox" name="company"><span>公司管理</span></li>
                    <li><input type="checkbox" name="ship"><span>船舶管理</span></li>
                  </ul>
                </li>
              </ul>
            </div>
          </form>
        %elif setting == "accounts":
          <h4>系统管理 >>> 账号管理</h4>

          <form action="/account_query" method="POST">
            <div class="row" id="account-user-input">
              <div class="col-8">
                <label>账号名称: <input type="text" name="account" /></label>
              </div>
              <div class="col-4">
                <input type="submit" name="query" value="查询" />
                <input type="submit" name="create" value="添加" />
              </div>
            </div>
          </form>
          <br/>
          <div class="row" id="account-display">
            <table>
              <tbody>
                <tr>
                  <th>登录账号</th>
                  <th>员工姓名</th>
                  <th>备注</th>
                  <th>创建时间</th>
                  <th>账号角色</th>
                  <th>查询范围</th>
                  <th>操作</th>
                </tr>
                %for user in users:
                  <tr>
                    <td>{{user.usrname}}</td>
                    <td>{{user.nickname}}</td>
                    <td>{{user.desc}}</td>
                    <td>{{user.regtime}}</td>
                    <td>{{user.role}}</td>
                    <td>{{user.access}}</td>
                    <td><a href="/edit_user/{{user.usrname}}">编辑</a> &nbsp
                        <a href="/del_user/{{user.usrname}}">删除</a></td>
                  </tr>
                %end
              </tbody>
            </table>
          </div>
        %elif setting == "edit_user":
          <h4>系统管理 >>> 账号管理 >>> 编辑帐号</h4>
          <form action="/edit_user/{{usrname}}" method="POST">
            <label for="usrname"><span>用户名: {{usrname}}</span>
            </label>
            <label for="nickname">姓名:
              <input type="text" name="nickname" id="nickname" />
            </label>
            <label for="desc">备注:
              <input type="text" name="desc" id="desc" />
            </label>
            <!--label for="access">查询范围:
              <select name="access" id="access">
              </select>
            </label-->
            <label for="role">角色:
              <select name="role" id="role">
                %for role in roles:
                  <option value={{role[0]}}>{{role[0]}}</option>
                %end
              </select>
            </label>
            <input type="submit" value="提交" />
          </form>
        %elif setting == "adduser":
          <h4>系统管理 >>> 账号管理 >>> 添加帐号</h4>
          <form action="/update_user" method="POST">
            <label for="usrname"><span>用户名:</span>
              <input type="text" id="usrname" name="usrname" required />
            </label>
            <label for="passwd"><span>密码:</span>
              <input type="password" id="passwd" name="passwd" required />
            </label>
            <label for="role"><span>角色:</span>
              <!--input type="text" id="role" name="role" required /-->
              <select id="role" name="role">
                %for r in roles:
                  <option value="{{r[0]}}">{{r[0]}}</option>
                %end
              </select>
            </label>
            <label for="desc"><span>备注:</span>
              <input type="text" id="desc" name="desc" />
            </label>
            <label for="nickname"><span>姓名:</span>
              <input type="text" id="nickname" name="nickname" />
            </label>
            <label for="status"><span>状态:</span>
              <select id="status" name="status">
                <option name="activated">启用</option>
                <option name="deactivated">未启用</option>
              </select>
            </label>
            <input type="submit" value="提交"/>
          </form>
        %elif setting == "change_password":
          <h4>系统管理 >>> 账号管理 >>> 修改密码</h4>
          <form action="/change_passwd" method="POST">
            <label for="newp"><span>新密码:</span>
              <input type="password" name="newpass" id="newp" required />
            </label>
            <label for="cfnp"><span>确认新密码:</span>
              <input type="password" name="confirmedpass" id="cnfp" required />
            </label>
            <input type="submit" value="确认修改" />
          </form>
        %else:
          <h4>系统设置</h4>
        %end
      </div>
    </div>
  </div>
  <script type="text/javascript">
    $('#access-tree').checkboxTree();
  </script>
</body>
</html>
