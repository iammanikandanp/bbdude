#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="bb_dude")
cur = con.cursor()
f = cgi.FieldStorage()
uid =f.getvalue("id")
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BB DUDE BLOG</title>
    <link rel="stylesheet" href="./css/bootstrap.css">
    <style>
        .jk{
            margin-top: 10px;
        }
    .blog{
        width: 100%;
        height: 300px;
    }
    .video{
        float: right;
        margin: 7px;
    }
    .video1{
        float: left;
        margin: 7px;
    }
    </style>
</head>
""")
print("""
<body>
    <div class="jk">
    <a href="userdash.py?id=%s">
    <button class="btn btn-primary btn-lg ">Home</button></a>
</div>
        <h1 class="text-danger" style="text-align: center;">TODAY BLOGS</h1>

    <div class="container">
        <div class="col-md-12 alert alert-success blog" style="margin-top: 50px;">
       <video width="300px" height="200px" autoplay muted controls class="video">
        <source src="./image/VID_20220120_124214.mp4" type="video/mp4">
       </video>
       <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo unde obcaecati dignissimos reprehenderit repellendus aliquam, reiciendis cum accusantium voluptate nostrum sed sapiente fugit nesciunt laboriosam distinctio quia veritatis sit iusto laborum veniam nisi neque. Pariatur iste totam, culpa alias, quos quo repudiandae enim accusamus quis harum eius laudantium qui dolore saepe animi distinctio dolorem. Aperiam fugiat cumque itaque quod consequatur corporis. Deserunt recusandae doloribus aut reiciendis laboriosam autem maiores expedita animi optio qui! Eveniet, reiciendis. Accusantium sit aspernatur fugiat reiciendis, laborum ipsa error consectetur nesciunt? Nisi esse aliquid laboriosam reiciendis fuga dicta quas in, cum fugit inventore voluptatibus suscipit molestiae at eius dolore obcaecati quia ad consequatur? Tempora quasi consectetur sapiente quibusdam dignissimos velit! Odio cupiditate aut porro neque est ipsa earum voluptates harum sunt quidem pariatur rerum et inventore consectetur magni minus in, ab ea explicabo fugit blanditiis, corporis assumenda praesentium error? Nesciunt fugiat, consequuntur quidem repellendus provident, pariatur, corrupti maxime quia deleniti qui dolore adipisci! In rem expedita nemo nisi inventore neque maxime, porro ex sequi temporibus, eligendi, quia error totam? Ea architecto obcaecati cupiditate iusto ullam aperiam autem, id aspernatur, blanditiis reprehenderit sed quae perferendis laboriosam veritatis tenetur perspiciatis? Quod, nobis distinctio esse minima temporibus laborum magni.</p>
        </div>
        <div class="col-md-12 alert alert-info blog">
<video width="300px" height="200px" autoplay muted controls class="video1">
        <source src="./image/VID_20220120_125311.mp4" type="video/mp4">
        </video>
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo unde obcaecati dignissimos reprehenderit repellendus aliquam, reiciendis cum accusantium voluptate nostrum sed sapiente fugit nesciunt laboriosam distinctio quia veritatis sit iusto laborum veniam nisi neque. Pariatur iste totam, culpa alias, quos quo repudiandae enim accusamus quis harum eius laudantium qui dolore saepe animi distinctio dolorem. Aperiam fugiat cumque itaque quod consequatur corporis. Deserunt recusandae doloribus aut reiciendis laboriosam autem maiores expedita animi optio qui! Eveniet, reiciendis. Accusantium sit aspernatur fugiat reiciendis, laborum ipsa error consectetur nesciunt? Nisi esse aliquid laboriosam reiciendis fuga dicta quas in, cum fugit inventore voluptatibus suscipit molestiae at eius dolore obcaecati quia ad consequatur? Tempora quasi consectetur sapiente quibusdam dignissimos velit! Odio cupiditate aut porro neque est ipsa earum voluptates harum sunt quidem pariatur rerum et inventore consectetur magni minus in, ab ea explicabo fugit blanditiis, corporis assumenda praesentium error? Nesciunt fugiat, consequuntur quidem repellendus provident, pariatur, corrupti maxime quia deleniti qui dolore adipisci! In rem expedita nemo nisi inventore neque maxime, porro ex sequi temporibus, eligendi, quia error totam? Ea architecto obcaecati cupiditate iusto ullam aperiam autem, id aspernatur, blanditiis reprehenderit sed quae perferendis laboriosam veritatis tenetur perspiciatis? Quod, nobis distinctio esse minima temporibus laborum magni.</p>
    </video>

        </div>
        <div class="col-md-12 alert alert-warning blog">
            <video width="300px" height="200px" autoplay muted controls class="video">
                <source src="./image/VID_20220120_125732.mp4" type="video/mp4">
               </video>
               <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo unde obcaecati dignissimos reprehenderit repellendus aliquam, reiciendis cum accusantium voluptate nostrum sed sapiente fugit nesciunt laboriosam distinctio quia veritatis sit iusto laborum veniam nisi neque. Pariatur iste totam, culpa alias, quos quo repudiandae enim accusamus quis harum eius laudantium qui dolore saepe animi distinctio dolorem. Aperiam fugiat cumque itaque quod consequatur corporis. Deserunt recusandae doloribus aut reiciendis laboriosam autem maiores expedita animi optio qui! Eveniet, reiciendis. Accusantium sit aspernatur fugiat reiciendis, laborum ipsa error consectetur nesciunt? Nisi esse aliquid laboriosam reiciendis fuga dicta quas in, cum fugit inventore voluptatibus suscipit molestiae at eius dolore obcaecati quia ad consequatur? Tempora quasi consectetur sapiente quibusdam dignissimos velit! Odio cupiditate aut porro neque est ipsa earum voluptates harum sunt quidem pariatur rerum et inventore consectetur magni minus in, ab ea explicabo fugit blanditiis, corporis assumenda praesentium error? Nesciunt fugiat, consequuntur quidem repellendus provident, pariatur, corrupti maxime quia deleniti qui dolore adipisci! In rem expedita nemo nisi inventore neque maxime, porro ex sequi temporibus, eligendi, quia error totam? Ea architecto obcaecati cupiditate iusto ullam aperiam autem, id aspernatur, blanditiis reprehenderit sed quae perferendis laboriosam veritatis tenetur perspiciatis? Quod, nobis distinctio esse minima temporibus laborum magni.</p>

        </div>
        <div class="col-md-12 alert alert-danger blog">
            <video width="300px" height="200px" autoplay muted controls class="video1">
                <source src="./image/VID_20220120_132146.mp4" type="video/mp4">
               </video>
               <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo unde obcaecati dignissimos reprehenderit repellendus aliquam, reiciendis cum accusantium voluptate nostrum sed sapiente fugit nesciunt laboriosam distinctio quia veritatis sit iusto laborum veniam nisi neque. Pariatur iste totam, culpa alias, quos quo repudiandae enim accusamus quis harum eius laudantium qui dolore saepe animi distinctio dolorem. Aperiam fugiat cumque itaque quod consequatur corporis. Deserunt recusandae doloribus aut reiciendis laboriosam autem maiores expedita animi optio qui! Eveniet, reiciendis. Accusantium sit aspernatur fugiat reiciendis, laborum ipsa error consectetur nesciunt? Nisi esse aliquid laboriosam reiciendis fuga dicta quas in, cum fugit inventore voluptatibus suscipit molestiae at eius dolore obcaecati quia ad consequatur? Tempora quasi consectetur sapiente quibusdam dignissimos velit! Odio cupiditate aut porro neque est ipsa earum voluptates harum sunt quidem pariatur rerum et inventore consectetur magni minus in, ab ea explicabo fugit blanditiis, corporis assumenda praesentium error? Nesciunt fugiat, consequuntur quidem repellendus provident, pariatur, corrupti maxime quia deleniti qui dolore adipisci! In rem expedita nemo nisi inventore neque maxime, porro ex sequi temporibus, eligendi, quia error totam? Ea architecto obcaecati cupiditate iusto ullam aperiam autem, id aspernatur, blanditiis reprehenderit sed quae perferendis laboriosam veritatis tenetur perspiciatis? Quod, nobis distinctio esse minima temporibus laborum magni.</p>

        </div>
        <div class="col-md-12 alert alert-success blog">
            <video width="300px" height="200px" autoplay muted controls class="video">
                <source src="./image/VID_20220120_132243.mp4" type="video/mp4">
               </video>
               <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo unde obcaecati dignissimos reprehenderit repellendus aliquam, reiciendis cum accusantium voluptate nostrum sed sapiente fugit nesciunt laboriosam distinctio quia veritatis sit iusto laborum veniam nisi neque. Pariatur iste totam, culpa alias, quos quo repudiandae enim accusamus quis harum eius laudantium qui dolore saepe animi distinctio dolorem. Aperiam fugiat cumque itaque quod consequatur corporis. Deserunt recusandae doloribus aut reiciendis laboriosam autem maiores expedita animi optio qui! Eveniet, reiciendis. Accusantium sit aspernatur fugiat reiciendis, laborum ipsa error consectetur nesciunt? Nisi esse aliquid laboriosam reiciendis fuga dicta quas in, cum fugit inventore voluptatibus suscipit molestiae at eius dolore obcaecati quia ad consequatur? Tempora quasi consectetur sapiente quibusdam dignissimos velit! Odio cupiditate aut porro neque est ipsa earum voluptates harum sunt quidem pariatur rerum et inventore consectetur magni minus in, ab ea explicabo fugit blanditiis, corporis assumenda praesentium error? Nesciunt fugiat, consequuntur quidem repellendus provident, pariatur, corrupti maxime quia deleniti qui dolore adipisci! In rem expedita nemo nisi inventore neque maxime, porro ex sequi temporibus, eligendi, quia error totam? Ea architecto obcaecati cupiditate iusto ullam aperiam autem, id aspernatur, blanditiis reprehenderit sed quae perferendis laboriosam veritatis tenetur perspiciatis? Quod, nobis distinctio esse minima temporibus laborum magni.</p>

        </div>
   </div>
   


           
    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
</body>
</html>
"""%(uid))