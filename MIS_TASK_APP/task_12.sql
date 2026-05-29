create or replace PROCEDURE insert_appointment(p_patient_id INT,p_doctor_id INT,p_appointment_date DATE,p_appointment_time TIME,p_status VARCHAR(30))
LANGUAGE plpgsql
as $$
begin 
    if p_status not in ('Scheduled','Completed','Cancelled')
	then
	    raise exception 'invalid status';
	end if;
    insert into appointments( patient_id,doctor_id,appointment_date,appointment_time,status)
	values(p_patient_id,p_doctor_id,p_appointment_date,p_appointment_time,p_status);
end;
$$;
CALL insert_appointment(

    15,
    4,
    '2026-06-15',
    '11:30:00',
    'Scheduled'

);

SELECT * 
FROM appointments
ORDER BY appointment_id DESC;


CREATE OR REPLACE PROCEDURE update_patient_engagement(p_patient_id INT,p_login_count INT,p_session_duration INT,p_device_type VARCHAR(50))
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE user_engagement
    SET
        login_count = p_login_count,
        session_duration = p_session_duration,
        device_type = p_device_type,
        last_login = CURRENT_TIMESTAMP
    WHERE patient_id = p_patient_id;
END;
$$;

CALL update_patient_engagement(5,12,45,'Mobile');
SELECT *
FROM user_engagement
WHERE patient_id = 5;


CREATE OR REPLACE PROCEDURE delete_inactive_users()
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM user_engagement
    WHERE last_login < CURRENT_DATE - INTERVAL '30 days';
END;
$$;

CALL delete_inactive_users();

