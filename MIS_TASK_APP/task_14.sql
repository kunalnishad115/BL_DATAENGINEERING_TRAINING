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




