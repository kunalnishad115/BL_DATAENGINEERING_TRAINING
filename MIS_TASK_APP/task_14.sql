create or replace function update_eng_summary()
returns trigger
as $$
begin 
     update engagement_summary
	 set
	  total_sessions=total_sessions+1,
		avg_session_duration=(
             select avg(session_duration)
			 from user_engagement
			 where patient_id=NEW.patient_id
		)
	where patient_id=NEW.patient_id;
	return NEW;
end;
$$ language plpgsql;

create trigger trg_update_eng_summary
after insert 
on user_engagement
for each row
execute function update_eng_summary();

INSERT INTO user_engagement(
    patient_id,
    login_count,
    session_duration
)
VALUES(
    5,
    10,
    40
);


create table appointments_logs(
 log_id serial primary key,
 appointment_id int,
 patient_id int,
 doctor_id int,
 appointment_date date ,
 appointment_time time,
 status varchar(30),
 created_at TIMESTAMP,
 deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create or replace function log_deleted_appointment()
returns trigger
as $$
begin
     insert into appointments_logs(
         appointment_id,
		 patient_id,
		 doctor_id,
		 appointment_date,
		 appointment_time,
		 status,
		 created_at
	 )values(
         OLD.appointment_id,OLD.patient_id,
		 OLD.doctor_id,OLD.appointment_date,
		 OLD.appointment_time,OLD.status,OLD.created_at
	 );
	 return OLD;
end;
$$ language plpgsql;

create trigger trg_log_deleted_appointment
before delete
on appointments
for each row
execute function log_deleted_appointment();

DELETE FROM appointments
WHERE appointment_id = 5;

select * from appointments_logs;







