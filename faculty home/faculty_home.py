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
	.login-container {

        width: 500px;
        height: 330px;

        padding: 20px;
        background-color: #f1f7f4;
        box-shadow: 0 0 10px rgba(47, 45, 45, 0.1);
        border-radius: 5px;
        opacity:0.8;
      }

      .card{
        height: 290px;
        margin-top: auto;
        margin-bottom: auto;
        width: 460px;
        background-color:rgba(216, 213, 217, 0.833) !important;
        position:center;
      }
      
      #password,#username,#rolodex,#lock{

        border-radius: 15px;
        border: 2px solid #dcdcdc8b;
      }
       #submit,#cancel{
        border-radius:15px;
      }
		td
		{
			font-weight:bold;
			font-style:italic;
			font-size:12pt;
		}
		button
		{
			padding:5px;width:200px;background-color:#33f;font-weight:bold;
			color:white;
		}
	</style>
</head>
<body>

 <div >
	</div>
    """)
print("""   
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
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
<div style="width:500px;height:400px;margin-top:50px;background-color:#aef;">
<br>
<h1>Welcome %s !!!</h1>
<div class="card">
<div class="card-body">
<table>
<tr><td>%s</td></tr>
<tr><td>%s</td></tr>
<tr><td>%s</td></tr>
<tr><td>%s</td></tr>
<tr><td>%s</td></tr>
<tr><td>%s</td></tr>
<tr><td><button onmouseover="this.innerHTML='%s'" onmouseout="this.innerHTML='Username'">Username</button></td></tr>
<tr><td><button onmouseover="this.innerHTML='%s'" onmouseout="this.innerHTML='Password'">Password</button></td></tr>


</table></div></div>
</div><br><br>
</center>
<!-- < Content ends here......> -->

</body>
</html>"""%(r[2],r[1],r[3],r[4],r[5],r[6],r[7],r[8],r[9]))
