COPY patients
TO 'C:\postgres_data\patients.csv'
DELIMITER ','
CSV HEADER;

COPY patients(
    patient_id,
    first_name,
    last_name,
    age,
    city
)
FROM 'C:\postgres_data\patients.csv'
DELIMITER ','
CSV HEADER;
