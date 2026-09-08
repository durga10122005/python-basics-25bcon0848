def main():
    student = {
        "name": input("Enter student name: ").strip(),
        "roll_no": input("Enter roll number: ").strip(),
        "marks": float(input("Enter marks: ").strip()),
    }

    print("\n--- Student Details (Dictionary) ---")
    print(f"Name    : {student['name']}")
    print(f"Roll No : {student['roll_no']}")
    print(f"Marks   : {student['marks']}")


if __name__ == "__main__":
    main()
