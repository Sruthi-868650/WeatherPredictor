Airline Reservation System (Java Mini Project)
📖 Overview

The Airline Reservation System is a Core Java–based mini project designed to automate the process of flight booking, ticket management, and passenger record maintenance.
It provides a user-friendly interface for passengers to reserve seats on available flights and enables backend data management using MySQL and JDBC.

The project demonstrates the practical implementation of Object-Oriented Programming (OOP) concepts, exception handling, multithreading, client–server networking, and GUI programming using Swing.

🧩 Project Modules
Module	Concept	Description
1	Core Java Fundamentals	Handles flight and passenger creation, data initialization, and basic validation.
2	Exception Handling	Manages errors such as invalid flight IDs, unavailable seats, and duplicate bookings.
3	Multithreading & Generics	Simulates concurrent flight booking by multiple users simultaneously.
4	Networking & JDBC	Implements client–server communication and stores booking data into a MySQL database.
5	Java Swing GUI	Displays booking records and flight details dynamically with refresh functionality.
🧠 System Architecture
+------------------------+
|   User Interface (GUI) |
|     Java Swing App     |
+-----------+------------+
            |
            v
+------------------------+
|  Application Logic     |
|  (Core Java + OOP)     |
+-----------+------------+
            |
            v
+------------------------+
|  JDBC Connectivity     |
|  (SQL Transactions)    |
+-----------+------------+
            |
            v
+------------------------+
|  MySQL Database        |
|  (Flights, Passengers, |
|   Reservations Tables) |
+------------------------+

🧱 Database Schema
Database Name: airlinedb
1️⃣ Flights Table
Column	Type	Description
flight_id	INT (PK)	Unique flight identifier
flight_number	VARCHAR(10)	Flight code (e.g., AI202)
source	VARCHAR(50)	Departure city
destination	VARCHAR(50)	Arrival city
departure_time	DATETIME	Departure schedule
arrival_time	DATETIME	Arrival schedule
available_seats	INT	Remaining seats
2️⃣ Passengers Table
Column	Type	Description
passenger_id	INT (PK)	Unique passenger ID
first_name	VARCHAR(50)	Passenger first name
last_name	VARCHAR(50)	Passenger last name
email	VARCHAR(100)	Passenger email
phone	VARCHAR(15)	Passenger contact number
3️⃣ Reservations Table
Column	Type	Description
reservation_id	INT (PK)	Booking reference ID
flight_id	INT (FK)	References Flights table
passenger_id	INT (FK)	References Passengers table
seat_number	VARCHAR(10)	Booked seat
booking_date	DATETIME	Booking timestamp
status	VARCHAR(20)	Confirmed / Cancelled
⚙️ Technologies Used

Programming Language: Java (JDK 17+ recommended)

Database: MySQL

Database Connector: JDBC (MySQL Connector/J)

GUI Framework: Swing

IDE: NetBeans / Eclipse / IntelliJ IDEA

Version Control: Git & GitHub

🚀 How to Run the Project
🧰 Prerequisites

Install JDK (Java Development Kit)

Install MySQL Server & Workbench

Add the MySQL Connector/J jar file to your project’s classpath.

💾 Database Setup
CREATE DATABASE airlinedb;

USE airlinedb;

CREATE TABLE bookings (
  id INT AUTO_INCREMENT PRIMARY KEY,
  details VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

▶️ Steps to Execute

Clone or download the project folder.

Open the project in your preferred Java IDE.

Configure your MySQL username and password inside the code files (e.g., Module4.java, Module5.java).

Run each module sequentially to test individual functionalities.

Finally, execute Module5.java to launch the Swing GUI.

🧮 Key Features

✅ Flight creation and listing
✅ Passenger registration and validation
✅ Ticket booking and cancellation
✅ Multithreaded booking simulation
✅ Networking between client and server
✅ Real-time MySQL database integration
✅ Interactive Java Swing GUI for admins

📸 Screenshots (to be added)

System Architecture Diagram

Database Structure Diagram

Booking GUI Interface

MySQL Data Table View

🔐 Security Features

All SQL queries are handled using Prepared Statements to prevent SQL injection.

Each booking is uniquely identified by an auto-incremented ID.

Multi-user simulation ensures concurrent bookings are processed atomically.

🧭 Future Enhancements

Add authentication for different roles (Admin, Passenger).

Include online payment gateway simulation.

Implement seat map visualization for better seat selection.

Create web-based version using JavaFX or JSP/Servlets.

Deploy database to cloud (AWS RDS) for multi-branch airline scalability.

🧑‍💻 Authors

Developed by:
Team OOPs Lab – Department of Computer Science & Engineering
(Mini Project under Object-Oriented Programming Concepts)

📎 License

This project is developed for educational and academic purposes only under open-source learning license.
You may modify or reuse the code for study and demonstration with proper credits.
