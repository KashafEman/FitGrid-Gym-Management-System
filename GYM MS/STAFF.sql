create database staff;
use staff;


CREATE TABLE Staff(
EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
EmployeeFirstName VARCHAR(10),
EmployeeLastName VARCHAR(10),
EmployeeUsername VARCHAR(20),
EmployeePassword VARCHAR(20),
EmployeeDesignation VARCHAR(20) CHECK(EmployeeDesignation IN('Trainer','Functional','Non-Functional')),
EmployeeConatct BIGINT,
EmployeeDateofBirth DATE,
EmployeeJoiningDate DATE,
EmployeeGender VARCHAR(6) CHECK (EmployeeGender IN ('Male', 'Female'))
);

select *from Staff;