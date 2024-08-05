#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="bb_dude")
cur = con.cursor()
p = cgi.FieldStorage()
uid=p.getvalue("id")
print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="./css/bootstrap.css">
        <link rel="stylesheet" href="style/demo.css">
    </head>
    <body>
    
        <div class="container" style="margin-top: 10px;">
        <div class="row">
            <div class="col-xs-12 cart">
                <form enctype="multipart/form-data" method="post">
                    <h1>ADD CART</h1>
                    <hr>
                    <div class="a-cart">
                        <label for="p-img">Product Image</label><br>
                        <input type="file" name="poogai"  required>
                    </div>
                    <div class="a-cart">
                        <label for="p-name">Product Name</label><br>
                        <input type="text" name="pname"  required  >
                    </div>
                    <div class="a-cart">
                        <label for="p-sn">Product discription</label><br>
                        <input type="message" name="short"  required>
                    </div>
                    <div class="a-cart">
                        <label for="p-actualamt">Product Actual Amount</label><br>
                        <input type="number" name="aamt"  required>
                    </div>
                    <div class="a-cart">
                        <label for="p-disamt">Product Discount Amount</label><br>
                        <input type="number" name="damt" required>
                    </div>
                         <div class="a-cart">
                        <label for="select">Product Type</label><br>
                        <select name="sclt" id="select" >
                            <option selected > choose...</option>
                            <option>Sweets</option>
                            <option>Chocolates</option>
                            <option>Cookies</option>
                            <option>Mixture</option>
                            <option>Donuts</option>
                            <option>Cupcakes</option>
                            <option>Shacks</option>
                            <option>Lolipop</option>
                        </select> 
                        </div> <br><br>
                    <button type="submit" name="sub" value="submit" class="btn btn-success btn-lg">ADD</button>
                    
                        

                </form>
<a href="admindash.py?id=%s">
                        <button name="cancel" class="btn btn-danger btn-lg">CANCEL</button></a>
            </div>
          </div>

            </div>
            <script src="./js/jquery.min.js"></script>
            <script src="./js/bootstrap.min.js"></script>
        </body>
        </html>
            """%(uid))
sub = p.getvalue("sub")
if sub != None:
    padam = p['poogai']
    pname = p.getvalue("pname")
    pshort = p.getvalue("short")
    aamt = p.getvalue("aamt")
    damt = p.getvalue("damt")
    select = p.getvalue("sclt")
    if padam.filename:
        fn = os.path.basename(padam.filename)
        open("media/" + fn, "wb").write(padam.file.read())
        q = """insert into sweets (img,pctname,shortnote,actualamt,disamt,type) values ('%s','%s','%s','%s','%s','%s')""" % (fn, pname, pshort, aamt, damt, select)
        cur.execute(q)
        con.commit()
        print("""
            <script>
            alert('add cart done');
            </script>""")



