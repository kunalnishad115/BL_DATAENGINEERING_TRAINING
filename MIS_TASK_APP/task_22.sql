SELECT patient_id, first_name,last_name,age,gender,
      sum(age) OVER(PARTITION by gender ORDER by age) as SUM_WINDOW_FUN,
	  avg(age) OVER(PARTITION by gender ORDER by age) as avg_WINDOW_FUN,
	  count(age) OVER(PARTITION by gender ORDER by age) as count_WINDOW_FUN,
	  min(age) OVER(PARTITION by gender ORDER by age) as min_WINDOW_FUN,
	  max(age) OVER(PARTITION by gender order by age) as max_WINDOW_FUN
from patients;

select doctor_id,first_name,last_name,experience_years,specialization,
      rank() OVER(PARTITION by specialization ) as RANK_FUN,
	  dense_rank() OVER(partition by specialization) as DENSE_RANK_FUN,
	  percent_rank() OVER(partition by specialization) as PERCENT_RANK_FUN,
	  row_number() OVER(partition by specialization) as ROW_NUM_FUN from doctors;

select doctor_id,first_name,last_name,experience_years,
    first_value(experience_years)OVER(PARTITION by specialization ) as ANA_FIRST_VAL_FUN,
	  last_value(experience_years)OVER(partition by specialization) as ANA_LAST_FUN,
	  lead(experience_years) OVER(partition by specialization) as ANA_LEAD_FUN,
	  lag(experience_years) OVER(partition by specialization) as ANA_LAG_FUN from doctors;

WITH patient_cte AS
(
    SELECT *
    FROM patients
    WHERE age > 30
)

SELECT *
FROM patient_cte;

WITH RECURSIVE patient_numbers AS
(
    SELECT 1 AS num
    UNION ALL
    SELECT num + 1
    FROM patient_numbers
    WHERE num < 10
)

SELECT *
FROM patient_numbers;