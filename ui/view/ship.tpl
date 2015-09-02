<!DOCTYPE html>
<html>
%include('./view/html_header.tpl')
<body unresolved>
  <div id="main" class="managementpage">
    <div id="page-hdr" class="row">
      <h2>数据库管理系统</h2>
    </div>
    <div class="row">
      % include('./view/side_nav.tpl')
      <div id="vehicle-manage-page" class="col-9">
        <h4>数据库管理 >>> 添加船舶信息</h4>
        <form action="/add_ship" method="POST">
          <p>尾部带<strong><abbr title="required">*</abbr></strong>为必填项。</p>
          <p>
            <label for="hc">
              <span>航次(3位口岸代码+4位年+1位服务器序号+5位流水): </span>
              <input type="text" id="hc" name="hc" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
		  </p>
		  <p>
            <label for="cbjsbs">
              <span>船舶检索标识: </span>
              <input type="text" id="cbjsbs" name="cbjsbs" />
            </label>
            <label for="cbdh">
              <span>MMSI号: </span>
              <input type="text" id="cbdh" name="cbdh" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="jtgjlxdm">
              <span>交通工具类型代码: </span>
              <input type="text" id="jtgjlxdm" name="jtgjlxdm" />
            </label>
          </p>
          <p>
            <label for="cbzldm">
              <span>船舶种类代码: </span>
              <input type="text" id="cbzldm" name="cbzldm" />
            </label>
            <label for="zwcbm">
              <span>船舶中文名称: </span>
			  <input type="text" id="zwcbm" name="zwcbm" />
              <!--select id="cllxdm" name="cllxdm">
                <option value="41" selected>货车</option>
              </select-->
            </label>
            <label for="ywcbm">
              <span>船舶英文名称: </span>
              <input type="text" id="ywcbm" name="ywcbm" />
            </label>
          </p>
          <p>
            <label for="imo">
              <span>IMO号: </span>
              <input type="text" id="imo" name="imo" />
              <strong><abbr title="required">*</abbr></strong>
              <!--select id="tw" name="tw">
                <option value="l" selected>左</option>
                <option value="r">右</option>
              </select-->
            </label>
            <label for="gjhh">
              <span>国际呼号: </span>
              <input type="text" id="gjhh" name="gjhh" />
            </label>
            <label for="gjdqdm">
              <span>国籍地区代码: </span>
              <input type="text" id="gjdqdm" name="gjdqdm" />
            </label>
          </p>
          <p>
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
                <option value="rj" selected>入境</option>
                <option value="cj">出境</option>
				<option value="rg">入港</option>
                <option value="lg">出港</option>
              </select>
            </label>
          </p>
          <p>
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
            <label for="czy">
              <span>操作员: </span>
              <input type="text" id="czy" name="czy" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
          </p>
          <p>
            <label for="czsj">
              <span>操作时间: </span>
              <input type="text" id="czsj" name="czsj" placeholder="2011-12-13 14:15"/>
              <strong><abbr title="required">*</abbr></strong>
            </label>
            <label for="cjg">
              <span>船籍港: </span>
              <input type="text" id="cjg" name="cjg" />
            </label>
            <label for="dqtkmt">
              <span>当前停靠地(码头): </span>
              <input type="text" id="dqtkmt" name="dqtkmt" />
            </label>
          </p>
          <p>
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
		  </p>
		  <p>
            <label for="jfsj">
              <span>加封时间: </span>
              <input type="text" id="jfsj" name="jfsj" />
            </label>
			<label for="qfr">
              <span>启封人: </span>
              <input type="text" id="qfr" name="qfr" />
              <strong><abbr title="required">*</abbr></strong>
            </label>
			<label for="qfsj">
              <span>启封时间: </span>
              <input type="text" id="qfsj" name="qfsj" />
            </label>
          </p>
		  <p>
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
          </p>
		  <p>
            <label for="tjbz">
              <span>优检标志: </span>
              <input type="text" id="tjbz" name="tjbz" />
            </label>
			<label for="status">
              <span>船舶状态: </span>
              <input type="text" id="status" name="status" />
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
