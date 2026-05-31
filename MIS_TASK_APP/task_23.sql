CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    
    CHECK (
        email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    )
);

CREATE TABLE patients(
    patient_id SERIAL PRIMARY KEY,
    phone VARCHAR(10),

    CHECK(
        phone ~ '^[0-9]{10}$'
    )
);

CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE user_sessions(
    session_id SERIAL PRIMARY KEY,
    login_time TIMESTAMP,
    logout_time TIMESTAMP
);

