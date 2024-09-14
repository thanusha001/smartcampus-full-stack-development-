#!C:/Users/thanu/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import header
header.hdr()

import cgi,cgitb,pymysql
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root", password="",database="scampus")
cur = conn.cursor()
sql2 = """select max(id) from announcement"""
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
anceid="ance"+z+str(r2[0]+1)

print("""<html><head>
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
    
			
			textarea{
				width:400px;
				
				border-radius:5px;
				background-color:a2a2a2;
				color:blue;
				font-size:10pt;
				font-weight:bold;
				border:2px solid #a2a2a2;
			}
			
	</style>
</head>
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
	<h1>Announcements</h1>""")

print("""<div class="container">
			<div class="container mt-5">
				<form action="announcement.py" enctype ="multipart/form-data" method="post" >
					<div class="row justify-content-center">   
						<div class="col-md-4">   
							<div class="form-group">  
								<input type="text" name="aid" value="%s" class="form-control" readonly>
							</div>   
                            <div class="form-group">  
								<input type="text" name="subject" placeholder="Subject" class="form-control" autocomplete="off" required>
                            </div> 
                            <div class="form-group"> 
                                <select name="msgto" class="form-control">
									<option value=" ---staff / student---">---staff / student---</option>
									<option value="Staff">Staff</option>
									<option value="Student">Student</option>
								</select>
                            </div> 
							<div class="form-group">       
								<textarea name="ance" cols="50" placeholder="Announcement" class="form-control" rows="5"></textarea>
                            </div> 
                             
                            <div class="d-flex justify-content-center">
                                <div class="form-row">
                                  <div class="col-text-right">
                                    <input type="submit" class="btn btn-success btn-sm"  value="Send"  name="sub">
                 					</div>
                                  <div class="col-text-right">
                                    <input type="reset" class="btn btn-danger btn-sm"  value="Clear">
              						</div>
                                </div>


                        	</div>
                    </div>
                    </div>
                </form>
                </div>
                </div><br><br>
</body>
</html>"""%(anceid))
f=cgi.FieldStorage()
sub=f.getvalue("sub")
if sub!=None:
	aid=f.getvalue("aid")
	subject=f.getvalue("subject")
	msgto=f.getvalue("msgto")
	ance=f.getvalue("ance")
	
	sql = """insert into announcement values('','%s','%s','%s','%s')"""%(aid,subject,msgto,ance)
	cur.execute(sql)
	conn.commit()

	print("""<script>alert('Announcement added successfully...');location.href='announcement.py';</script>""")
