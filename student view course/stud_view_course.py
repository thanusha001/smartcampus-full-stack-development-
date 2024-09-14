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
sql = """select * from student where id=%s"""%(id)
cur.execute(sql)
r=cur.fetchone()

print("""<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.2/font/bootstrap-icons.min.css">



   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

	<style>
		table{
			width:80%;
			background-color:#c4c4c4;
		}
		th
		{
			background-color:#0a0;
			padding:7px;
			font-weight:bold;
			font-size:12pt;
		}
		td
		{
			padding:5px;
			font-weight:bold;
			font-size:11pt;
		}
	</style>
	
</head>
<body>

    """)
print("""      <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto">
  <li class="nav-item">
               <a class="nav-link" href="student_home.py?id=%s"><span>Student</span></a>
           </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Course</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="stud_view_course.py?id=%s"><span>Course Details</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Leave</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="stud_leave.py?id=%s"><span>New Request</span></a></li>
                  <li><a class="dropdown-item" href="stud_view_leave.py?id=%s"><span>Status</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Assignments</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="stud_view_assign.py?id=%s"><span>View Assignments</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
               <a class="nav-link" href="stud_view_ance.py?id=%s"><span>Announcements</span></a></li>
           </li>
           <li class="nav-item">
               <a class="nav-link" href="index.html"><span>Logout</span></a></li>
           </li>
      </ul>
    </div>
  </div>
</nav>"""%(id,id,id,id,id,id))

print("""<!-- <Content starts here......> -->


<center>
<h1>Course Details</h1>
<table border=2>
<tr>
<th> S.No. </th>
<th> Course Id </th>
<th> Course Name </th>
<th> Duration </th>
<th> Department </th>
<th> Starting Date </th>
<th> Fees </th>
<th> Apply</th>
</tr>""")
sql = """select * from course where department='%s'"""%(r[4])
cur.execute(sql)
r1=cur.fetchall()
cnt=0
for i in r1:
	sql2="""select * from course_reg where course_id='%s' and stud_id='%s'"""%(i[1],r[1])
	cur.execute(sql2)
	r2=cur.fetchone()
	if r2==None:
		st="<a href='stud_course_apply.py?cid=%s&id=%s'>Apply now..</a>"%(i[0],id)
	else:
		st="Applied"
	cnt=cnt+1
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
	</tr>
	"""%(cnt,i[1],i[2],i[3],i[4],i[5],i[6],st))
print("""</table>
</center>
</div><br><br>

<!-- < Content ends here......> -->

</body>
</html>""")
