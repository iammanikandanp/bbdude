#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="bb_dude")
cur = con.cursor()
f = cgi.FieldStorage()
uid = f.getvalue("id")
h = """select uname,email,password,phnum,dob,gender,address,pincode,city,img from register where id='%s'""" % (uid)
cur.execute(h)
bb = cur.fetchone()
print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BB Dude</title>
    <link rel="stylesheet" href="./css/bootstrap.css">
    <link rel="stylesheet" href="style/editpro.css">
   
   

</head>

<body style="background-color: black;">
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
        <div><a href=""><input type="search" value="Search...">
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
    <div class="k">
        <div class="l">
            <img src="media/%s" alt="" class="img-circle " width="200px"
                height="200px" onclick="view()">
        </div>
        <div class="changep">
            <a href="#" class="changes">
                <h4>Change profile</h4>
            </a>
        </div>
        <div class="edit">
            <h3 class="edits" onclick="edit()">Edit Profile</h3>
        </div>
        <div class="container-fulid max-lp">
            <div class="row">
                
                <div class="col-md-6 loginpage">
                    <div ><span class="spans"><i class="back glyphicon glyphicon-remove" onclick="ret()"></i></span></div>
                    <form enctype="multipart/form-data" method="post">
                        <h1 class="text-danger">Edit Profile</h1>
                        <hr>
    
                        <div class="form-group">
                            <label for="inputAddress">UserName</label>
                            <input type="text" class="form-control" id="UserName" value="%s" name="uname"
                                required>
                        </div>
                        <div class="form-group ">
                            <label for="inputEmail4">Email</label>
                            <input type="email" class="form-control" id="inputEmail4" value="%s"
                                name="email" required>
                        </div>
                        <div class="form-group">
                            <label for="inputPassword4">Password</label>
                            <input type="password" class="form-control" id="inputPassword4" value="%s"
                                name="pwd" required>
                        </div>
                        <div class="form-group">
                            <label for="inputPassword4">Phone number</label>
                            <input type="number" class="form-control" id="dob" value="%s" name="phnum"
                                required>
                        </div>
                        <div class="form-group">
                            <label for="inputPassword4">Gender</label>
                            <input type="text" class="form-control" id="gender" value="%s"
                                name="gender" required>
                        </div>
    
                        <div class="form-group">
                            <label for="inputAddress2">Address</label>
                            <input type="text" class="form-control" id="inputAddress2" name="address"
                                value="%s">
                        </div>
                        <div class="form-row">
                            <div class="form-group">
                                <label for="inputCity">City</label>
                                <input type="text" class="form-control" id="inputCity" value="%s" name="city">
                            </div>
                            
                            <div class="form-group ">
                                <label for="inputZip">Pincode</label>
                                <input type="text" class="form-control" id="inputZip" value="%s" name="pincode">
                            </div>
                        </div>
                        
                        <button type="submit" name="upd" class="btn btn-primary btn-lg">Update</button>
                    </form>
                </div>
            </div>
        </div>

    </div>

    <div id="j"><i class="back glyphicon glyphicon-remove" onclick="back()"></i></div>
    <div id="lg-view">
        <img src="media/%s" alt="" width="300px" height="300">
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


        function view() {
            var lg = document.getElementById("lg-view")
            var small = document.querySelector(".k")
            var overlay = document.querySelector("#j")
            small.style.display = "none"
            lg.style.display = "block"
            overlay.style.display = "block"


        }
        function back() {
            var lg = document.getElementById("lg-view")
            var small = document.querySelector(".k")
            var overlay = document.querySelector("#j")
            small.style.display = "block"
            lg.style.display = "none"
            overlay.style.display = "none"

        }

        function edit(){
            var edit=document.querySelector(".loginpage")
            var edits=document.querySelector("edits")
            edit.style.display="block"
        }
        function ret(){
            var edit=document.querySelector(".loginpage")
            edit.style.display="none"

        }
    </script>

    <script src="./script.js"></script>
    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
"""%(bb[9],bb[0],bb[9],bb[0],bb[1],bb[2],bb[3],bb[5],bb[6],bb[8],bb[7],bb[9]))

name=f.getvalue("uname")
email=f.getvalue("email")
pwd=f.getvalue("pwd")
phnum=f.getvalue("phnum")
gender=f.getvalue("gender")
add=f.getvalue("address")
city=f.getvalue("city")
pin=f.getvalue("pincode")
upd=f.getvalue("upd")
if upd!=None:
    j="""update register set uname='%s' , email='%s',password='%s', gender='%s',phnum='%s',address='%s',city='%s',pincode='%s' where id='%s' """%(name,email,pwd,gender,phnum,add,city,pin,uid)
    cur.execute(j)
    con.commit()
    print("""
    <script>
    alert("update successful!");
    location.href="editprofile.py?id=%s"
    </script>
    """%(uid))
