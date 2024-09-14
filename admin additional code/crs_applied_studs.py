#!C:/Users/thanu/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import header
header.hdr()

import cgi,cgitb,pymysql
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root", password="",database="scampus")
cur = conn.cursor()

f=cgi.FieldStorage()

print("""<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.2/font/bootstrap-icons.min.css">

        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"><!--it give good align-->
       


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
		 h2,h1{
                text-align:center;
            }    
            .form-control{
                border-radius: 15px;
            	border: 2px solid #e3e1e08b;
            }
	</style>
</head>
<body>


 <div >
	</div>
	<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto">
  <li class="nav-item">
               <a class="nav-link" href="admin_home.py"><span>Admin</span></a>
           </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Course</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="adm_view_course.py"><span>Course Details</span></a></li>
                 <li><a class="dropdown-item" href="adm_add_course.py"><span>Add New</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Faculty</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="adm_view_faculty.py"><span>Faculty Details</span></a></li>
                  <li><a class="dropdown-item" href="adm_view_fac_leave.py"><span>Leave Request</span></a></li>
                  <li><a class="dropdown-item" href="adm_add_faculty.py"><span>New Faculty</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Students</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="adm_view_student.py"><span>Student Details</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
               <a class="nav-link" href="announcement.py"><span>Announcements</span></a></li>
           </li>
           <li class="nav-item">
               <a class="nav-link" href="index.html"><span>Logout</span></a></li>
           </li>
      </ul>
    </div>
  </div>
</nav>
   

<!-- <Content starts here......> -->


<center>
<h1>Student Details</h1>
<table border=2>
<tr>
<th> S.No. </th>
<th> Roll No </th>
<th> Student Name </th>
<th> Degree </th>
<th> Department </th>
<th> Batch </th>
<th> Contact </th>
<th> Mail Id </th>
</tr>""")

cid=f.getvalue("cid")

sql2 = """select * from course_reg where course_id='%s'"""%(cid)
cur.execute(sql2)
r2=cur.fetchall()
cnt=0
for i in r2:
	cnt=cnt+1
	sql = """select * from student where roll_no='%s'"""%(i[2])
	cur.execute(sql)
	r=cur.fetchone()
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
	"""%(cnt,r[1],r[2],r[3],r[4],r[5],r[6],r[7]))
print("""</table>
		</center>
		</div><br><br>
		
		<!-- < Content ends here......> -->
		
		</body>
		</html>""")





