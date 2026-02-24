create database GYMSTAFF;

CREATE TABLE Staff(
EmployeeID INT PRIMARY KEY,
EmployeeFirstName VARCHAR(10),
EmployeeLastName VARCHAR(10),
EmployeeUsername VARCHAR(20),
EmployeePassword VARCHAR(20),
EmployeeDesignation VARCHAR(20),
EmployeeConatct INT,
EmployeeDateofBirth DATE,
EmployeeJoiningDate DATE,
EmployeeGender VARCHAR(6) CHECK (EmployeeGender IN ('Male', 'Female'))
);
SELECT * FROM Staff;