create or replace function total_login_cnt(p_patient_id int)
returns int
as $$
declare
     total_cnt int;
begin
     select login_count
	 into total_cnt
	 from user_engagement
	 where patient_id=p_patient_id;
	 return total_cnt;
end;
$$ language plpgsql;

select total_login_cnt(2);

create or replace function doc_cnt(d_doctor_id int)
returns int
as $$
declare
     total_cnt int;
begin
     select count(*) 
	 into total_cnt
	 from appointments
	 where doctor_id=d_doctor_id;
	 return total_cnt;
end;
$$ language plpgsql;

select doc_cnt(2);

create or replace function avg_eng_duration(p_patient_id int)
returns int
as $$
declare
     avg_duration int;
begin
     select avg_session_duration
	 into avg_duration
	 from engagement_summary
	 where patient_id=p_patient_id;
	 return avg_duration;
end;
$$ language plpgsql;

select avg_eng_duration(1);


