CREATE DATABASE HEALTHHISTORY;

CREATE TABLE HealthHistory(
HistoryID INT PRIMARY KEY,
HealthCondition VARCHAR(20) CHECK (HealthCondition IN ('Stable', 'Detriorating')),
Medication VARCHAR(100),
Immunization VARCHAR(100),
Allergies VARCHAR(100),
Injuries VARCHAR(100),
EmergencyContactNumber INT,
EmergencyContactName VARCHAR(25)
);

SELECT * FROM HealthHistory;
