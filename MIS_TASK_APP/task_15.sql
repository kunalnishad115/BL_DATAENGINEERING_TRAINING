create index patient_name on patients(first_name,last_name);
select * from pg_indexes where tablename='patients';

create index idx_doctor_name on doctors(first_name,last_name);
select * from pg_indexes where tablename='doctors';

create index idx_appointments on appointments(appointment_date);
select * from pg_indexes where tablename='appointments';

