#!C:/Users/thanu/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import header
header.hdr()

import cgi,pymysql,os
import smtplib,cgitb;cgitb.enable()

conn = pymysql.connect(host="localhost",user="root", password="",database="scampus")
cur=conn.cursor()

f=cgi.FieldStorage()
id=f.getvalue("id")
cid=f.getvalue("cid")
sql = """select * from student where id=%s"""%(id)
cur.execute(sql)
r=cur.fetchone()

sql1 = """select * from course where id=%s"""%(cid)
cur.execute(sql1)
r1=cur.fetchone()

sql2 = """insert into course_reg values('','%s','%s')"""%(r1[1],r[1])
cur.execute(sql2)
conn.commit()
print("""<script>alert('Course register successfully...');location.href='stud_view_course.py?id=%s';</script>"""%(id))
	