<!DOCTYPE html>
<html>
%include('./view/html_header.tpl')
<body unresolved>
  <div id="main" class="managementpage">
    %include('./view/page_head.tpl')
    <div class="row">
      % include('./view/expanding_side_nav.tpl')
      <div id="vehicle-manage-page" class="col-10">
        <h4>数据库管理 >>> 更新公司信息</h4>
        <form action="/company/{{rowid}}" method="POST">
          <p>
            <label for="gsdm">
              <span>公司代码: </span>
              <input type="text" id="gsdm" name="gsdm" value={{default_data['gsdm']}}>
            </label>
            <label for="gsqc">
              <span>公司全称: </span>
              <input type="text" id="gsqc" name="gsqc" value={{default_data['gsqc']}}>
            </label>
            <label for="gsjc">
              <span>公司简称: </span>
              <input type="text" id="gsjc" name="gsjc" value={{default_data['gsjc']}}>
            </label>
          </p>
          <p>
            <label for="lxdm">
              <span>类型代码: </span>
              <input type="text" id="lxdm" name="lxdm" value={{default_data['lxdm']}}>
            </label>
          </p>
          <p>
            <label for="ssgj">
              <span>所属国籍: </span>
              <input type="text" id="ssgj" name="ssgj" value={{default_data['ssgj']}}>
            </label>
            <label for="fzr">
              <span>负责人: </span>
              <input type="text" id="fzr" name="fzr" value={{default_data['fzr']}}>
            </label>
          </p>
          <p>
            <label for="ywfw">
              <span>业务范围（可组织的团体类型，多个以逗号间隔）: </span>
              <input type="text" id="ywfw" name="ywfw" value={{default_data['ywfw']}}>
            </label>
            <label for="sybj">
              <span>使用标记: </span>
              <select id="sybj" name="sybj">
                <option value="0">禁用</option>
                <option value="1">可用</option>
                <option value="" selected>不更改</option>
              </select>
            </label>
          </p>
          <p>
            <label for="czy">
              <span>录入检查员代码: </span>
              <input type="text" id="czy" name="czy" value={{default_data['czy']}}>
            </label>
            <label for="czsj">
              <span>录入时间: </span>
              <input type="text" id="czsj" name="czsj" value={{default_data['czsj']}}>
            </label>
            <label for="czkadm">
              <span>操作口岸代码: </span>
              <input type="text" id="czkadm" name="czkadm" value={{default_data['czkadm']}}>
            </label>
          </p>
          <p>
            <label for="bz">
              <span>备注: </span>
              <input type="text" id="bz" name="bz" value={{default_data['bz']}}>
            </label>
          </p>
          <input type="submit" value="更新" />
        </form>
      </div>
    </div>
  </div>
  <script type="text/javascript">
  </script>
</body>
</html>
