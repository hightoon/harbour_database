<!DOCTYPE html>
<html>
%include('./view/html_header.tpl')
<body unresolved>
  <div id="main" class="managementpage">
    %include('./view/page_head.tpl')
    <div class="row">
      % include('./view/expanding_side_nav.tpl')
      <div id="vehicle-manage-page" class="col-10">
        <h4>数据库管理 >>> 更新船舶信息</h4>
        <form action="/ship/{{rowid}}" method="POST">
          <p>
            <label for="hc">
              <span>航次(3位口岸代码+4位年+1位服务器序号+5位流水): </span>
              <input type="text" id="hc" name="hc" value={{default_data['hc']}}>
            </label>
		      </p>
		      <p>
            <label for="cbjsbs">
              <span>船舶检索标识: </span>
              <input type="text" id="cbjsbs" name="cbjsbs" value={{default_data['cbjsbs']}}>
            </label>
            <label for="cbdh">
              <span>MMSI号: </span>
              <input type="text" id="cbdh" name="cbdh" value={{default_data['cbdh']}}>
            </label>
            <label for="jtgjlxdm">
              <span>交通工具类型代码: </span>
              <input type="text" id="jtgjlxdm" name="jtgjlxdm" value={{default_data['jtgjlxdm']}}>
            </label>
          </p>
          <p>
            <label for="cbzldm">
              <span>船舶种类代码: </span>
              <input type="text" id="cbzldm" name="cbzldm" value={{default_data['cbzldm']}}>
            </label>
            <label for="zwcbm">
              <span>船舶中文名称: </span>
			  <input type="text" id="zwcbm" name="zwcbm" value={{default_data['zwcbm']}}>
              <!--select id="cllxdm" name="cllxdm">
                <option value="41" selected>货车</option>
              </select-->
            </label>
            <label for="ywcbm">
              <span>船舶英文名称: </span>
              <input type="text" id="ywcbm" name="ywcbm" value={{default_data['ywcbm']}}>
            </label>
          </p>
          <p>
            <label for="imo">
              <span>IMO号: </span>
              <input type="text" id="imo" name="imo" value={{default_data['imo']}}>
              <!--select id="tw" name="tw">
                <option value="l" selected>左</option>
                <option value="r">右</option>
              </select-->
            </label>
            <label for="gjhh">
              <span>国际呼号: </span>
              <input type="text" id="gjhh" name="gjhh" value={{default_data['gjhh']}}>
            </label>
            <label for="gjdqdm">
              <span>国籍地区代码: </span>
              <input type="text" id="gjdqdm" name="gjdqdm" value={{default_data['gjdqdm']}}>
            </label>
          </p>
          <p>
            <label for="cybgbs">
              <span>船员变更标识: </span>
              <input type="text" id="cybgbs" name="cybgbs" value={{default_data['cybgbs']}}>
            </label>
            <label for="zdgzbs">
              <span>重点关注标识: </span>
              <input type="text" id="zdgzbs" name="zdgzbs" value={{default_data['zdgzbs']}}>
            </label>
            <label for="dqjcfl">
              <span>当前检查分类: </span>
              <!--input type="text" id="dqjcfl" name="dqjcfl" /-->
			  <select id="dqjcfl" name="dqjcfl">
                <option value="入境">入境</option>
                <option value="出境">出境</option>
				        <option value="入港">入港</option>
                <option value="出港">出港</option>
                <option value="" selected>不更改</option>
              </select>
            </label>
          </p>
          <p>
            <label for="dqjczt">
              <span>当前检查状态: </span>
              <!--input type="text" id="ksys" name="ksys" /-->
			        <select id="dqjczt" name="dqjczt">
              <option value="1" >确报</option>
              <option value="2">预检正常</option>
				      <option value="3">预检异常</option>
              <option value="5">正检正常</option>
				      <option value="6">正检异常</option>
				      <option value="8">检查结束</option>
				      <option value="9">归档</option>
              <option value="" selected>不更改</option>
              </select>
            </label>
            <label for="kadm">
              <span>口岸代码: </span>
              <input type="text" id="kadm" name="kadm" value={{default_data['kadm']}}>
            </label>
            <label for="czy">
              <span>操作员: </span>
              <input type="text" id="czy" name="czy" value={{default_data['czy']}}>
            </label>
          </p>
          <p>
            <label for="czsj">
              <span>操作时间: </span>
              <input type="text" id="czsj" name="czsj" value={{default_data['czsj']}}>
            </label>
            <label for="cjg">
              <span>船籍港: </span>
              <input type="text" id="cjg" name="cjg" value={{default_data['cjg']}}>
            </label>
            <label for="dqtkmt">
              <span>当前停靠地(码头): </span>
              <input type="text" id="dqtkmt" name="dqtkmt" value={{default_data['dqtkmt']}}>
            </label>
          </p>
          <p>
            <label for="dqtkbw">
              <span>当前停靠地(泊位): </span>
              <input type="text" id="dqtkbw" name="dqtkbw" value={{default_data['dqtkbw']}}>
            </label>
            <label for="jdxgzt">
              <span>解档修改状态: </span>
              <input type="text" id="jdxgzt" name="jdxgzt" value={{default_data['jdxgzt']}}>
            </label>
            <label for="jfr">
              <span>加封人: </span>
              <input type="text" id="jfr" name="jfr" value={{default_data['jfr']}}>
            </label>
		      </p>
		      <p>
            <label for="jfsj">
              <span>加封时间: </span>
              <input type="text" id="jfsj" name="jfsj" value={{default_data['jfsj']}}>
            </label>
			      <label for="qfr">
              <span>启封人: </span>
              <input type="text" id="qfr" name="qfr" value={{default_data['qfr']}}>
            </label>
			      <label for="qfsj">
              <span>启封时间: </span>
              <input type="text" id="qfsj" name="qfsj" value={{default_data['qfsj']}}>
            </label>
          </p>
		      <p>
            <label for="wqdy">
              <span>武器弹药: </span>
              <input type="text" id="wqdy" name="wqdy" value={{default_data['wqdy']}}>
            </label>
			      <label for="jfkadm">
              <span>加封口岸: </span>
              <input type="text" id="jfkadm" name="jfkadm" value={{default_data['jfkadm']}}>
            </label>
			      <label for="qfkadm">
              <span>启封口岸: </span>
              <input type="text" id="qfkadm" name="qfkadm" value={{default_data['qfkadm']}}>
            </label>
          </p>
		      <p>
            <label for="yjbz">
              <span>优检标志: </span>
              <input type="text" id="yjbz" name="yjbz" value={{default_data['yjbz']}}>
            </label>
			      <label for="status">
              <span>船舶状态: </span>
              <input type="text" id="status" name="status" value={{default_data['status']}}>
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
