import tkinter as tk
from tkinter import ttk

staff = {}
students = {}

# Dropdown Values 
courses_available = ["Biology", "Chemistry", "Maths", "English", "Geography", "History", "Physics", "Spanish"]
roles_available = ["Student", "Teacher"]

class School:
    def __init__(self, name, postcode, course):
        self.name = name
        self.postcode = postcode
        self.course = course

    def add_to_database(self):
        return f"{self.name}: {self.postcode}, {self.course}"

# Student Access Granted      
class Student(School):
    def __init__(self, name, postcode, course, grade):
        super().__init__(name, postcode, course)
        self.grade = grade
        students[self.name] = {
            "Postcode": self.postcode, 
            "Course" : self.course, 
            "Grade" : self.grade}
    
    def add_to_database(self):
        return f"{self.name}: Postcode: {self.postcode}, Course: {self.course}, Grade : {self.grade}"
    
    def update_details(self, field_name, value):
        if field_name.lower() == "postcode":
            self.postcode = value
            students[self.name]["Postcode"] = value
        elif field_name.lower() == "course":
            self.course = value
            students[self.name]["Course"] = value


# Staff Access Granted 
class Staff(School):
    def __init__(self, name, postcode, course, job):
        super().__init__(name, postcode, course)
        self.job = job
        index_ref = 0
        staff[self.name] = {
            "Indes Reference": index_ref,
            "Postcode": self.postcode, 
            "Course" : self.course, 
            "Job role" : job}

    def add_to_database(self):
        with open("teacher_database.txt", "r") as file_input, open("teacher_database.txt" "w") as file_output:
            content = file_input.readlines()
            if not content:
                print("Error: file is empty")
            else:
                for line in content:
                    # Removes unwanted white space for a cleaner output
                    line = line.strip().split(", ")
                    # Adds the fommatted string to the empty file
                    file_output.write(f"T{index_ref}" + line)
                    # Increments index reference
                    index_ref += 1
        return f"{self.name}: Role: {self.job}, Course: {self.course}, Postcode: {self.postcode}"
 
    def update_own_details(self, field_name, value):
        if field_name.lower() == "postcode":
            self.postcode = value
            staff[self.name]["Postcode"] = value
        elif field_name.lower() == "course":
            self.course = value
            staff[self.name]["Course"] = value
        
    def update_student_details(self, name, field_name, value):
        if field_name.lower() == "postcode":
            name.postcode = value
            students[name]["Postcode"] = value
        elif field_name.lower() == "course":
            name.course = value
            students[name]["Course"] = value

    def view_student_database(self):
        for name, details in students.items():
            print(f"Name: {name}")
            for field, value in details.items():
                print(f"{field}: {value}")
            print("\n")

    def view_staff_database(self):
        for name, details in staff.items():
            print(f"Name: {name}")
            for field, value in details.items():
                print(f"{field}: {value}")
            print("\n")

class LoginGUI:
    def __init__(self, root):
        self.root = root

        self.root.title("School Database")
        self.root.geometry("500x400")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text = "Log in", bg="#693efe", fg= "white", width=100, pady=7, font=("Arial", 17)).pack()

        # Name Field
        self.name_var = tk.StringVar()
        tk.Label(self.root, text = "Name:").pack(pady=5)
        tk.Entry(self.root, textvariable= self.name_var).pack()
        
        # Postcode Field
        self.postcode_var = tk.StringVar()
        tk.Label(self.root, text = "Postcode:").pack(pady=5)
        tk.Entry(self.root, textvariable= self.postcode_var).pack()

        # Course Field
        self.course_var = tk.StringVar()
        tk.Label(self.root, text = "Course:").pack(pady=5)
        ttk.Combobox(self.root, textvariable= self.course_var, values=courses_available, state="readonly").pack()

        # Idetifies what dictionary to input the details
        self.status_var = tk.StringVar()
        tk.Label(self.root, text = "Role").pack(pady=5)
        ttk.Combobox(self.root, textvariable= self.status_var, values=roles_available, state="readonly").pack()

        tk.Button(self.root, text = "Add to Database", padx= 10, command= self.validate).pack(pady=5)
    
    # Validates User Input
    def validate(self):
        # Converting the object to strings for validation
        name = self.name_var.get()
        postcode = self.postcode_var.get()
        course = self.course_var.get()
        status = self.status_var.get()

        name_valid, postcode_valid, course_valid, role_valid = False

        # Destroys Label if exists to prevent label stacking
        if hasattr(self, 'name_error'):
            self.name_error.destroy()
        if hasattr(self, 'postcode_error'):
            self.postcode_error.destroy()
        if hasattr(self, 'course_error'):
            self.course_error.destroy()
        if hasattr(self, 'role_error'):
            self.role_error.destroy()

        # Name Validation
        if name.strip() == "":
            self.name_error = tk.Label(text= "Error: Name cannot be empty", fg= "red")
            self.name_error.pack()
        elif not name.isalpha():
            self.name_error = tk.Label(text= "Error: Name must only contain letters")
            self.name_error.pack()
        elif len(name) < 6:
            self.name_error = tk.Label(text= "Error: Name must be at least 6 characters long.")
            self.name_error.pack()
        else:
            name_valid = True 
            name = name.capitalize()
        
        # Postcode Validation
        if postcode.strip() == "":
            self.postcode_error = tk.Label(text= "Error: Postcode cannot be empty", fg = "red")
            self.postcode_error.pack()
        elif not postcode.isalnum():
            self.postcode_error = tk.Label(text= "Error: Postcode can only contain letters and numbers", fg= "red")
            self.postcode_error.pack()
        elif len(postcode) < 5:
            self.postcode_errortk.Label(text = "Error: Postcode must be at least 5 characters long", fg= "red")
            self.postcode_error.pack()
        elif len(postcode) > 7:
            self.postcode_error = tk.Label(text= "Error: Postcode must be no more than 7 characters long", fg= "red")
            self.postcode_error.pack()
        else:
            postcode_valid = True
            postcode = postcode.upper()

        # Course Validation
        if course.strip() == "":
            self.course_error = tk.Label(text= "Error: Course cannot be empty", fg = "red")
            self.course_error.pack()
        else:
            course_valid = True
            course = course.capitalize()

        # Student or Staff Validation
        if status.strip() == "":
            self.role_error = tk.Label(text= "Error: Student or Staff cannot be empty", fg = "red")
            self.role_error.pack()
        else:
            course_valid = True
            status = status.capitalize()

        #Adding to the database
        if status.lower() == "student":
            with open("Python Projects /School Database/student_database.txt", "a") as file_output:
                student_object = Student(name, postcode, course, "N/A")
                file_output.write(student_object.add_to_database())

        elif status.lower() == "teacher":
            with open("Python Projects /School Database/teacher_database.txt", "a") as file_output:
                staff_object = Staff(name, postcode, course, status)
                file_output.write(staff_object.add_to_database())

        if all (valid == True for valid in (name_valid, postcode_valid, course_valid, role_valid)) :
            # Ensuring all fields are empty
            self.name_var.set("")
            self.postcode_var.set("")
            self.course_var.set("")
    
if __name__ == "__main__":
    root = tk.Tk()
    my_app = LoginGUI(root)
    root.mainloop()


