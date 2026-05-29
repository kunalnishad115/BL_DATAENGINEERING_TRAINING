-- SUBQUERIES

select p.first_name, p.last_name from patients as p
join user_engagement as u
on u.patient_id=p.patient_id
where u.login_count=(select max(login_count) from user_engagement);

select p.patient_id,p.first_name,p.last_name from patients as p
join engagement_summary as e
on e.patient_id=p.patient_id
where e.avg_session_duration > (select avg(avg_session_duration) from engagement_summary);

SELECT d.doctor_id,d.first_name,d.last_name,
COUNT(a.appointment_id) AS total_appointments
FROM doctors AS d
JOIN appointments AS a
ON a.doctor_id = d.doctor_id
GROUP BY 
    d.doctor_id,
    d.first_name,
    d.last_name
HAVING COUNT(a.appointment_id) = (
SELECT MAX(appointment_count)
FROM (
SELECT COUNT(*) AS appointment_count
FROM appointments
GROUP BY doctor_id) AS max_table);


