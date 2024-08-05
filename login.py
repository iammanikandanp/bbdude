#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql,cgi,cgitb
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="bb_dude")
cur=con.cursor()
print(""" <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="./css/bootstrap.css">
    <link rel="stylesheet" href="style/loginstyle.css">
</head>

<body>

    <!-- navbar -->
    <div class="navbars">
        <div class="logo">
            <div class="menu"><a href="#"><i class="glyphicon glyphicon-menu-hamburger" data-toggle="collapse"
                        data-target="#menus"></i></a>
                <a href="">
                    <img src="./image/bb logo.png" alt="illai" class="img-circle" width="40px" height="40px">
                    <span><b>Big Bite Dude</b></span>

                </a>
            </div>
        </div>
        <div class="searchbar"><a href=""><input type="search" placeholder="Search..." class="inputs">
                <button class="btn btn-danger btns"><i class="glyphicon glyphicon-search"></i></button>
        </div>
        <div><a href="main.py"><i class="glyphicon glyphicon-home" style="padding-top: 7px;"></i> Home</a></div>
        <div><a href="#"><i class="glyphicon glyphicon-user " style="padding-top: 7px;"></i> Login</a></div>
        <div><a href=""><i class="glyphicon glyphicon-shopping-cart" style="padding-top: 7px;"></i></a></div>
    </div>

    <!-- navbar small screen -->
    <div class="navbars-min">
        <div class="logo-min">
            <div class="menu-min"><a href="#"><i class="glyphicon glyphicon-menu-hamburger" data-toggle="collapse"
                        data-target="#menus"></i></a>
                <a href="">
                    <img src="./image/bb logo.png" alt="illai" class="img-circle" width="40px" height="40px">
                    <span class="min-name"><b>BB Dude</b></span>
                </a>
            </div>
        </div>
        <div>
            <i class="glyphicon glyphicon-search" data-toggle="collapse" data-target="#searchbarmin"
                style="padding-top: 7px;"></i>
        </div>
        <div>
            <a href="dashboard.py?id=%s"><i class="glyphicon glyphicon-home" style="padding-top: 7px;"></i></a>&nbsp;&nbsp;       
             <a href="login.py"><i class="glyphicon glyphicon-user login-min" style="padding-top: 7px;"></i></a> &nbsp;&nbsp;
            <a href=""><i class="glyphicon glyphicon-shopping-cart" style="padding-top: 7px;"></i></a>
        </div>
    </div>
    <div id="searchbarmin" class="collapse">
        <div><a href=""><input type="search" placeholder="Search...">
                <button class="btn btn-danger">
                    <i class="glyphicon glyphicon-search"></i>
                </button>
            </a>
        </div>
    </div>
    <div id="menus" class="collapse col-md-4 col-sm-6 col-xs-6">
        <ul>
           <li><a href="">Sweets</a></li>
            <li><a href="">Mixture</a></li>
            <li><a href="">Chocolates</a></li>
            <li><a href="">Setting</a></li>
            <li><a href="">Blogs</a></li>
            <li><a href="">About us</a></li>
            <li><a href="">Contact us</a></li> 
        </ul>
    </div>
    <!-- loginpage max -->
    <div class="container-fulid max-lp min-lp">
        <div class="row">
            <div class="col-md-6 imgs">
                <img src="./image/bb logo.png" alt="logo" class="img-circle" width="550px" height="550px">
            </div>
            <div class="col-md-6 loginpage">
                <form enctype="multipart/form-data" method="post">
                    <h1 class="text-danger">Login</h1>
                    <hr>
                    <div class="form-group">
                        <label for="exampleInputEmail1">Email/Username</label>
                        <input type="text" class="form-control tables" name="email" placeholder="Email/Username">
                        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone
                            else.</small>
                    </div>
                    <div class="form-group">
                        <label for="exampleInputPassword1">Password</label>
                        <input type="password" class="form-control tables" name="pwd" placeholder="Password">
                    </div>
                    <div class="form-group">
                        <label  for="exampleCheck1">You Haven't Account <a href="signin.py" class="here">Signin</a></label>
                    </div>
                    <button type="submit" name="sub" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
    </div>

    <div class="internet">
        <p id="online"><i class="glyphicon glyphicon-ok"></i> You are Online</p>
        <p id="offline"><i class="glyphicon glyphicon-ban-circle"></i> No Internet</p>
    </div>
    <script>
        let online = document.getElementById("online");
        let offline = document.getElementById("offline");
        window.addEventListener("online", function () {
            online.style.display = "block";
            setTimeout(() => {
                online.style.display = "none";
            }, 3000);
        });
        window.addEventListener("offline", function () {
            offline.style.display = "block";
            setTimeout(() => {
                offline.style.display = "none";
            }, 3000);
        });
    </script>

    <script src="./script.js"></script>
    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>

</body>

</html> 
""")
p=cgi.FieldStorage()
user=p.getvalue("email")
password=p.getvalue("pwd")
submit=p.getvalue("sub")
if submit!=None:
    b="""select id from register where (email="%s" and password="%s") or (uname="%s" and password="%s")   """%(user,password,user,password)
    cur.execute(b)
    rec=cur.fetchone()
    if rec != None:
        print("""<script>
        alert("jeichutom mara");
         location.href='userdash.py?id=%s'
        </script>
        """ % rec[0])
    elif submit != None:
        p = """select id from adminreg  where (email="%s" and password="%s") or (name="%s" and password="%s") """ % (user, password,user,password)
        cur.execute(p)
        rec = cur.fetchone()
        if rec != None:
            print("""<script>
                alert("jeichutom mara");
                location.href='admindash.py?id=%s'
                </script>
                """ % rec[0])
        else:
            print("""<script>
                       alert("thothutom mara");
                       </script>
                       """)

