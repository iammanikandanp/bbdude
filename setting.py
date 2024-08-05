#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="bb_dude")
cur = con.cursor()
f = cgi.FieldStorage()
uid = f.getvalue("id")
h = """select uname,img from register where id='%s'""" % (uid)
cur.execute(h)
bb = cur.fetchone()
print(
    """  <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BB Dude</title>
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="style/dash.css">
    

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
                <button class="btn btn-danger btns"><i class="glyphicon glyphicon-search"></i></button></a>
        </div>
        <div><a href=""><i class="glyphicon glyphicon-home"></i> Home</a></div>
        <div><a href=""><i class="glyphicon glyphicon-user"></i> Account</a></div>
        <div align="center" style="padding-top: 3px;"><a href=""><i class="glyphicon glyphicon-adjust"></i> </a></div>
        <div align="center" style="padding-top: 3px;"><a href=""><i class="glyphicon glyphicon-shopping-cart"></i></a></div>
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
        <div style="margin-top: 7px;">
            <i class="glyphicon glyphicon-search " data-toggle="collapse" data-target="#searchbarmin"></i>
        </div>
        <div style="margin-top: 7px;">
            <a href=""><i class="glyphicon glyphicon-home"></i></a> &nbsp;&nbsp;
            <a href=""><i class="glyphicon glyphicon-user login-min"></i></a> &nbsp;&nbsp;
            <a href=""><i class="glyphicon glyphicon-shopping-cart"></i></a>
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
     <div id="menus" class="collapse col-md-4 col-sm-6 col-xs-10">
    <div class="row">
                    <div class="col-md-2 col-xs-3" style="padding-top: 5px;">
                        <img src="media/%s" alt="userprofile" name="profile"  class="img-circle" width="50px"
                            height="50px" name="pics">
                    </div>
                    <div class="col-md-8 col-xs-6" >
                        <h3 name="uname">%s</h3>
                    </div>
                </div>
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

    <div class="container">
        <div class="row">
            <div class="orders col-md-6">
                <a href="userorder.py?id=%s">
                    <h3>Orders <span class="oders glyphicon glyphicon-menu-right "></span></h3>
                </a>
            </div>
        </div>
        <div class="row">
            <div class="orders col-md-6">
                <a href="r.html">
                    <h3>Whislist <span class="oders glyphicon glyphicon-menu-right"></span></h3>
                </a>
            </div>
        </div>
        <div class="row">
            <div class="orders col-md-6">
                <a href="editprofile.py?id=%s">
                    <h3>Edit Profile <span class="oders glyphicon glyphicon-menu-right"></span></h3>
                </a>
            </div>
        </div>
        <div class="row">
            <div class="orders col-md-6">
                <a href="r.html">
                    <h3>Coupon <span class="oders glyphicon glyphicon-menu-right"></span></h3>
                </a>
            </div>
        </div>
        <div class="row">
            <div class="orders col-md-6">
                <a href="r.html">
                    <h3>Reviews <span class="oders glyphicon glyphicon-menu-right"></span></h3>
                </a>
            </div>
        </div>
    </div>






    <!-- cards -->
    <!-- <div class="container">
        <div class="row">
            <div class="col-md-3" id="act">

            </div>
            <div class="col-md-3" id="act"></div>
            <div class="col-md-3" id="act"></div>
            <div class="col-md-3" id="act"></div>
            <div class="col-md-3" id="act"></div>
        </div>
    </div> -->

    <div class="il">
        <footer>
            <a href="main.py">
            <button id="lo" class="btn btn-primary btn-lg" onclick="g()">Log out</button>
            </a>
        </footer>
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
        
        function g(){
        alert("Are you Sure to Log out?");
        }
    </script>

    <script src="./script.js"></script>
    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>

    """%(bb[1],bb[0],uid,uid)
)