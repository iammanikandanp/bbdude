#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="bb_dude")
cur = con.cursor()
form = cgi.FieldStorage()
uid = form.getvalue("id")
p = """select * from orderlist"""
cur.execute(p)
pri = cur.fetchall()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>table</title>
    <link rel="stylesheet" href="./css/bootstrap.css">

</head>
<body>

    <table  class="table table-hover table-bordered table-responsive">
        <tr>
            <th>id</th>
            <th>cst id</th>
            <th>food id</th>
            <th>img </th>
            <th>pctname</th>
            <th>qty</th>
            <th>per price</th>
            <th>total</th>
            <th>username</th>
            <th>address</th>
            <th>phone number</th>
            <th>payment</th>
            <th>reg time</th>
        </tr>


""")
for i in pri:
    print("""
            <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
             </tr>""" % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11],i[12]))
print("""</table>
             <script src="./js/jquery.min.js"></script>
            <script src="./js/bootstrap.min.js"></script>""")