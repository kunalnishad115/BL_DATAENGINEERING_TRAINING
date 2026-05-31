SELECT
    DATE(last_login) AS engagement_date,
    COUNT(patient_id) AS total_patients,
    SUM(login_count) AS total_logins,
    AVG(session_duration) AS avg_session_duration
FROM user_engagement
GROUP BY DATE(last_login)
ORDER BY engagement_date;


SELECT
    d.doctor_id,
    d.first_name,
    d.last_name,
    DATE_TRUNC('month', a.appointment_date) AS month,
    COUNT(a.appointment_id) AS total_consultations
FROM doctors AS d
JOIN appointments AS a
ON d.doctor_id = a.doctor_id
GROUP BY
    d.doctor_id,
    d.first_name,
    d.last_name,
    DATE_TRUNC('month', a.appointment_date)
ORDER BY month;

SELECT
    p.patient_id,
    p.first_name,
    p.last_name,
    SUM(u.login_count) AS total_logins,
    AVG(u.session_duration) AS avg_session_duration
FROM patients AS p
JOIN user_engagement AS u
ON p.patient_id = u.patient_id
GROUP BY
    p.patient_id,
    p.first_name,
    p.last_name
ORDER BY total_logins DESC;

SELECT
    d.doctor_id,
    d.first_name,
    d.last_name,
    COUNT(a.appointment_id) AS total_appointments
FROM doctors AS d
JOIN appointments AS a
ON d.doctor_id = a.doctor_id
GROUP BY
    d.doctor_id,
    d.first_name,
    d.last_name
ORDER BY total_appointments DESC;

SELECT
    status,
    COUNT(*) AS total_appointments
FROM appointments
GROUP BY status
ORDER BY total_appointments DESC;

