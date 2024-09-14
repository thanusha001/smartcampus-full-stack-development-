#!C:/Users/thanu/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import header
header.hdr()
import cgi,cgitb,pymysql
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root", password="",database="scampus")
cur = conn.cursor()

print("""<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.2/font/bootstrap-icons.min.css">



   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>


	
	<style>
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
""")
print("""

<!-- <Content starts here......> -->
<div class="container-fluid">
             <div class="container mt-5">
                <form action="student_reg.py" enctype ="multipart/form-data" method="post" >
                    <div class="row justify-content-center"> 
                    <h1>Student Register...</h1>  
                        <div class="col-md-4">   
                            <div class="form-group">  
                               
                                <input type="text" name="sid" placeholder="Roll Number" class="form-control" autocomplete="off" required> 
                                </div>   
                            <div class="form-group">
                              <input type="text" name="sname" placeholder="Student Name" class="form-control" autocomplete="off" required>
                            </div> 
                            <div class="form-group"> 
								<select name="deg" class="form-control">
									<option value="BSC">BSC</option>
									<option value="BCA">BCA</option>
									<option value="BBA">BBA</option>
									<option value="BCOM">BCOM</option>
								</select>
							</div>
							<div class="form-group"> 
                                <select name="dept" class="form-control">
									<option value="Computer Science">Computer Science</option>
									<option value="Commerce">Commerce</option>
								</select>
                            </div>  
                            <div class="form-group"> 
                                <select name="batch" class="form-control">
									<option value="2023-2026">2023-2026</option>
									<option value="2024-2027">2024-2027</option>
									<option value="2025-2028">2025-2028</option>
									<option value="2026-2029">2026-2029</option>
								</select>
                            </div> 
                            
                            <div class="form-group">   
                                <input type="text" name="contact" placeholder="Contact Number" class="form-control" autocomplete="off" required>
                            </div> 
                            <div class="form-group"> 
                            	<input type="email" name="mailid" placeholder="Mail Id" class="form-control" autocomplete="off" required onchange="document.getElementById('uid').value=this.value;">
                                </div>
                                 <div class="form-group">  
                                 <input type="text" name="uid" placeholder="User login Id" class="form-control" id="uid" autocomplete="off" readonly>
                                </div>
                                 <div class="form-group"> 
                                <input type="password" name="pwd" placeholder="Password" class="form-control" autocomplete="off" required>
		
                                </div>
                                  
                            <div class="d-flex justify-content-center">
                                <div class="form-row">
                                  <div class="col-text-right">
                                    <input type="submit" class="btn btn-success "  value="Add"  name="sub">
                 					</div>
                                  <div class="col-text-right">
                                    <input type="reset" class="btn btn-danger "  value="Cancel"  onclick="location.href='index.html';">
              						</div>
                                </div>

                        	</div>
                    </div>
                    </div>
                </form>
                </div>
                </div><br><br>
</body>
</html>""")
f=cgi.FieldStorage()
sub=f.getvalue("sub")
if sub!=None:
	sid = f.getvalue("sid")
	sname = f.getvalue("sname")
	deg= f.getvalue("deg")
	dept = f.getvalue("dept")
	batch= f.getvalue("batch")
	contact = f.getvalue("contact")
	mailid = f.getvalue("mailid")
	uid = f.getvalue("uid")
	pwd = f.getvalue("pwd")
	q="""select * from student where roll_no='%s'"""%(sid)
	cur.execute(q)
	r=cur.fetchone()
	if r==None:
		sql = """insert into student values('','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(sid,sname,deg,dept,batch,contact,mailid,uid,pwd)
		cur.execute(sql)
		conn.commit()

		print("""<script>alert('You are registered successfully...');location.href='student_login.py';</script>""")
	else:
		print("""<script>alert('You are already registered...');location.href='student_reg.py';</script>""")