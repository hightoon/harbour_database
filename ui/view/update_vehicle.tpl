<!DOCTYPE html>
<html>
%include('./view/html_header.tpl')
<body>
  <div id="main" class="managementpage">
    %include('./view/page_head.tpl')
    <div class="row">
      % include('./view/expanding_side_nav.tpl')
      <div id="vehicle-manage-page" class="col-10">
        <h4>数据库管理 >>> 更新车辆信息</h4>
        <form action="/vehicle/{{rowid}}" method="POST">
          <p>
            <label for="wycph">
              <span>唯一车牌号: </span>
              <input type="text" id="wycph" name="wycph" value={{default_data['wycph']}}>
            </label>
            <label for="gsqc">
              <span>公司全称: </span>
              <input type="text" id="gsqc" name="gsqc" value={{default_data['gsqc']}}>
            </label>
          </p>
          <p>
            <label for="jwcph">
              <span>境外车牌号: </span>
              <input type="text" id="jwcph" name="jwcph" value={{default_data['jwcph']}}>
            </label>
            <label for="jncph">
              <span>境内车牌号: </span>
              <input type="text" id="jncph" name="jncph" value={{default_data['jncph']}}>
            </label>
          </p>
          <p>
            <label for="ssgjdm">
              <span>所属国籍: </span>
              <input type="text" id="ssgjdm" name="ssgjdm" value={{default_data['ssgjdm']}}>
            </label>
            <label for="cllxdm">
              <span>车辆类型代码: </span>
              <select id="cllxdm" name="cllxdm">
                <option value="41">货车</option>
                <option value="42">客车</option>
                <option value="43">小车</option>
                <option value="49">其他</option>
                <option value="" selected>不修改</option>
              </select>
            </label>
            <label for="clgd">
              <span>车辆高度: </span>
              <input type="text" id="clgd" name="clgd" value={{default_data['clgd']}}>
            </label>
          </p>
          <p>
            <label for="tw">
              <span>肽位: </span>
              <select id="tw" name="tw">
                <option value="左" >左</option>
                <option value="右">右</option>
                <option value="" selected>不修改</option>
              </select>
            </label>
            <label for="pwyxq">
              <span>批文有效期: </span>
              <input type="text" id="pwyxq" name="pwyxq" value={{default_data['pwyxq']}}>
            </label>
            <label for="txkadm">
              <span>通行口岸代码: </span>
              <input type="text" id="txkadm" name="txkadm" value={{default_data['txkadm']}}>
            </label>
          </p>
          <p>
            <label for="txyxq">
              <span>通行有效期: </span>
              <input type="text" id="txyxq" name="txyxq" value={{default_data['txyxq']}}>
            </label>
            <label for="sqbh">
              <span>申请表号: </span>
              <input type="text" id="sqbh" name="sqbh" value={{default_data['sqbh']}}>
            </label>
            <label for="pwh">
              <span>现批文号码: </span>
              <input type="text" id="pwh" name="pwh" value={{default_data['pwh']}}>
            </label>
          </p>
          <p>
            <label for="ksys">
              <span>款式颜色: </span>
              <input type="text" id="ksys" name="ksys" value={{default_data['ksys']}}>
            </label>
            <label for="ctz">
              <span>车头字: </span>
              <input type="text" id="ctz" name="ctz" value={{default_data['ctz']}}>
            </label>
            <label for="zzdw">
              <span>载重吨位: </span>
              <input type="text" id="zzdw" name="zzdw" value={{default_data['zzdw']}}>
            </label>
          </p>
          <p>
            <label for="cbdw">
              <span>内地承办单位(合营单位): </span>
              <input type="text" id="cbdw" name="cbdw" value={{default_data['cbdw']}}>
            </label>
            <label for="czy">
              <span>录入检查员代码: </span>
              <input type="text" id="czy" name="czy" value={{default_data['czy']}}>
            </label>
            <label for="czsj">
              <span>录入时间: </span>
              <input type="text" id="czsj" name="czsj" value={{default_data['czsj']}}/>
            </label>
          </p>
          <p>
            <label for="czkadm">
              <span>操作口岸代码: </span>
              <input type="text" id="czkadm" name="czkadm" value={{default_data['czkadm']}}>
            </label>
            <label for="pd">
              <span>主司机: </span>
              <input type="text" id="pd" name="pd" value={{default_data['pd']}}>
            </label>
            <label for="sd">
              <span>副司机: </span>
              <input type="text" id="sd" name="sd" value={{default_data['sd']}}>
            </label>
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
