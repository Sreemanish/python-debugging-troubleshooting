Student Management System - Debugging and Troubleshooting Project
=================================================================

Project Overview
----------------
This project was completed as part of the Week 2 Debugging and Troubleshooting Python Applications assignment.

The objective was to simulate a real-world debugging scenario by identifying, reproducing, analyzing, documenting, and fixing defects in a Python-based Student Management System. The application manages student records, course enrollments, academic grades, and top-performing student identification.

During the project, several bugs were intentionally introduced into a working application. Each bug was investigated using structured debugging techniques, fixed systematically, and documented thoroughly.

Project Objectives
------------------
The primary objectives of this project were:

Perform an initial code review.
Identify runtime and logical errors.
Reproduce bugs consistently.
Analyze traceback information.
Apply debugging techniques.
Use Python debugging tools.
Document the troubleshooting process.
Refactor code for readability and maintainability.
Verify fixes through testing.

Application Features
--------------------
The Student Management System supports:

Student Management
Add new students
Prevent duplicate student records
Track student age information
Course Management
Store enrolled courses
Verify course enrollment
List students enrolled in specific courses
Grade Management
Add student grades
Calculate average grades
Filter top-performing students

Bugs Identified
---------------
Bug ID	Description	Type
BUG-001	Grades initialized as List instead of Set	AttributeError
BUG-002	Incorrect dictionary key ("course")	KeyError
BUG-003	Incorrect variable name (student_record)	NameError
BUG-004	Incorrect filtering condition	Logical Error
BUG-005	Missing return statement	Functional Error

Tools Used
----------
Python 3.x
Visual Studio Code
pdb Debugger
Git
GitHub
Project Structure
Debugging and Troubleshooting/

├── Buggyscript.py
├── Fixedscript.py
├── DEBUGGING_LOG.md
├── TESTING_GUIDE.md
├── README.md
├── screenshots/
│
├── BUG-001_AttributeError.png
├── BUG-003_NameError.png
├── BUG-004_LogicalError.png
└── BUG-005_ReturnIssue.png
Application Flow Diagram
flowchart TD

A[Start]
B[Add Student]
C[Store Courses]
D[Add Grades]
E[Calculate Average Grades]
F[Filter Top Students]
G[Display Results]
H[End]

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
G --> H
Sample Input
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])

add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
Expected Output
print(filter_top_students(80))
print(filter_top_students(90))
print(filter_top_students(100))
Output:

['Alice', 'Diana']
['Diana']
[]
Learning Outcomes
Through this project, the following debugging skills were developed:

Reading Tracebacks
Debugging AttributeError
Debugging NameError
Debugging KeyError
Resolving Logical Errors
Root Cause Analysis
Incremental Testing
Code Refactoring
Documentation Practices
Git and GitHub Workflow
Final Result
All identified defects were successfully reproduced, documented, fixed, and verified. The Student Management System now functions as expected and passes all test cases.