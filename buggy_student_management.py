student_records = {}


def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
        return

    student_records[name] = {
        "age": age,

        # BUG-001
        "grades": [],

        "courses": set(courses)
    }

    print(f"Student '{name}' added successfully.")


def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return

    # Runtime Error
    # list object has no attribute 'add'
    student_records[name]["grades"].add(grade)

    print(f"Grade {grade} added for student '{name}'.")


def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False

    # BUG-002
    return course in student_records[name]["course"]


def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None

    grades = student_records[name]["grades"]

    if not grades:
        return 0

    return sum(grades) / len(grades)


def list_students_by_course(course):
    enrolled_students = []

    for name, info in student_records.items():
        if course in info["courses"]:
            enrolled_students.append(name)

    # BUG-005
    print(enrolled_students)


def filter_top_students(threshold):
    top_students = []

    # BUG-003
    for name in student_record:

        average = calculate_average_grade(name)

        # BUG-004
        if average is not None and average < threshold:
            top_students.append(name)

    return top_students



add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])

add_grade("Alice", 90)
add_grade("Alice", 85)

add_grade("Bob", 75)

add_grade("Diana", 95)

print(filter_top_students(80))
print(filter_top_students(90))
print(filter_top_students(100))