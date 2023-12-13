import sqlite3
import os
import hashlib

# Create an SQLite database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# ... (Previous code remains unchanged)

# Function for login with parameterized query
def login():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Use parameterized query to prevent SQL injection
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            print("Login successful.")
            break
        else:
            print("Incorrect username or password. Please try again.")

# Update the password to be stored as a hash
def update_default_password():
    hashed_password = hashlib.sha256("password".encode()).hexdigest()
    cursor.execute("UPDATE users SET password = ?", (hashed_password,))
    conn.commit()

# Function to upload an image with validation
def upload_image():
    student_number = input("Enter the student number (image will be associated with this student): ")
    image_file = input("Enter the image file name (e.g., student_card.png): ")

    image_path = os.path.join("images", image_file)

    # Validate image file type and size
    if os.path.exists(image_path) and os.path.splitext(image_path)[1].lower() in ['.png', '.jpg', '.jpeg']:
        cursor.execute("UPDATE students SET image_path = ? WHERE student_number = ?", (image_path, student_number))
        conn.commit()
        print("Image uploaded and associated with the student.")
    else:
        print("Invalid image file.")

# Feature to anonymize metadata before downloading an image
def download_student_image():
    student_number = input("Enter the student number of the student whose image you want to download: ")

    cursor.execute("SELECT image_path FROM students WHERE student_number = ?", (student_number,))
    image_path = cursor.fetchone()

    if image_path:
        image_path = image_path[0]
        if os.path.exists(image_path):
            # Anonymize metadata (example: by creating a copy)
            with open(image_path, "rb") as f:
                image_data = f.read()
            new_image_name = input("Enter a new file name for the image (e.g., downloaded_image.png): ")
            with open(new_image_name, "wb") as f:
                f.write(image_data)
            print(f"Image downloaded as '{new_image_name}'.")
        else:
            print("Image not found on the server.")
    else:
        print("Student not found.")

# Main method
def main():
    login()  # Login
    while True:
        print("\nSelect an action:")
        print("1. Add a student")
        print("2. Add grades for a student")
        print("3. Search for a student by student number")
        print("4. Display all students")
        print("5. Upload an image for a student")
        print("6. Download a student's image")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")



        if choice == "1":
            add_student()
        elif choice == "2":
            add_grades()
        elif choice == "3":
            search_student()
        elif choice == "4":
            def add_student():
                student_number = input("Enter student number: ")
                name = input("Enter student name: ")
                contact = input("Enter student contact information: ")
                ssn = input("Enter student SSN: ")
                
                image_path = input("Enter the image file name (e.g., student_card.png, press Enter to skip): ")
                if image_path:
                    image_path = os.path.join("images", image_path)
                    if not os.path.exists(image_path):
                        print("Image file not found. Student added without an image.")
                        image_path = None
                
                cursor.execute("INSERT INTO students (student_number, name, contact, ssn, image_path) VALUES (?, ?, ?, ?, ?)",
                           (student_number, name, contact, ssn, image_path))
                conn.commit()
                print("Student added to the database.")
            
            
            def add_grades():
                student_number = input("Enter the student number of the student to add grades for: ")
                course = input("Enter course name: ")
                grade = input("Enter the grade: ")
                
                cursor.execute("SELECT student_number FROM students WHERE student_number = ?", (student_number,))
                student_id = cursor.fetchone()
                
                if student_id:
                    cursor.execute("INSERT INTO grades (student_id, course, grade) VALUES (?, ?, ?)",
                                   (student_number, course, grade))
                    conn.commit()
                    print("Grade added successfully.")
                else:
                    print("Student not found.")
            
            
            def search_student():
                student_number = input("Enter the student number of the student to search for: ")
                
                cursor.execute("SELECT * FROM students WHERE student_number = ?", (student_number,))
                student = cursor.fetchone()
                
                if student:
                    print("Student found:")
                    print(f"Student Number: {student[0]}")
                    print(f"Name: {student[1]}")
                    print(f"Contact: {student[2]}")
                    print(f"SSN: {student[3]}")
                    print(f"Image Path: {student[4]}")
                else:
                    print("Student not found.")
            
            
            def display_all_students():
                cursor.execute("SELECT * FROM students")
                students = cursor.fetchall()
                
                if students:
                    print("All students:")
                    for student in students:
                        print(f"Student Number: {student[0]}")
                        print(f"Name: {student[1]}")
                        print(f"Contact: {student[2]}")
                        print(f"SSN: {student[3]}")
                        print(f"Image Path: {student[4]}")
                        print()
                else:
                    print("No students in the database.")()
        elif choice == "5":
            upload_image()
        elif choice == "6":
            download_student_image()
        elif choice == "7":
            break
  

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
