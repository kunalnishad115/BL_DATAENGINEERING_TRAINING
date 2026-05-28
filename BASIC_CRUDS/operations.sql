SELECT fname,salary FROM bank;

SELECT * FROM bank
WHERE dept='IT';

SELECT * FROM bank
WHERE salary > 50000;

SELECT * FROM bank
WHERE fname LIKE 'K%';

SELECT * FROM bank
WHERE dept IN ('IT','HR');

SELECT * FROM bank
WHERE salary BETWEEN 40000 AND 70000;

SELECT * FROM bank
ORDER BY salary ASC;

SELECT * FROM bank 
WHERE dept LIKE '__'



