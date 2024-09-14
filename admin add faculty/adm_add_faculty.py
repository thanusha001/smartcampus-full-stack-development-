#!C:/Users/thanu/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import header
header.hdr()
import cgi,cgitb,pymysql,smtplib
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root", password="",database="scampus")
cur = conn.cursor()

sql2 = """select max(id) from faculty"""
cur.execute(sql2)
r2=cur.fetchone()
if r2[0]==None:
	r2[0]=0
z=""
if r2[0]<=9:
	z="000"
elif r2[0]>=10 and r2[0]<=99:
	z="00"
elif r2[0]>=100 and r2[0]<=999:
	z="0"
facid="faculty"+z+str(r2[0]+1)
print("""<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.2/font/bootstrap-icons.min.css">

        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"><!--it give good align-->
       


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
	<h1>Add Faculty</h1>""")
print("""<center>
	<div class="container-fluid">
             <div class="container mt-5">
                <form action="adm_add_faculty.py" enctype ="multipart/form-data" method="post" >
                    <div class="row justify-content-center">   
                        <div class="col-md-4">   
                            <div class="form-group">  
                                <input type="text" name="fid"   class="form-control" value="%s" readonly>  
                                </div>   
                            <div class="form-group">
                               <input type="text" id="fname" name="fname" class="form-control" placeholder="Faculty Name" autocomplete="off" required>
                            </div> 
                            <div class="form-group"> 
                                <select class="form-control" name="qual">
                                    <option value="BE/BTECH">BE/BTECH</option>
									<option value="ME/MTECH">ME/MTECH</option>
									<option value="MBA/MCOM">MBA/MCOM</option>
									<option value="MSC/MCA">MSC/MCA</option>
                                </select> 
                            </div> 
                            <div class="form-group"> 
                                <select class="form-control" name="dept">
                                    <option value="Computer Science">Computer Science</option>
                                    <option value="Commerce">Commerce</option>
                                </select> 
                            </div>  
                            <h2>Date of Joining:</h2>
                            <div class="form-group">   
                                <input type="date" class="form-control" name="doj"  required>
                            </div> 
                            <div class="form-group"> 
                            	<input type="text" name="contact" class="form-control"  placeholder="Contact Number" autocomplete="off" required>
		  
                                </div>
                                 <div class="form-group">  
                                 <input type="email" name="mailid" class="form-control" placeholder="Mail Id" autocomplete="off" required>
		 
                                </div>
                                 <div class="form-group"> 
                                 <input type="text" name="uid"  class="form-control" placeholder="User login Id" id="uid" autocomplete="off" value="%s" readonly>
		  
                                </div>
                                 <div class="form-group">  
                                 <input type="password" name="pwd" class="form-control" placeholder="Password" autocomplete="off" required>
		 
                                </div>   
                            <div class="d-flex justify-content-center">
                                <div class="form-row">
                                  <div class="col-text-right">
                                    <input type="submit" class="btn btn-success btn-sm"  value="Add"  name="sub">
                 					</div>
                                  <div class="col-text-right">
                                    <input type="reset" class="btn btn-danger btn-sm"  value="Cancel"  onclick="location.href='index.html';"><br><br>
              						</div>
                                </div>

                        	</div>
                    </div>
                    </div>
                </form>
                </div>
                </div>
</center>
<!-- < Content ends here......> -->

</body>
</html>""" %(facid,facid))

f=cgi.FieldStorage()
sub=f.getvalue("sub")
if sub!=None:
	fid=f.getvalue("fid")
	fname=f.getvalue("fname")
	qual=f.getvalue("qual")
	dept=f.getvalue("dept")
	doj=f.getvalue("doj")
	contact=f.getvalue("contact")
	mailid=f.getvalue("mailid")
	uid=f.getvalue("uid")
	pwd=f.getvalue("pwd")

	sql = """insert into faculty values('','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(fid,fname,qual,dept,doj,contact,mailid,uid,pwd)
	cur.execute(sql)
	conn.commit()
	fromadd = 'shathanu000@gmail.com'
	password = 'ebbn vmop hyfm fobs'
	toadd = mailid
	subject = " your password"
	body = "your password is {} ".format(pwd)
	msg = """Subject:{} \n\n{}""".format(subject, body)
	server = smtplib.SMTP("smtp.gmail.com:587")
	server.ehlo()
	server.starttls()
	server.login(fromadd, password)
	server.sendmail(fromadd, toadd, msg)
	server.quit()

	print("""<script>alert('Faculty added successfully...');location.href='adm_add_faculty.py';</script>""")
