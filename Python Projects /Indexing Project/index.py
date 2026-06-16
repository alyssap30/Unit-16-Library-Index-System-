import tkinter as tk
from tkinter import ttk

class Book:
   def __init__(self, file_name, indexReference):
       self.filename = file_name
       self.index_reference = f"prog{indexReference:02d}"
       self.book_title = file_name[0]
       self.book_author = file_name[1]
       self.publisher = file_name[2]
       self.publication_date = file_name[3]
   def get_book_details(self):
       # String manipulation for the required format
       return f"{self.index_reference}: {self.book_title}, {self.book_author}, {self.publisher}, {self.publication_date}"

def read_file(file):
    counter = 1
    try:
        # Reads the contents of the file line by line
        with open(file, "r") as file_input, open("Python Projects /Indexing Project/formated_book_storage.txt", "a") as file_output:
            # Checks if file is not empty
            content = file_input.readlines()
            if not content:
                print("Error: file is empty")
            else:
                for line in content:
                    # Removes unwanted white space for a cleaner output
                    line = line.strip().split(", ")
                    book_object = Book(line, counter)
                    # Adds the fommatted string to the empty file
                    file_output.write(book_object.get_book_details() + "\n")
                    # Increments index reference
                    counter += 1
    # Error handling
    except IndexError:
        print("Error: Missing value")
    except Exception as e:
        print(f"Error: {e}")

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Entry")
        self.root.geometry("400x400")
    
    def create_widgets(self):
        input_choice_inp = ttk.Combobox(self.root, values=['File input', 'Manual input'], state='readonly')
        input_choice_inp.pack()

        tk.Button(self.root, text= "Submit")
        self.input_choice = input_choice_inp.get()
    def validate_user_inp(self):
        if self.input_choice == "File input":
            # Calls function for declared file
            read_file("Python Projects /Indexing Project/book_storage.txt")


    def file_input_widgets(self):
        pass
    def manual_input_widgets(self):
        pass
        

if __name__ == "__main__":
    root = tk.Tk()
    my_app = GUI(root)
    root.mainloop()
