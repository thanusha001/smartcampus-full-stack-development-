#!C:/Users/thanu/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, pymysql, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

f = cgi.FieldStorage()

email = f.getvalue("email")

conn = pymysql.connect(host="localhost", user="root", password="", database="scampus")
cur = conn.cursor()

q = """SELECT * FROM faculty WHERE mailid='%s'""" % email
cur.execute(q)
result = cur.fetchone()

if result:
    # Send email with password
    sender_email = "shathanu000@gmail.com"  # Change to your email
    receiver_email = email
    password = "ebbn vmop hyfm fobs"  # Change to your email password

    message = MIMEMultipart("alternative")
    message["Subject"] = "Password Recovery"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "Your password is: %s" % result[9]  # Assuming password is in the second column
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    with smtplib.SMTP("smtp.gmail.com:587") as server:  # Change to your SMTP server
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("""<script>alert('email has been sent...');location.href='faculty_login.py';</script>""")

    # print("Content-type:text/html\r\n\r\n")
    # print("<html>")
    # print("<head>")
    # print("<title>Password Recovery</title>")
    # print("</head>")
    # print("<body>")
    # print("<h2>Password Recovery</h2>")
    # print("<p>An email has been sent to your registered email address with your password.</p>")
    # print("</body>")
    # print("</html>")
else:
    print("""<script>alert('email not found...');location.href='faculty_login.py';</script>""")
    # print("Content-type:text/html\r\n\r\n")
    # print("<html>")
    # print("<head>")
    # print("<title>Password Recovery</title>")
    # print("</head>")
    # print("<body>")
    # print("<h2>Password Recovery</h2>")
    # print("<p>Email not found. Please try again.</p>")
    # print("</body>")
    # print("</html>")

conn.close()
