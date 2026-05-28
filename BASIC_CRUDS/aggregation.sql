SELECT COUNT(emp_id) FROM bank;
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT MAX(salary) FROM employees;

SELECT dept, SUM(salary)
FROM employees
GROUP BY dept;

SELECT dept, COUNT(*)
FROM employees
GROUP BY dept;

