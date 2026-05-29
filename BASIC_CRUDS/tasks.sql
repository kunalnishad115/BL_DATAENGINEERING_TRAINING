select * from bank where salary=(select max(salary) from bank);

SELECT emp_id, fname , salary, 
CASE WHEN salary>=50000.00 THEN 'HIGH' 
ELSE 'LOW' 
END AS category_DATA 
from bank;



SELECT emp_id , fname,
CASE WHEN
salary >0 THEN round(salary*.10)
END AS bonus_table
FROM bank;


