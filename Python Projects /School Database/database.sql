CREATE TABLE  StudentsDatabase (
    IndexReference INT NOT NULL,
    StudentName VARCHAR(100) NOT NULL,
    PostCode VARCHAR(8) NOT NULL,
    Course VARCHAR(30) NOT NULL,
    Acheived VARCHAR(3) NOT NULL,
    Grade VARCHAR(2),
    PRIMARY KEY (IndexReference) 
)

CREATE TABLE  StaffDatabase (
    IndexReference INT NOT NULL,
    StaffName VARCHAR(100) NOT NULL,
    PostCode VARCHAR(8) NOT NULL,
    Course VARCHAR(30) NOT NULL,
    JobRole VARCHAR(30) NOT NULL,
    PRIMARY KEY (IndexReference) 
)

SELECT * FROM StudentsDatabase ORDER BY IndexReference ASC, StudentName;
SELECT * FROM StaffDatabase ORDER BY IndexReference ASC, StudentName ;