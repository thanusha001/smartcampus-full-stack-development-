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

sql2 = """select max(id) from faculty_leave"""
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
flid="flid"+z+str(r2[0]+1)

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
print("""<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
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
</nav>"""%(id,id,id,id,id,id,id,id,id))
print("""<center>
	<div class="container">
		<div class="container mt-5">
			<form action="fac_apply_leave.py"  enctype ="multipart/form-data" method="post" >
				<div class="row justify-content-center">   
					<div class="col-md-4"> 
						<h1>Leave Request</h1>  
							<div class="form-group">    
								<input type="hidden" name="id" value="%s" >
							</div>   
							<div class="form-group">
								<input type="hidden" name="flid" value="%s">
                            </div>
							<div class="form-group">
								<input type="text" name="name" class="form-control" value="%s">
							</div>
							<div class="form-group">
								<input type="text" name="dept" class="form-control" value="%s">
							</div>
							<div class="form-group">
								<input type="text" name="fid" class="form-control" value="%s" readonly>
							</div> 
                              
                            <h2>Date:</h2>
                            <div class="form-group">   
                                <input type="date" name="ldate" class="form-control" required>	
                            </div> 
                            <div class="form-group">   
                                <input type="number" name="nodays" class="form-control" placeholder="No of days" required>
                            </div> 
                            <div class="form-group"> 
                            	<select name="reason" class="form-control">
									<option value="Personal">Personal</option>
									<option value="Function">Function</option>
									<option value="Sick">Sick</option>
								</select>
                            </div>
                            <div class="d-flex justify-content-center">
                                <div class="form-row">
									<div class="col-text-right">
										<input type="submit" class="btn btn-success btn-sm"  value="Send"  name="sub">
                 					</div>
									<div class="col-text-right">
										<input type="reset" class="btn btn-danger btn-sm"  value="Clear"  ><br><br>
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
</html>"""%(id,flid,r[2],r[4],r[1]))
sub=f.getvalue("sub")
if sub!=None:
	flid=f.getvalue("flid")
	name=f.getvalue("name")
	fid=f.getvalue("fid")
	dept=f.getvalue("dept")
	ldate=f.getvalue("ldate")
	nodays=f.getvalue("nodays")
	reason=f.getvalue("reason")

	sql = """insert into faculty_leave(leave_id,faculty_id,faculty_name,department,ldate,nodays,reason) values('%s','%s','%s','%s','%s','%s','%s')"""%(flid,fid,name,dept,ldate,nodays,reason)
	cur.execute(sql)
	conn.commit()

	print("""<script>alert('Request sent...');location.href='fac_apply_leave.py?id=%s'</script>"""%(id))
