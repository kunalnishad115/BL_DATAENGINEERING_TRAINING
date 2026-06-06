ALTER TABLE patients
ADD COLUMN blood_group VARCHAR(5);

ALTER TABLE patients
RENAME COLUMN phone TO mobile_number;

DROP TABLE engagement_summary;

TRUNCATE TABLE user_engagement;

UPDATE patients
SET city = 'Bangalore'
WHERE patient_id = 1;


DELETE FROM appointments
WHERE status = 'Cancelled';

INSERT INTO user_engagement
(patient_id, login_count, session_duration, last_login, device_type)
VALUES
(3, 5, 35, CURRENT_TIMESTAMP, 'Mobile'),
(7, 2, 20, CURRENT_TIMESTAMP, 'Laptop'),
(10, 8, 50, CURRENT_TIMESTAMP, 'Tablet');

GRANT SELECT
ON patients
TO reporting_user;

REVOKE DELETE
ON appointments
FROM reporting_user;



