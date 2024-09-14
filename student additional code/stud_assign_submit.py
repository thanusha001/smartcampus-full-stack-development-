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
aid=f.getvalue("aid")
sql = """select * from student where id=%s"""%(id)
cur.execute(sql)
r=cur.fetchone()

sql1 = """select * from faculty_assignment where assign_id='%s'"""%(aid)
cur.execute(sql1)
r1=cur.fetchone()

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

<div class="container-fluid">
             <div class="container mt-5">
                <form action="stud_assign_submit.py" enctype ="multipart/form-data" method="post" >
                    <div class="row justify-content-center"> 
                    <h1>Submit Assignment</h1> 
                        <div class="col-md-4">   
                            <div class="form-group">  
								<input type="hidden" name="id" value="%s" class="form-control" readonly>
                                </div>   
                            <div class="form-group">
                              <input type="hidden" name="fac_id" value="%s" class="form-control" readonly>
                            </div>  
                            <div class="form-group">   
                                <input type="text" name="aid" value="%s" class="form-control" readonly>
                            </div> 
                            <div class="form-group"> 
                            	<input type="text" name="stud_id" value="%s" class="form-control" readonly>
                            </div>
                            <h2>Select your document here..</h2>
                                 <div class="form-group">  
                                	<input type="file" name="a_output" class="form-control" accept=".txt,.doc,.pdf">
                                </div>
                            <div class="d-flex justify-content-center">
                                <div class="form-row">
                                  <div class="col-text-right">
                                    <input type="submit" class="btn btn-success"  value="Add"  name="sub">
                 					</div>
                                  <div class="col-text-right">
                                    <input type="reset" class="btn btn-danger"  value="Cancel"  onclick="location.href='index.html';">
              						</div>
                                </div>

                        	</div>
                    </div>
                    </div>
                </form>
                </div>
                </div><br><br>

</body>
</html>
"""%(id,r1[1],aid,r[1]))
sub=f.getvalue("sub")
if sub!=None:
	fac_id = f.getvalue("fac_id")
	stud_id = f.getvalue("stud_id")
	afile=f['a_output']
	if afile.filename:
		fn1=os.path.basename(afile.filename)
		open("files/"+fn1,"wb").write(afile.file.read())
	
		sql = """insert into student_assign(faculty_id,assign_id,stud_id,assignment) values('%s','%s','%s','%s')"""%(fac_id,aid,stud_id,fn1)
		cur.execute(sql)
		conn.commit()
		print("""<script>alert('Congrats, you are submit your assignment successfully...');location.href='stud_view_assign.py?id=%s';</script>"""%(id))
