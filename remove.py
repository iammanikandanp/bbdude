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
h="""select qty  from useraddcart where cid='%s' and fid='%s' """%(uid,fid)
cur.execute(h)
hot=cur.fetchone()
if hot != None:
    u="""delete from useraddcart where cid='%s' and fid='%s' """ % (uid, fid)
    cur.execute(u)
    con.commit()
    con.close()

print(""" <script> 
        location.href="dashfood.py?id=%s&fid=%s"
        </script>
        """ % (uid, fid))