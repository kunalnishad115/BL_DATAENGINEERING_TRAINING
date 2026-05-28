CREATE TABLE bank(
    emp_id SERIAL PRIMARY KEY,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE DEFAULT 'None',
    dept VARCHAR(100),
    salary DECIMAL(10,2) DEFAULT 30000,
    hire_date DATE
);

INSERT INTO bank(fname,lname,email,dept,salary,hire_date)
VALUES
('Kunal','Nishad','kunal@gmail.com','IT',50000,'2026-01-10'),
('Rahul','Sharma','rahul@gmail.com','HR',45000,'2025-05-11'),
('Aman','Verma','aman@gmail.com','Finance',60000,'2024-08-15'),
('Priya','Singh','priya@gmail.com','IT',70000,'2023-03-20'),
('Neha','Gupta','neha@gmail.com','Sales',40000,'2022-07-18');

SELECT * FROM bank;

UPDATE bank
SET salary = 80000
WHERE emp_id = 1;

-- DELETE FROM bank
-- WHERE emp_id=5;

