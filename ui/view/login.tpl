<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>数据库管理系统</title>
  <link rel="stylesheet" type="text/css" href="/static/view/bsfiles/css/bootstrap.min.css">
  <link rel="stylesheet" type="text/css" href="/static/view/style.css">
</head>
<body unresolved>
  <div class="login-container">
    <div class="row">
      <!--div class="col-2"></div-->
      <!--div class="col-12" id="login-header"><h2>上海边境数据库管理系统</h2></div-->
      <!--div class="col-2"></div-->
      <img id="logo-img" src="/static/view/images/bj-logo.png" alt="logo" />
    </div>
    <div class="row">
      <!--div class="col-4"></div-->
      <div class="col-12" id="login-form">
        <form class="form-signin" action="/login" method="POST">
          <input type="text" name="username" class="form-control" placeholder="账号" required autofocus>
          <input type="password" name="password" class="form-control" placeholder="密码" autofocus>
          <br/>
          <button class="btn btn-lg btn-primary btn-block" id="login-but" type="submit">
            登录
          </button>
        </form>
      </div>
      <!--div class="col-4"></div-->
      <br/><br/><br/>
    </div>
  </div>
  <script type="text/javascript">
  </script>
</body>
</html>
