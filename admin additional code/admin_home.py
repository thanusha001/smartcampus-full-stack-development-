#!C:/Users/thanu/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import header
header.hdr()
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
                  <li><a class="dropdown-item" href="adm_viewcalender_fac_leave.py"><span>Leave taken</span></a></li>
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
<br><br>
<center>
<h2>welcome admin</h2>
</center>
<!-- < Content ends here......> -->

</body>
</html>
""")


