TESTING GUIDE
Purpose
This document describes the testing process followed to validate the fixes applied to the Student Management System.

The objective of testing was to verify:

Bug reproduction
Bug resolution
Functional correctness
Expected outputs
System stability after modifications
Testing Environment
Component	Details
Language	Python 3.x
IDE	Visual Studio Code
Debugger	pdb
Platform	Windows 11
Test Data
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])

add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
___________________________________________________________________________________________________
BUG-001 Test
Purpose
Verify grade storage functionality.

Bug
"grades": []
Expected Error
AttributeError:
'list' object has no attribute 'add'
Fix
"grades": set()
Result
PASS ✅
___________________________________________________________________________________________________
BUG-002 Test
Purpose
Verify student enrollment checking.

Buggy Test
print(is_enrolled("Alice", "Math"))
Expected Error
KeyError: 'course'
Fix
student_records[name]["courses"]
Result
True
PASS ✅
____________________________________________________________________________________________________
BUG-003 Test
Purpose
Verify student filtering iteration.

Bug
for name in student_record:
Expected Error
NameError
Fix
for name in student_records:
Result
Program executed successfully.

PASS ✅
____________________________________________________________________________________________________
BUG-004 Test
Purpose
Verify top student filtering.

Bug
if average < threshold
Incorrect Output
['Bob']
Fix
if average > threshold
Correct Output
['Alice', 'Diana']
PASS ✅
______________________________________________________________________________________________________
BUG-005 Test
Purpose
Verify student listing function.

Test
print(list_students_by_course("Math"))
Buggy Output
['Alice', 'Bob']
None
Fix
return enrolled_students
Correct Output
['Alice', 'Bob']
PASS ✅

Final Functional Tests
Test Case 1
Input

filter_top_students(80)
Expected Output

['Alice', 'Diana']
Actual Output

['Alice', 'Diana']
Result

✅ PASS

Test Case 2
Input

filter_top_students(90)
Expected Output

['Diana']
Actual Output

['Diana']
Result

✅ PASS

Test Case 3
Input

filter_top_students(100)
Expected Output

[]
Actual Output

[]
Result

✅ PASS

Test Case 4
Input

is_enrolled("Alice", "Math")
Expected Output

True
Actual Output

True
Result

✅ PASS

Test Case 5
Input

list_students_by_course("Math")
Expected Output

['Alice', 'Bob']
Actual Output

['Alice', 'Bob']
Result

✅ PASS

Testing Summary
Test Case	Status
BUG-001	PASS
BUG-002	PASS
BUG-003	PASS
BUG-004	PASS
BUG-005	PASS
Final Functional Tests	PASS
Conclusion
All identified bugs were successfully reproduced and resolved. Functional, logical, and runtime testing confirmed that the corrected version of the Student Management System behaves as expected.