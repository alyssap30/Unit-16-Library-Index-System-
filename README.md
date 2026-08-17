## Summary of the Problem 

The college library has asked me to create a library index system to store all of their books. The application will automatically read the book details which includes its title, author, publisher and publication date which will be found in a stored file. An index reference would then be created and stored in a new file containing all the fetched details. I chose to use Python's built in file handling over the csv build-in library as the book_storage.txt file uses a comma-space to determine the string split making string manipulation methods such as “strip().split()” effective to use in that case. 

This program’s required interactivity requires the program lines to be processed one by one to be split, remove any whitespace and validates to be encapsulated as a book object. The local counter variable is incremented after each iteration of the line of the input file to ensure accurate index references and error handling is used to identify missing records and empty input files to prevent the file from running with errors which would cause the output file to be inaccurate. 

This program required the implementation of a batch processing model where the entire input file is processed in a single sequin tail execution with no user interaction during execution of the programming instead the GUI is driven by GUI callbacks. This architecture is appropriate for the library system as the input file is fixed during execution and the output is determined  using the file contents making iterative processing unnecessary and not resource effective.

The process uses a Read-Format-Write approach pattern where the input file is opened in read mode and each line is converted into a string to be formatted without whitespace and split into a list. The line list is then encapsulated into a “Book Object” and the object's formatted string is then written to the output file. I have chosen to make each stage isolated to allow for independent modification following the Single Responsibility Principle. 

## Intended Users

The target audience of the Library Book System is the college IT staff which will use this application to store all their books in an index database. This means I am required to create a functional design with an intuitive design and contains simple commands to ensure ease of use. 

## Use Case Summary

<img width="193" height="195" alt="Screenshot 2026-08-17 at 16 39 43" src="https://github.com/user-attachments/assets/e1898c32-4549-4fbf-8bae-6913b711057a" />

## Flowchart 

<img width="402" height="474" alt="Screenshot 2026-08-17 at 16 40 14" src="https://github.com/user-attachments/assets/a2f6485c-84f3-4ddb-9355-dbc37c203737" />

## Sequence Diagram 

<img width="722" height="300" alt="Screenshot 2026-08-17 at 16 40 58" src="https://github.com/user-attachments/assets/aefbd296-3bfe-48ca-ac29-9068bd32f4e3" />

## Activity Diagram

<img width="411" height="623" alt="Screenshot 2026-08-17 at 16 41 35" src="https://github.com/user-attachments/assets/afa88090-c1b7-4bf5-ae7c-29257624f9f2" />

## Test Plan 

<img width="721" height="584" alt="Screenshot 2026-08-17 at 16 42 23" src="https://github.com/user-attachments/assets/86df0610-7197-4092-84ff-9e4a5458d878" />
<img width="720" height="136" alt="Screenshot 2026-08-17 at 16 43 11" src="https://github.com/user-attachments/assets/b23f7632-892b-4dc7-8d39-0332cb6ed11e" />




