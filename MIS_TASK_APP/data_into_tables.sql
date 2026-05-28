INSERT INTO patients(first_name,last_name,gender,age,email,phone,city)
VALUES
('Rahul','Sharma','Male',25,'rahul1@gmail.com','9876543210','Delhi'),
('Priya','Verma','Female',28,'priya2@gmail.com','9876543211','Mumbai'),
('Aman','Singh','Male',32,'aman3@gmail.com','9876543212','Pune'),
('Neha','Gupta','Female',24,'neha4@gmail.com','9876543213','Indore'),
('Rohit','Yadav','Male',30,'rohit5@gmail.com','9876543214','Bhopal'),
('Simran','Kaur','Female',27,'simran6@gmail.com','9876543215','Chandigarh'),
('Karan','Patel','Male',35,'karan7@gmail.com','9876543216','Ahmedabad'),
('Pooja','Mehta','Female',29,'pooja8@gmail.com','9876543217','Jaipur'),
('Vikas','Mishra','Male',40,'vikas9@gmail.com','9876543218','Lucknow'),
('Anjali','Joshi','Female',26,'anjali10@gmail.com','9876543219','Nagpur'),
('Deepak','Saini','Male',31,'deepak11@gmail.com','9876543220','Noida'),
('Ritika','Das','Female',22,'ritika12@gmail.com','9876543221','Kolkata'),
('Harsh','Agarwal','Male',34,'harsh13@gmail.com','9876543222','Surat'),
('Sneha','Rana','Female',23,'sneha14@gmail.com','9876543223','Patna'),
('Arjun','Nair','Male',29,'arjun15@gmail.com','9876543224','Kochi'),
('Meera','Iyer','Female',33,'meera16@gmail.com','9876543225','Chennai'),
('Nitin','Thakur','Male',38,'nitin17@gmail.com','9876543226','Shimla'),
('Kavya','Bansal','Female',21,'kavya18@gmail.com','9876543227','Kanpur'),
('Suresh','Pawar','Male',45,'suresh19@gmail.com','9876543228','Nashik'),
('Tina','Roy','Female',27,'tina20@gmail.com','9876543229','Hyderabad');

-- select * from patients;

INSERT INTO doctors(first_name,last_name,specialization,email,phone,experience_years)
VALUES
('Raj','Malhotra','Cardiologist','rajdoc1@gmail.com','9123456701',10),
('Pankaj','Sharma','Neurologist','pankajdoc2@gmail.com','9123456702',8),
('Meena','Verma','Dermatologist','meenadoc3@gmail.com','9123456703',6),
('Aditi','Kapoor','Pediatrician','aditidoc4@gmail.com','9123456704',7),
('Rakesh','Singh','Orthopedic','rakeshdoc5@gmail.com','9123456705',12),
('Sonia','Mehta','Gynecologist','soniadoc6@gmail.com','9123456706',9),
('Vivek','Joshi','ENT Specialist','vivekdoc7@gmail.com','9123456707',5),
('Ankit','Gupta','Psychiatrist','ankitdoc8@gmail.com','9123456708',11),
('Nisha','Rao','Oncologist','nishadoc9@gmail.com','9123456709',15),
('Tarun','Patel','General Physician','tarundoc10@gmail.com','9123456710',4);

-- select * from doctors;

INSERT INTO appointments
(patient_id,doctor_id,appointment_date,appointment_time,status)
VALUES
(1,1,'2026-05-01','10:00','Completed'),
(2,2,'2026-05-02','11:00','Scheduled'),
(3,3,'2026-05-03','12:00','Cancelled'),
(4,4,'2026-05-04','01:00','Completed'),
(5,5,'2026-05-05','02:00','Scheduled'),
(6,6,'2026-05-06','03:00','Completed'),
(7,7,'2026-05-07','04:00','Scheduled'),
(8,8,'2026-05-08','05:00','Completed'),
(9,9,'2026-05-09','06:00','Cancelled'),
(10,10,'2026-05-10','07:00','Completed'),

(11,1,'2026-05-11','10:30','Scheduled'),
(12,2,'2026-05-12','11:30','Completed'),
(13,3,'2026-05-13','12:30','Scheduled'),
(14,4,'2026-05-14','01:30','Completed'),
(15,5,'2026-05-15','02:30','Cancelled'),
(16,6,'2026-05-16','03:30','Completed'),
(17,7,'2026-05-17','04:30','Scheduled'),
(18,8,'2026-05-18','05:30','Completed'),
(19,9,'2026-05-19','06:30','Scheduled'),
(20,10,'2026-05-20','07:30','Completed'),

(1,2,'2026-05-21','09:00','Scheduled'),
(2,3,'2026-05-22','10:15','Completed'),
(3,4,'2026-05-23','11:15','Cancelled'),
(4,5,'2026-05-24','12:15','Completed'),
(5,6,'2026-05-25','01:15','Scheduled'),
(6,7,'2026-05-26','02:15','Completed'),
(7,8,'2026-05-27','03:15','Scheduled'),
(8,9,'2026-05-28','04:15','Completed'),
(9,10,'2026-05-29','05:15','Cancelled'),
(10,1,'2026-05-30','06:15','Completed');

-- select * from appointments;

INSERT INTO user_engagement
(patient_id,login_count,session_duration,last_login,device_type)
VALUES
(1,5,30,'2026-05-01 10:00','Mobile'),
(2,3,25,'2026-05-01 11:00','Laptop'),
(3,7,40,'2026-05-01 12:00','Tablet'),
(4,2,15,'2026-05-01 01:00','Mobile'),
(5,9,50,'2026-05-01 02:00','Desktop'),
(6,4,20,'2026-05-01 03:00','Laptop'),
(7,6,35,'2026-05-01 04:00','Mobile'),
(8,1,10,'2026-05-01 05:00','Tablet'),
(9,8,45,'2026-05-01 06:00','Desktop'),
(10,5,28,'2026-05-01 07:00','Mobile'),

(11,4,22,'2026-05-02 10:00','Laptop'),
(12,7,38,'2026-05-02 11:00','Mobile'),
(13,2,18,'2026-05-02 12:00','Tablet'),
(14,6,33,'2026-05-02 01:00','Desktop'),
(15,5,29,'2026-05-02 02:00','Mobile'),
(16,3,16,'2026-05-02 03:00','Laptop'),
(17,9,55,'2026-05-02 04:00','Desktop'),
(18,8,47,'2026-05-02 05:00','Tablet'),
(19,2,12,'2026-05-02 06:00','Mobile'),
(20,6,36,'2026-05-02 07:00','Laptop'),

(1,3,18,'2026-05-03 10:00','Mobile'),
(2,4,24,'2026-05-03 11:00','Desktop'),
(3,5,27,'2026-05-03 12:00','Tablet'),
(4,2,14,'2026-05-03 01:00','Laptop'),
(5,7,39,'2026-05-03 02:00','Mobile'),
(6,1,9,'2026-05-03 03:00','Desktop'),
(7,8,48,'2026-05-03 04:00','Tablet'),
(8,5,31,'2026-05-03 05:00','Laptop'),
(9,6,34,'2026-05-03 06:00','Mobile'),
(10,4,26,'2026-05-03 07:00','Desktop'),

(11,7,41,'2026-05-04 10:00','Tablet'),
(12,2,13,'2026-05-04 11:00','Laptop'),
(13,5,32,'2026-05-04 12:00','Mobile'),
(14,6,37,'2026-05-04 01:00','Desktop'),
(15,8,49,'2026-05-04 02:00','Tablet'),
(16,4,23,'2026-05-04 03:00','Laptop'),
(17,3,19,'2026-05-04 04:00','Mobile'),
(18,7,43,'2026-05-04 05:00','Desktop'),
(19,5,30,'2026-05-04 06:00','Tablet'),
(20,9,60,'2026-05-04 07:00','Laptop'),

(1,6,35,'2026-05-05 10:00','Mobile'),
(2,7,40,'2026-05-05 11:00','Desktop'),
(3,4,21,'2026-05-05 12:00','Tablet'),
(4,5,28,'2026-05-05 01:00','Laptop'),
(5,3,17,'2026-05-05 02:00','Mobile'),
(6,8,52,'2026-05-05 03:00','Desktop'),
(7,2,11,'2026-05-05 04:00','Tablet'),
(8,6,36,'2026-05-05 05:00','Laptop'),
(9,5,29,'2026-05-05 06:00','Mobile'),
(10,7,44,'2026-05-05 07:00','Desktop');

-- select * from user_engagement;