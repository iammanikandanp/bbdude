#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="bb_dude")
cur = con.cursor()
f = cgi.FieldStorage()
uid =f.getvalue("id")
fid=f.getvalue("fid")
o="""select fid from useraddcart where id='%s' and fid='%s'"""%(uid,fid)
cur.execute(o)
hot=cur.fetchone()
if hot ==None:
    o="""select qty,disamt,total from useraddcart where  cid='%s' and fid='%s' """%(uid,fid)
    cur.execute(o)
    pp=cur.fetchone()
    count=pp[0]+1
    discount=pp[1]
    price=pp[2]
    total=price+discount
    s="""update useraddcart set qty='%s' , total='%s' where  cid='%s' and fid='%s' """%(count,total,uid,fid)
    cur.execute(s)
    con.commit()
    print("""<script>
           location.href="dashfood.py?id=%s"
           </script>
           """ % (uid))