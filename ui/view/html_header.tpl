<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>数据库管理系统</title>
  <!--link rel="stylesheet" type="text/css" href="/static/view/bsfiles/css/bootstrap.min.css"-->
  <link rel="stylesheet" type="text/css" href="/static/view/style.css">
  <link rel="stylesheet" type="text/css" href="/static/view/jquery-ui.css">
  <script type="text/javascript" src="/static/js/checkboxtree-0.5.2/library/jquery-1.4.4.js"></script>
  <script type="text/javascript" src="/static/js/jquery-1.11.3.min.js"></script>
  <script type="text/javascript" src="/static/js/checkboxtree-0.5.2/library/jquery-ui-1.8.12.custom/js/jquery-ui-1.8.12.custom.min.js"></script>
  <script type="text/javascript" src="/static/js/checkboxtree-0.5.2/jquery.checkboxtree.js"></script>
  <script src="/static/view/bsfiles/js/bootstrap.min.js"></script>
  <script src="/static/view/bsfiles/js/bootstrap.js"></script>
  <script type="text/javascript">
    $( "#startdate" ).datepicker();
    $( "#enddate" ).datepicker();
    menu_status = new Array();
    function showHide(theid){
      if (document.getElementById){
      var switch_id = document.getElementById(theid);

          if(menu_status[theid] != 'show') {
             switch_id.className = 'show';
             menu_status[theid] = 'show';
          }else{
             switch_id.className = 'hide';
             menu_status[theid] = 'hide';
          }
      }
    }

    function keepShowHide() {
        if (document.getElementById){
          var switch_id = document.getElementById("query_items");
          switch_id.className = menu_status["query_items"];
          alert(menu_status["query_items"]);
          var switch_id = document.getElementById("setting_items");
          switch_id.className = menu_status["setting_items"];
        }
    }

    //$(function() {
      
      $( "#start" ).datepicker();
      $( "#end" ).datepicker();
    //});
  </script>
</head>
