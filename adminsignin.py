#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb, smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="bb_dude")
cur = con.cursor()
print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Signin</title>
    <link rel="stylesheet" href="./css/bootstrap.css">
    <link rel="stylesheet" href="style/sginin.css">
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
        <div><a href="dashboard.py"><i class="glyphicon glyphicon-home" style="padding-top: 7px;"></i> Home</a></div>     
        <div><a href="login.py"><i class="glyphicon glyphicon-user" style="padding-top: 7px;" ></i>Logout</a></div>
        <div><a href=""><i class="glyphicon glyphicon-shopping-cart" style="padding-top: 7px;"></i></a></div>
    </div>

    <!-- navbar small screen -->
    <div class="navbars-min">
        <div class="logo-min">
            <div class="menu-min"><a href="#"><i class="glyphicon glyphicon-menu-hamburger" data-toggle="collapse"
                        data-target="#menus"></i></a>
                <a href="">
                    <img src="./image/bb logo.png" alt="illai" class="img-circle " width="40px" height="40px">
                    <span class="min-name"><b>BB Dude</b></span>
                </a>
            </div>
        </div>
        <div>
            <i class="glyphicon glyphicon-search " data-toggle="collapse" data-target="#searchbarmin"  style="margin-top: 7px;"></i>
        </div>
         <div>
            <a href="dashboard.py"><i class="glyphicon glyphicon-home" style="padding-top: 7px;"></i></a>&nbsp;&nbsp;       
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
            <div class="col-md-6 imgss" >
                <img src="./image/bb logo.png" alt="logo" class="img-circle " width="600px" height="600px">
            </div>
            <div class="col-md-6 col-xs-12 loginpage ">
                <form enctype="multipart/form-data" method="post">
                    <h1 class="texts">Admin SignIn</h1>
                    <hr>

                    <div class="form-group">
                        <label for="inputAddress">UserName</label>
                        <input type="text" class="form-control" id="UserName" placeholder="UserName" name="uname"
                            required>
                    </div>
                    <div class="form-group ">
                        <label for="inputEmail4">Email</label>
                        <input type="email" class="form-control" id="inputEmail4" placeholder="exampla@gmail.com"
                            name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="inputPassword4">Password</label>
                        <input type="password" class="form-control" id="inputPassword4" placeholder="Ex- $M@n!k@ND&n"
                            name="pwd" required>
                    </div>
                   

                    <div class="form-group">
                        <label for="inputAddress2">Address</label>
                        <input type="text" class="form-control" id="inputAddress2"
                            placeholder="Apartment, studio, or floor" name="address">
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="inputCity">City</label>
                            <input type="text" class="form-control" id="inputCity" placeholder="Example covai" name="city">
                        </div>
                       
                        <div class="form-group ">
                            <label for="inputZip">Branch code</label>
                            <input type="text" class="form-control" name="code" id="inputZip" placeholder="c001">
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="form-group">
                        <div class="form-group">
                        <label for="exampleCheck1"> You Have Already Account <a class="here" href="login.py">Login</a></label>
                    </div>
                    </div>
                    <button type="submit" name="sub" class="btn btn-primary btn-lg">Sign in</button>
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

p = cgi.FieldStorage()
username = p.getvalue("uname")
email = p.getvalue("email")
passwords = p.getvalue("pwd")
address = p.getvalue("address")
city = p.getvalue("city")
pincode = p.getvalue("code")
submit = p.getvalue("sub")
if submit != None:
    b = """insert into adminreg (name,email,password,address,city,branchcode,img) values ('%s','%s','%s','%s','%s','%s','bb logo.png')""" % (username, email, passwords,address, city, pincode)
    cur.execute(b)
    con.commit()
    # fromadd = "mk7094846331@gmail.com"
    # password = "qyfs bnzl fmdn zmje"
    # toadd = email
    # subject = "welcome to BB Dude"
    # body = "hello {}".format(username)
    # msg = """subject: {} \n\n{}""".format(subject, body)
    # server = smtplib.SMTP("smtp.gmail.com:587")
    # server.ehlo()
    # server.starttls()
    # server.login(fromadd, password)
    # server.sendmail(fromadd, toadd, msg)
    # server.quit()
    k="""select id from adminreg where email='%s'"""%(email)
    cur.execute(k)
    you=cur.fetchone()
    print(""" <script>
                  location.href="admindash.py?id=%s"
                  </script>"""%you[0])
con.close()







