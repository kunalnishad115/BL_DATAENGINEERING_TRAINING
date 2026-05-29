select p.patient_id , p.first_name as pat_name , d.first_name as doc_name , d.specialization , a.appointment_date ,a.status
from appointments as a
inner join patients as p
on p.patient_id=a.patient_id
inner join doctors as d
on d.doctor_id=a.doctor_id

select p.patient_id , p.first_name as pat_name , d.first_name as doc_name , d.specialization , a.appointment_date ,a.status
from appointments as a
left join patients as p
on p.patient_id=a.patient_id
left join doctors as d
on d.doctor_id=a.doctor_id


select p.patient_id, p.first_name, p.last_name , p.city
from patients as p
left join appointments as a
on a.patient_id=p.patient_id
where a.appointment_id is null;