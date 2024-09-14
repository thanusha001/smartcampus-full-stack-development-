# smartcampus-full-stack-development-

# Smart Campus

## Project Overview
The **Smart Campus** system aims to streamline the academic and administrative processes in colleges. It provides a centralized platform for students, faculty, and administrators to manage various tasks such as attendance, course enrollment, assignment submissions, and leave applications, while keeping everyone updated on college events. The platform enhances efficiency, transparency, and engagement within the campus community.

## Features
- **Administrator Features:**
  - Manage user accounts (students, faculty).
  - Approve courses, manage leaves, and maintain event forums.
  - Monitor attendance and results.
  - Generate reports related to students, faculty, and courses.

- **Faculty Features:**
  - Update attendance and results.
  - Assign and evaluate assignments.
  - Offer short-term courses.
  - Apply for leave and answer student queries.

- **Student Features:**
  - View attendance and results.
  - Enroll in courses and upload assignments.
  - Apply for leave and ask queries related to subjects.

## Technologies Used
- **Frontend:** JavaScript
- **Backend:** Python, MySQL
- **Frameworks/Libraries:** jQuery
- **Database:** MySQL
- **Design Patterns:** MVC Architecture
- **Tools:** PyCharm for development

## Database Structure
The system includes a well-structured database to store user data, course information, attendance records, assignment submissions, and leave requests. Key tables include:
- **Users**: Manages user login credentials and roles.
- **Courses**: Stores course details and enrollments.
- **Attendance**: Logs attendance records for students.
- **Assignments**: Handles submission and evaluation of assignments.
- **Leave Requests**: Tracks leave applications for students and faculty.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-campus.git
   ```
2. Install the required dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database with the provided schema in `/db/schema.sql`.
4. Run the application:
   ```bash
   python app.py
   ```

## Usage
- **Login as Admin/Faculty/Student**: Use the credentials provided to access respective dashboards.
- **Student Dashboard**: View and manage attendance, results, assignments, and leave requests.
- **Faculty Dashboard**: Track attendance, assign grades, and respond to student queries.
- **Admin Dashboard**: Manage all user data, courses, and campus events.

## Testing
- Unit and system tests were performed to ensure the robustness of the platform. Key areas tested include user authentication, course enrollments, and data security.

## Future Enhancements
- Integration with mobile platforms for easier access.
- Add more detailed analytics for students' progress tracking.
- Enable real-time notifications for students and faculty on upcoming events and deadlines.

## Description
Smart Campus is a digital platform designed to make college management easier for students, faculty, and administrators. It allows students to check their attendance, view results, submit assignments, and apply for leave. Faculty can update attendance, assign grades, upload assignments, and offer short-term courses. Administrators can manage all user accounts, approve courses, handle leave requests, and share important updates with everyone.

By automating tasks like attendance and assignment submissions, the Smart Campus system helps save time, reduces paperwork, and improves communication between students, teachers, and staff. It’s built using JavaScript for the frontend and Python with MySQL for the backend, ensuring that it's reliable, secure, and easy to use.


