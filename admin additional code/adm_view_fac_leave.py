#!C:/Users/thanu/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import header
header.hdr()
import cgi,cgitb,pymysql,smtplib
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root", password="",database="scampus")
cur = conn.cursor()
f=cgi.FieldStorage()
flid=f.getvalue("flid")
st=f.getvalue("st")	
if st!=None:
	upd = """update faculty_leave set status='%s' where leave_id='%s'"""%(st,flid)
	cur.execute(upd)
	conn.commit()

	if st == "Accept" or st == "Reject":
		s = """select mailid from faculty where faculty_id = (select faculty_id from faculty_leave where leave_id='%s')""" % (flid)
		cur.execute(s)
		toadd = cur.fetchone()[0]  # Fetching email address of the faculty

		fromadd = 'shathanu000@gmail.com'  # Update with your email address
		password = 'ebbn vmop hyfm fobs'  # Update with your email password
		subject = "Leave Request Status"
		body = "Your leave request has been %s." % st
		msg = """Subject: %s\n\n%s""" % (subject, body)

		try:
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.starttls()
			server.login(fromadd, password)
			server.sendmail(fromadd, toadd, msg)
			server.quit()
			print("<script>alert('Email sent to faculty.'); location.href='adm_view_fac_leave.py';</script>")
		except Exception as e:
			print(
				"<script>alert('Failed to send email. Error: %s'); location.href='adm_view_fac_leave.py';</script>" % str(e))

	print("""<script>alert('Updated');location.href='adm_view_fac_leave.py';</script>""")

print("""<html>
<head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
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

<div style="margin-top:60px;">

<center>
<h1>Faculty Leave Request</h1>

<table border='2'>
<tr>
<th> S.No. </th>
<th>Faculty Id </th>
<th>Name </th>
<th>Department </th>
<th>Date </th>
<th> No of Days</th>
<th>Reason </th>
<th> Approve</th>
</tr>""")
sql = """select * from faculty_leave where status='%s'"""%("")
cur.execute(sql)
r=cur.fetchall()
cnt=0
for i in r:
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
		<td><a href='adm_view_fac_leave.py?flid=%s&st=%s'>Accept</a>
		     <br><a href='adm_view_fac_leave.py?flid=%s&st=%s'>Reject</a></td>
		
	</tr>
	"""%(cnt,i[2],i[3],i[4],i[5],i[6],i[7],i[1],"Accept",i[1],"Reject"))

print("""</table>
</center>
</div><br><br>

<!-- < Content ends here......> -->

</body>
</html>""")
