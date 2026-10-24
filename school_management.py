# School Management System

# Data Storage
students = {}
teachers = {}
subjects = ["English", "Mathematics", "Physics", "Chemistry", "Computer"]


def validate_student_id():
    while True:
        s_id = input("Enter Student ID (e.g., ST101): ").strip().upper()
        if not s_id:
            print("Error: Student ID cannot be empty.")
        elif s_id in students:
            print("Student ID already exists. Please enter another ID.")
        else:
            return s_id


def add_student():
    print("\n--- ADD NEW STUDENT ---")
    s_id = validate_student_id()
    name = input("Enter Student Name: ").strip().title()
    
    while True:
        try:
            age = int(input("Enter Age: "))
            if age > 0:
                break
            print("Age must be positive.")
        except ValueError:
            print("Invalid input! Please enter a numeric age.")

    gender = input("Enter Gender (Male/Female/Other): ").strip().capitalize()
    s_class = input("Enter Class: ").strip()
    section = input("Enter Section: ").strip().upper()
    father_name = input("Enter Father's Name: ").strip().title()
    contact = input("Enter Contact Number: ").strip()

    students[s_id] = {
        "info": {
            "name": name,
            "age": age,
            "gender": gender,
            "class": s_class,
            "section": section,
            "father_name": father_name,
            "contact": contact
        },
        "attendance": {"present": 0, "absent": 0, "leave": 0, "total": 0},
        "marks": {},
        "academic_summary": {"total_marks": 0, "percentage": 0.0, "grade": "N/A", "status": "N/A"},
        "fees": {"monthly_fee": 0.0, "paid_amount": 0.0, "remaining": 0.0, "status": "Pending"}
    }
    print(f"\nStudent '{name}' with ID '{s_id}' registered successfully!")


def view_students():
    print("\n--- ALL REGISTERED STUDENTS ---")
    if not students:
        print("No student records found.")
        return

    print(f"{'ID':<10} {'Name':<20} {'Class':<8} {'Section':<8} {'Contact'}")
    print("-" * 60)
    for s_id, data in students.items():
        info = data["info"]
        print(f"{s_id:<10} {info['name']:<20} {info['class']:<8} {info['section']:<8} {info['contact']}")


def update_student():
    print("\n--- UPDATE STUDENT INFORMATION ---")
    s_id = input("Enter Student ID to update: ").strip().upper()
    if s_id not in students:
        print(f"Error: Student ID '{s_id}' not found.")
        return

    info = students[s_id]["info"]
    print(f"Updating details for {info['name']} (Leave blank to keep current value):")

    new_name = input(f"New Name [{info['name']}]: ").strip()
    if new_name:
        info['name'] = new_name.title()

    new_class = input(f"New Class [{info['class']}]: ").strip()
    if new_class:
        info['class'] = new_class

    new_sec = input(f"New Section [{info['section']}]: ").strip()
    if new_sec:
        info['section'] = new_sec.upper()

    new_contact = input(f"New Contact [{info['contact']}]: ").strip()
    if new_contact:
        info['contact'] = new_contact

    print("Student information updated successfully!")


def delete_student():
    print("\n--- DELETE STUDENT RECORD ---")
    s_id = input("Enter Student ID to delete: ").strip().upper()
    if s_id not in students:
        print(f"Error: Student ID '{s_id}' not found.")
        return

    confirm = input(f"Are you sure you want to delete {students[s_id]['info']['name']}? (y/n): ").strip().lower()
    if confirm == 'y':
        del students[s_id]
        print(f"Student ID '{s_id}' deleted successfully.")
    else:
        print("Deletion cancelled.")


def student_management_menu():
    while True:
        print("\n=== STUDENT MANAGEMENT ===")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Back to Main Menu")

        choice = input("Enter option (1-6): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            break
        else:
            print("Invalid selection!")


def add_teacher():
    print("\n--- ADD NEW TEACHER ---")
    t_id = input("Enter Teacher ID (e.g., T101): ").strip().upper()
    if t_id in teachers:
        print("Teacher ID already exists.")
        return

    name = input("Enter Teacher Name: ").strip().title()
    subject = input("Enter Subject Taught: ").strip().capitalize()
    qualification = input("Enter Qualification: ").strip()
    
    try:
        exp = int(input("Years of Experience: "))
    except ValueError:
        exp = 0

    contact = input("Contact Number: ").strip()
    assigned_class = input("Assigned Class/Grade: ").strip()

    teachers[t_id] = {
        "name": name,
        "subject": subject,
        "qualification": qualification,
        "experience": exp,
        "contact": contact,
        "assigned_class": assigned_class
    }
    print(f"Teacher '{name}' added successfully!")


def view_teachers():
    print("\n--- ALL TEACHERS ---")
    if not teachers:
        print("No teacher records found.")
        return

    for t_id, data in teachers.items():
        print(f"ID: {t_id} | Name: {data['name']} | Subject: {data['subject']} | Class: {data['assigned_class']} | Contact: {data['contact']}")


def teacher_management_menu():
    while True:
        print("\n=== TEACHER MANAGEMENT ===")
        print("1. Add Teacher")
        print("2. View Teachers")
        print("3. Search Teacher")
        print("4. Back to Main Menu")

        choice = input("Enter option (1-4): ").strip()
        if choice == "1":
            add_teacher()
        elif choice == "2":
            view_teachers()
        elif choice == "3":
            t_id = input("Enter Teacher ID: ").strip().upper()
            if t_id in teachers:
                t = teachers[t_id]
                print(f"\nID: {t_id}\nName: {t['name']}\nSubject: {t['subject']}\nQualification: {t['qualification']}\nExperience: {t['experience']} yrs\nContact: {t['contact']}\nClass: {t['assigned_class']}")
            else:
                print("Teacher not found.")
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


def mark_attendance():
    print("\n--- ATTENDANCE MANAGEMENT ---")
    s_id = input("Enter Student ID: ").strip().upper()
    if s_id not in students:
        print("Student not found.")
        return

    print("Mark status: P = Present, A = Absent, L = Leave")
    status = input("Enter status (P/A/L): ").strip().upper()

    att = students[s_id]["attendance"]
    if status == 'P':
        att["present"] += 1
    elif status == 'A':
        att["absent"] += 1
    elif status == 'L':
        att["leave"] += 1
    else:
        print("Invalid status option.")
        return

    att["total"] += 1
    pct = (att["present"] / att["total"]) * 100

    print(f"\nStudent: {students[s_id]['info']['name']}")
    print(f"Total Days: {att['total']}")
    print(f"Present: {att['present']} | Absent: {att['absent']} | Leave: {att['leave']}")
    print(f"Attendance Percentage: {pct:.1f}%")

    if pct < 75.0:
        print("Warning: Student attendance is below 75%.")


def compute_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def enter_marks():
    print("\n--- MARKS AND GRADES ---")
    s_id = input("Enter Student ID: ").strip().upper()
    if s_id not in students:
        print("Student not found.")
        return

    student_marks = {}
    print("Enter marks for subjects (0 - 100):")

    for subj in subjects:
        while True:
            try:
                score = float(input(f"  {subj}: "))
                if 0 <= score <= 100:
                    student_marks[subj] = score
                    break
                else:
                    print("Invalid marks. Please enter marks between 0 and 100.")
            except ValueError:
                print("Please enter a numeric mark value.")

    total = sum(student_marks.values())
    percentage = (total / (len(subjects) * 100)) * 100
    grade = compute_grade(percentage)
    status = "PASS" if grade != "F" else "FAIL"

    students[s_id]["marks"] = student_marks
    students[s_id]["academic_summary"] = {
        "total_marks": total,
        "percentage": round(percentage, 2),
        "grade": grade,
        "status": status
    }

    print(f"\nMarks recorded for {students[s_id]['info']['name']}:")
    print(f"Total Marks: {total}/{len(subjects)*100} | Percentage: {percentage:.2f}% | Grade: {grade} | Status: {status}")


def manage_fees():
    print("\n--- FEE MANAGEMENT ---")
    s_id = input("Enter Student ID: ").strip().upper()
    if s_id not in students:
        print("Student not found.")
        return

    fee_dict = students[s_id]["fees"]

    try:
        monthly_fee = float(input("Enter Monthly Fee (Rs.): "))
        paid_amount = float(input("Enter Paid Amount (Rs.): "))
    except ValueError:
        print("Invalid fee input numbers.")
        return

    remaining = max(0.0, monthly_fee - paid_amount)
    status = "Paid" if remaining == 0 else "Pending"

    fee_dict["monthly_fee"] = monthly_fee
    fee_dict["paid_amount"] = paid_amount
    fee_dict["remaining"] = remaining
    fee_dict["status"] = status

    print(f"\nMonthly Fee: Rs. {monthly_fee:,.0f}")
    print(f"Paid Amount: Rs. {paid_amount:,.0f}")
    print(f"Remaining: Rs. {remaining:,.0f}")
    print(f"Status: {status}")


def search_student():
    print("\n--- SEARCH STUDENT ---")
    s_id = input("Enter Student ID to lookup: ").strip().upper()
    if s_id not in students:
        print(f"Student ID '{s_id}' not found.")
        return

    st = students[s_id]
    info = st["info"]
    att = st["attendance"]
    summary = st["academic_summary"]
    fees = st["fees"]

    print("\n==================================================")
    print(f" STUDENT PROFILE: {info['name']} ({s_id})")
    print("==================================================")
    print(f"Class & Sec : {info['class']} - {info['section']}")
    print(f"Age / Gender: {info['age']} / {info['gender']}")
    print(f"Father Name : {info['father_name']}")
    print(f"Contact     : {info['contact']}")
    print("-" * 50)
    
    print("ATTENDANCE SUMMARY:")
    if att["total"] > 0:
        pct = (att["present"] / att["total"]) * 100
        print(f"  Total: {att['total']} | Present: {att['present']} | Absent: {att['absent']} | Leave: {att['leave']}")
        print(f"  Percentage: {pct:.1f}%")
    else:
        print("  No attendance recorded.")

    print("-" * 50)
    print("MARKS & ACADEMIC RESULT:")
    if st["marks"]:
        for subj, mark in st["marks"].items():
            print(f"  {subj:<12}: {mark}")
        print(f"Percentage: {summary['percentage']}%")
        print(f"Grade: {summary['grade']}")
        print(f"Status: {summary['status']}")
    else:
        print("  No marks entered yet.")

    print("-" * 50)
    print("FEES STATUS:")
    print(f"Monthly Fee: Rs. {fees['monthly_fee']:,.0f}")
    print(f"Paid: Rs. {fees['paid_amount']:,.0f}")
    print(f"Remaining: Rs. {fees['remaining']:,.0f}")
    print(f"Status: {fees['status']}")
    print("==================================================")


def school_report():
    print("\n==================================================")
    print("              OVERALL SCHOOL REPORT               ")
    print("==================================================")
    print(f"Total Enrolled Students: {len(students)}")
    print(f"Total Faculty Members  : {len(teachers)}")
    
    if students:
        pass_count = sum(1 for s in students.values() if s["academic_summary"]["status"] == "PASS")
        fail_count = sum(1 for s in students.values() if s["academic_summary"]["status"] == "FAIL")
        print(f"Academic Performance   : {pass_count} Passed | {fail_count} Failed")
        
        total_pending_fees = sum(s["fees"]["remaining"] for s in students.values())
        print(f"Total Pending Fees     : Rs. {total_pending_fees:,.0f}")
    print("==================================================")


def main():
    while True:
        print("\n--------------------------------------------------")
        print("            SCHOOL MANAGEMENT SYSTEM              ")
        print("--------------------------------------------------")
        print("1. Student Management")
        print("2. Teacher Management")
        print("3. Attendance")
        print("4. Marks and Grades")
        print("5. Fee Management")
        print("6. Search Student")
        print("7. School Report")
        print("8. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_management_menu()
        elif choice == "2":
            teacher_management_menu()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            enter_marks()
        elif choice == "5":
            manage_fees()
        elif choice == "6":
            search_student()
        elif choice == "7":
            school_report()
        elif choice == "8":
            print("\nExiting School Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 8.")


if __name__ == "__main__":
    main()