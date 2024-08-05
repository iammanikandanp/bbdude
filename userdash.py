#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="bb_dude")
cur = con.cursor()
f = cgi.FieldStorage()
uid =f.getvalue("id")
h="""select uname,img from register where id='%s'"""%(uid)
cur.execute(h)
bb=cur.fetchone()
img=bb[1]
uname=bb[0]
v1 = """select count(cid) from useraddcart where cid= '%s' """ % (uid)
cur.execute(v1)
hot = cur.fetchone()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BB Dude</title>
    <link rel="stylesheet" href="./css/bootstrap.css">
    <link rel="stylesheet" href="style/style.css">
     <style>
        @media screen and (min-width:400px) {

        #cart{
            width: 250px;
            height: 420px;
            border: 1px solid black;
            border-radius: 15px;
            margin-left: 10px;
            margin-top: 10px;
            cursor: pointer;
            overflow: hidden;
        }
         .cards > img{
            width: 200px;
            height: 200px;
        }
        
    }
    
        @media screen and (max-width:400px) {
            #cart{
            width: 100%;
            height: 420px;
            border: 1px solid black;
            border-radius: 15px;
            margin-left: 10px;
            margin-top: 10px;
            cursor: pointer;
            overflow: hidden;
        }
        .cards > img{
            width: 300px;
            height: 200px;
        }
        
        }
        #cart > p{
            font-size: 12px;
            color: gray;
        }
        .cards{
            display: flex;
            justify-content: center;
            padding-top: 7px;
        }
        
        .kj{
            display: flex;
            justify-content: center;
            padding-top: 6px;

        }
         .alerts{
            width: 300px;
            height: 50px;
            background-color: black;
            color: white;
            border-radius: 15px;
            display: flex;
            justify-content: center;
            align-items: center;
            position: absolute;
            top: 70%;
            left: 40%;
            z-index:1;
        }
        .k{
            display: none;
        }
        .o{
            color: gold;
        }
        .o:hover{
            color: red;
        }
         #badges{
            width: fit-content;
            height: fit-content;
           
        }
       #menus{
            position: absolute;
            opacity: 1;
            z-index:1;
            
          }
           #foter{
           width: 100%;
           height: 400px;
           background-color: lightgray;
           margin-top: 50px;       
           padding: 30px;
        }
         
     .bull{
        list-style-type: none;
        padding-top: 50px;
    }
    .bull> li{
        padding-top: 2rem;
    }
    .infos{
        filter: grayscale(100%);
        margin-left: 7px;
        margin-top:5px;
    }
    .infos:hover{
        filter: grayscale(0%);
        animation: infos 1s linear ;
    }
    @keyframes infos {
       form{
        transform: rotateX(70deg) rotateY(45deg) rotateZ(50deg);
       }
       to{
        transform: rotateX(360deg) rotateY(360deg)  rotateZ(360deg);
       }
       0%{
        filter: grayscale(75%);
       }
       50%{
        filter: grayscale(50%);
       }
       100%{
        filter: grayscale(0%);
       }      
    }
    .CopyRights{
        background-color: lightgray;
        text-align: center;
        color: black;
        padding-bottom: 15px;
    }
    
    </style>
    </head>
""")

print("""


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
        <div class="searchbar"><a href="#"><input type="search" placeholder="Search..." class="inputs">
                <button class="btn btn-danger btns"><i class="glyphicon glyphicon-search"></i></button></a>
        </div>
        <div><a href="#"><i class="glyphicon glyphicon-home"></i> Home</a></div>
        <div><a href="setting.py?id=%s"><i class="glyphicon glyphicon-user"></i> Account</a></div>
        <div align="center" style="padding-top: 3px;"><a href=""><i class="glyphicon glyphicon-adjust"></i> </a></div>
        <div align="center" style="padding-top: 3px;"><a href="dashfood.py?id=%s">
         <span id="badges" class="badge badge-info">%s</span>
        <i class="glyphicon glyphicon-shopping-cart"></i>
        </a></div>
        
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
            <i class="glyphicon glyphicon-search " data-toggle="collapse" data-target="#searchbarmin" style="padding-top: 7px;"></i>
        </div>
        <div>
            <a href="#"><i class="glyphicon glyphicon-home" style="padding-top: 7px;"></i></a>&nbsp;&nbsp;       
             <a href="login.py"><i class="glyphicon glyphicon-user login-min" style="padding-top: 7px;"></i></a> &nbsp;&nbsp;
            <a href="dashfood.py?id=%s"><i class="glyphicon glyphicon-shopping-cart" style="padding-top: 7px;"></i>
            <span id="badges" class="badge badge-info">%s</span></a>
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
                    <a href="editprofile.py?id=%s">
                        <img src="media/%s" alt="userprofile" name="profile"  class="img-circle" width="50px"
                            height="50px" name="pics">
                            </a>
                    </div>
                    <div class="col-md-8 col-xs-6" >
                        <h3 name="uname">%s</h3>
                    </div>
                </div>
        <ul>
            <li><a href="">Sweets</a></li>
            <li><a href="">Mixture</a></li>
            <li><a href="">Chocolates</a></li>
            <li><a href="setting.py?id=%s">My Account</a></li>
            <li><a href="blog.py?id=%s">Blogs</a></li>
            <li><a href="">About us</a></li>
            <li><a href="" data-toggle="modal"
                data-target="#mymodal">Contact us</a></li>           
        </ul>
    </div>

    <div class="internet">
        <p class="ps" id="online"><i class="glyphicon glyphicon-ok"></i> You are Online</p>
        <p class="ps" id="offline"><i class="glyphicon glyphicon-ban-circle"></i> No Internet</p>
    </div>
    <script>
        let online = document.getElementById("online");
        let offline = document.getElementById("offline");
        window.addEventListener("online", function () {
            online.style.display = "block";
            setTimeout(()=>{
                online.style.display = "none";
            },3000);
        });
        window.addEventListener("offline", function () {
            offline.style.display = "block";
            setTimeout(()=>{
                offline.style.display = "none";
            },3000);
        });
        
         function kk(){
            var d= document.querySelector(".k")
            d.style.display="block"
            setTimeout(() => {
                d.style.display="none"
            },5000)
        }
        var badgess= document.getElementById("badges");
        var badgeValue=badgess.textContent;
        if (badgeValue == 0 ){
            badgess.style.display="none"      
        }else{
            badgess.style.display="block"
        }
      

    </script>

    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
    <div class="modal fade" id="mymodal">
    <div class="modal-dialog modal-sm">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" >&times;</button>
                <h4 class="modal-title">Contact Us</h4>
            </div>
            <div class="modal-body">
                <ul style="list-style-type: none;">
                    <li style="margin: 5px;"><a href=""><img src="./image/wa.jpg" alt="" class="img-circle" width="40px" height="40px">
                    <span>6382223981</span></a></li>
                    <li style="margin: 5px;"><a href=""><img src="./image/insta.jpg" alt="" class="img-circle" width="40px" height="40px">
                        <span>solitariness_king</span>
                    </a></li>
                    <li style="margin: 5px;"><a href=""><img src="./image/fb.jpg" alt="" class="img-circle" width="40px" height="40px">
                    <span>BB Dude sweets</span></a></li>
                    <li style="margin: 5px;"><a href=""><img src="./image/x.jpg" alt="" class="img-circle" width="40px" height="40px">
                    <span>@BB Dude sweets</span></a></li>
                </ul>
            </div>
            
        </div>
    </div>
</div>
     <div class="container divs">

        <div>
            <a href="">
                <img src="./image/rasakula.jpg" alt="illai"  class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/lolipop donut.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/walfuls.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/gift.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/sweet murukku.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/cupcake.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/cakes.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/col donus.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/badham mlik.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/brownies.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/seeda.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>
        <div>
            <a href="">
                <img src="./image/miture2.jpg" alt="illai" class="img-circle act" width="150px" height="150px">
            </a>
        </div>

       </div>
        <div class="k">
    <div class="alerts">
        <p>Item Added &nbsp; &nbsp;  <span><a href="dashfood.py?id=%s" class="o"> Go to Cart</a></span></p>
    </div>
    </div>
         <div class="container ">

"""%(uid,uid,hot[0],uid,hot[0],uid,img,uname,uid,uid,uid))

ll="""select img,pctname,shortnote,actualamt,disamt,id  from sweets"""
cur.execute(ll)
u=cur.fetchall()
for i in u:
    print("""
    <div class="col-md-3 col-sm-6 col-xs-12" id="cart">
        <div class="cards"> <img src="media/%s" alt="" >
        </div><hr>
         <h3>%s</h3>
         <p>%s</p>
         <h5><del>Rs.%s</del>&nbsp;&nbsp;&nbsp;<b>Rs.%s</b></h5>
         <div class="kj">
         <a href="addcartprocess.py?id=%s&fid=%s&img=%s&pct=%s&sht=%s&act=%s&dis=%s">
         <button class="btn btn-danger btn-lg" onclick="kk()" >ADD CART</button>
         </a>
     </div>
     </div>
    """%(i[0],i[1],i[2],i[3],i[4],uid,i[5],i[0],i[1],i[2],i[3],i[4]))

print("""
</div>
 
        <div id="foter" class="container-fulid ">
        <div class="col-md-3 col-sm-3 col-xs-12">
            <img src="./image/bb logo.png" alt="" width="200px" height="200px" class="img-circle uu">
            <h2>Big Bite Dude</h2>
            <p>Your BB Dude is now delivering sweets and snacks across India!</p>
        </div>
        <div class="col-md-3 col-sm-3 col-xs-12">
            <ul class="bull" >
                <li><a href="">Home</a></li>
                <li><a href="">About Us</a></li>
                <li><a href="blog.py?id=%s">Blogs</a></li>
                <li><a href="">Track your Order</a></li>
                <li><a href=""data-toggle="modal"
                data-target="#mymodal">Contact Us</a></li>
            </ul>
        </div >
        <div class="col-md-3 col-sm-3 col-xs-12">
            <ul class="bull">
                <li><a href="">Privacy policy</a></li>
                <li><a href="">Shipping Policy</a></li>
                <li><a href="">Trems of Use</a></li>
                <li><a href="">Cancellation</a></li>
                <li><a href="">Refund Policy</a></li>
            </ul>
        </div>
        <div class="col-md-3 bull col-sm-3 col-xs-12">
            <h2>GET TO CONNECT</h2>
            <img src="./image/fb.jpg" alt="" width="50px" height="50px" class="infos img-circle">
            <img src="./image/wa.jpg" alt="" width="50px" height="50px" class="infos img-circle">
            <img src="./image/insta.jpg" alt="" width="50px" height="50px" class="infos img-circle">
            <img src="./image/x.jpg" alt="" width="50px" height="50px" class="infos img-circle">
        </div>
    </div>
    

        <div class="CopyRights col-md-12 col-sm-12 col-xs-12">
            <h4>CopyRights <i class="glyphicon glyphicon-copyright-mark"></i>2024 Big Bite Dude. All rights reserved.</h4>
            <p>Powered by <span class="text-danger"> Weone Digital</span></p>
        </div>
        

    """%(uid))