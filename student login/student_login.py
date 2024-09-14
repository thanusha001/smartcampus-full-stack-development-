#!C:/Users/thanu/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import header
header.hdr()
import cgi,pymysql,os
import smtplib,cgitb;cgitb.enable()

conn = pymysql.connect(host="localhost",user="root", password="",database="scampus")
cur=conn.cursor()

f=cgi.FieldStorage()

print("""<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.2/font/bootstrap-icons.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>



   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
	<style>
		.login-container {

        width: 500px;
        height: 290px;

        padding: 20px;
        background-color: #f1f7f4;
        box-shadow: 0 0 10px rgba(47, 45, 45, 0.1);
        border-radius: 5px;
        opacity:0.8;
      }

      .card{
        height: 250px;
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

	</style>
</head>
<body>

   <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto">
           <li class="nav-item">
               <a class="nav-link" href="index.html"><span>Home</span></a>
           </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Course</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="home_crs_details.py"><span>Course Details</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Staff Login</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="adm_login.py"><span>Admin</span></a></li>
                  <li><a class="dropdown-item" href="faculty_login.py"><span>Faculty</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
            <li class="nav-item dropdown" >
              <a class="nav-link dropdown-toggle" id="navbarDropdown" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><span>Student</span></a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="student_reg.py"><span>Register</span></a></li>
                  <li><a class="dropdown-item" href="student_login.py"><span>Login</span></a></li>
              </ul>
            </li>
          </li>
          <li class="nav-item">
               <a class="nav-link" href="contact.py"><span>Contact</span></a>
           </li>
      </ul>
    </div>
  </div>
</nav>

<!-- <Content starts here......> -->
<center>
<h1>student Login</h1>
	<div class="login-container">
		<div class="card">
			<div class="card-body">
				<form id="loginForm" action="student_login.py" method="post" enctype="multipart/form-data">
					<div class="form-group">
						<div class="input-group">
							<div class="input-group-prepend">
								<span class="input-group-text" id="rolodex"><i class="bi bi-person-rolodex"></i></span>
							</div>
							<input type="text" class="form-control" id="username" name="uname" placeholder="User Name" autocomplete="off" required><br><br> 
						</div>
					</div>
					<div class="form-group">
						<div class="input-group">
							<div class="input-group-prepend">
								<span class="input-group-text" id="lock"><i class="bi bi-person-fill-lock"></i></span>
							</div>
							<input type="Password" class="form-control" id="password" name="pwd" placeholder="Password" autocomplete="off" required><br><br>
						</div>
					</div> 
					
					<div class="d-flex justify-content-center">
						<div class="form-row">
							<div class="col-text-right">
								<input type="submit" class="btn btn-success"  value="Login"  name="sub"><br><br>
							
							</div>
							<div class="col-text-right">
								<input type="button" class="btn btn-danger"  value="Cancel"  onclick="location.href='index.html';">
							</div>
						</div>
					</div>
					
					                            <button type="button" class="btn btn-link" data-bs-toggle="modal" data-bs-target="#forgotPasswordModal">Forgot Password?</button>

				</form>
			</div>
		</div>
	</div><br><br>
</center>
<!-- < Content ends here......> -->
<!-- Forgot Password Modal -->
<div class="modal fade" id="forgotPasswordModal" tabindex="-1" aria-labelledby="forgotPasswordModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="forgotPasswordModalLabel">Forgot Password?</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form id="forgotPasswordForm" action="stud_forgot_password.py" method="post">
          <div class="form-group">
            
            <input type="email" class="form-control" id="email" name="email" placeholder="enter your email" required>
          </div>
          <button type="submit" class="btn btn-primary">Send</button>
        </form>
      </div>
    </div>
  </div>
</div>

</body>
</html>""")

uname=f.getvalue("uname")
pwd=f.getvalue("pwd")
sub=f.getvalue("sub")
if sub!=None:
	q1="""select * from student where username='%s' and password='%s'""" % (uname,pwd)
	cur.execute(q1)
	r=cur.fetchone()

	if r!=None:
		print("""<script>alert("Successfully logged");location.href="student_home.py?id=%s";</script>"""%(r[0]))
	else:
		print("""<script>alert("Invalid Username or password... ");location.href="student_login.py";</script>""")
conn.close()
