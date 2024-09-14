#!C:/Users/thanu/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import header
header.hdr()
import cgi,cgitb,pymysql
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root", password="",database="scampus")
cur = conn.cursor()

f=cgi.FieldStorage()

id=f.getvalue("id")
fid=f.getvalue("fid")
aid=f.getvalue("aid")

sql = """select * from faculty where id=%s"""%(id)
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
			padding:15px;
			font-weight:bold;
			font-size:12pt;
		}
		td
		{
			padding:15px;
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
               <a class="nav-link" href="faculty_home.py?id=%s"><span>Faculty</span></a></li>
           </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Course</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="fac_view_course.py?id=%s"><span>Course Details</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Leave</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="fac_apply_leave.py?id=%s"><span>Apply</span></a></li>
                  <li><a class="dropdown-item" href="fac_leave_status.py?id=%s"><span>Status</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Students</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="fac_view_stud.py?id=%s"><span>Student Details</span></a></li>
                  <li><a class="dropdown-item" href="fac_stud_leave.py?id=%s"><span>Leave Request</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Assignments</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="fac_add_assign.py?id=%s"><span>Add</span></a></li>
                 <li><a class="dropdown-item" href="fac_view_assign.py?id=%s"><span>View</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
               <a class="nav-link" href="fac_view_ance.py?id=%s"><span>Announcements</span></a></li>
           </li>
           <li class="nav-item">
               <a class="nav-link" href="index.html"><span>Logout</span></a></li>
           </li>
      </ul>
    </div>
  </div>
</nav>
"""%(id,id,id,id,id,id,id,id,id))
print("""<!-- <Content starts here......> -->


<center>
<h1>Assignment Details</h1>
<div class="container">
<table border=2>
<tr>
<th> S.No. </th>
<th> Assignment Id </th>
<th> Student Id </th>
<th> Student Name </th>
<th> View</th>
</tr>""")

sql1 = """select * from student_assign where faculty_id='%s' and assign_id='%s'"""%(fid,aid)
cur.execute(sql1)
r1=cur.fetchall()

cnt=0
for i in r1:
	sql2 = """select * from student where roll_no='%s'"""%(i[3])
	cur.execute(sql2)
	r2=cur.fetchone()
	cnt=cnt+1
	print("""
	<tr>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
		<td>%s</td>
		<td><a href='files/%s' target='_blank' title='Assignment'>View Assignment</a></td>
		
		</tr>
	"""%(cnt,i[2],i[3],r2[2],i[4]))
print("""</table>
</center>
</div>
</div><br><br>
<!-- < Content ends here......> -->

</body>
</html>""")
