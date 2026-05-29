create view active_patients as
select p.patient_id, p.first_name,p.last_name from patients as p
join appointments as a
on a.patient_id=p.patient_id
where a.status='Completed';

select * from active_patients;


create view doctor_appointment_summary as
select p.patient_id, p.first_name as patient_f_name, p.last_name as patient_l_name,
    d.doctor_id,d.first_name as doc_f_name,d.last_name as doc_last_name,
	  a.appointment_date,a.status from patients as p
JOIN appointments AS a
ON a.patient_id = p.patient_id
JOIN doctors AS d
ON d.doctor_id = a.doctor_id;

select * from doctor_appointment_summary;


create view month_eng_report as
select p.patient_id, p.first_name, p.last_name,
       u.session_duration, u.last_login , u.device_type
from patients as p
join user_engagement as u
on p.patient_id=u.patient_id;

select * from month_eng_report;