<!DOCTYPE html>
<html>
%include('./view/html_header.tpl')
<body unresolved>
  <div id="main" class="managementpage">
    %include('./view/page_head.tpl')
    <div class="row">
      % include('./view/expanding_side_nav.tpl')
      <div id="vehicle-manage-page" class="col-10">
        <h4>数据库管理 >>> 添加船舶信息</h4>
        <form action="/add_ship" method="POST">
          <p>尾部带<strong><abbr title="required">*</abbr></strong>为必填项。</p>
          <p>
            <label for="hc">
              <span>航次(3位口岸代码+4位年+1位服务器序号+5位流水): </span>
              <input type="text" id="hc" name="hc" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="cbdh">
              <span>MMSI号: </span>
              <input type="text" id="cbdh" name="cbdh" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="imo">
              <span>IMO号: </span>
              <input type="text" id="imo" name="imo" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="czy">
              <span>操作员: </span>
              <input type="text" id="czy" name="czy" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="czsj">
              <span>操作时间: </span>
              <input type="text" id="czsj" name="czsj" placeholder="2011-12-13 14:15"/>
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="qfr">
              <span>启封人: </span>
              <input type="text" id="qfr" name="qfr" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="zwcbm">
              <span>船舶中文名称: </span>
              <input type="text" id="zwcbm" name="zwcbm" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="ywcbm">
              <span>船舶英文名称: </span>
              <input type="text" id="ywcbm" name="ywcbm" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="status">
              <span>船舶状态: </span>
              <select id="status" name="status">
                <option value="在港">在港</option>
                <option value="离港">离港</option>
              </select>
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="cbjsbs">
              <span>船舶检索标识: </span>
              <input type="text" id="cbjsbs" name="cbjsbs" />
            </label>
            
            <label for="jtgjlxdm">
              <span>交通工具类型代码: </span>
              <input type="text" id="jtgjlxdm" name="jtgjlxdm" />
            </label>
            <label for="cbzldm">
              <span>船舶种类代码: </span>
              <input type="text" id="cbzldm" name="cbzldm" />
            </label>
            
            <label for="gjhh">
              <span>国际呼号: </span>
              <input type="text" id="gjhh" name="gjhh" />
            </label>
            <label for="gjdqdm">
              <span>国籍地区代码: </span>
              <input type="text" id="gjdqdm" name="gjdqdm" />
            </label>
            <label for="cybgbs">
              <span>船员变更标识: </span>
              <input type="text" id="cybgbs" name="cybgbs" />
            </label>
            <label for="zdgzbs">
              <span>重点关注标识: </span>
              <input type="text" id="zdgzbs" name="zdgzbs" />
            </label>
            <label for="dqjcfl">
              <span>当前检查分类: </span>
              <!--input type="text" id="dqjcfl" name="dqjcfl" /-->
			  <select id="dqjcfl" name="dqjcfl">
                <option value="入境" selected>入境</option>
                <option value="出境">出境</option>
				        <option value="入港">入港</option>
                <option value="出港">出港</option>
              </select>
            </label>
            <label for="dqjczt">
              <span>当前检查状态: </span>
              <!--input type="text" id="ksys" name="ksys" /-->
			  <select id="dqjczt" name="dqjczt">
                <option value="1" selected>确报</option>
                <option value="2">预检正常</option>
				<option value="3">预检异常</option>
                <option value="5">正检正常</option>
				<option value="6">正检异常</option>
				<option value="8">检查结束</option>
				<option value="9">归档</option>
              </select>
            </label>
            <label for="kadm">
              <span>口岸代码: </span>
              <input type="text" id="kadm" name="kadm" />
            </label>
            <label for="cjg">
              <span>船籍港: </span>
              <input type="text" id="cjg" name="cjg" />
            </label>
            <label for="dqtkmt">
              <span>当前停靠地(码头): </span>
              <input type="text" id="dqtkmt" name="dqtkmt" />
            </label>
            <label for="dqtkbw">
              <span>当前停靠地(泊位): </span>
              <input type="text" id="dqtkbw" name="dqtkbw" />
            </label>
            <label for="jdxgzt">
              <span>解档修改状态: </span>
              <input type="text" id="jdxgzt" name="jdxgzt" />
            </label>
            <label for="jfr">
              <span>加封人: </span>
              <input type="text" id="jfr" name="jfr" />
            </label>
            <label for="jfsj">
              <span>加封时间: </span>
              <input type="text" id="jfsj" name="jfsj" />
            </label>
			      <label for="qfsj">
              <span>启封时间: </span>
              <input type="text" id="qfsj" name="qfsj" />
            </label>
            <label for="wqdy">
              <span>武器弹药: </span>
              <input type="text" id="wqdy" name="wqdy" />
            </label>
			      <label for="jfkadm">
              <span>加封口岸: </span>
              <input type="text" id="jfkadm" name="jfkadm" />
            </label>
			      <label for="qfkadm">
              <span>启封口岸: </span>
              <input type="text" id="qfkadm" name="qfkadm" />
            </label>
            <label for="tjbz">
              <span>优检标志: </span>
              <input type="text" id="tjbz" name="tjbz" />
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
