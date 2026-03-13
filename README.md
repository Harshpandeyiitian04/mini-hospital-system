Mini Hospital Management System (HMS)
Overview

This project is a Mini Hospital Management System (HMS) that allows doctors to manage their availability and patients to book appointments online.

The system supports doctor scheduling, patient appointment booking, Google Calendar integration, and email notifications through a serverless microservice.

This project demonstrates backend development using Django, PostgreSQL, serverless architecture, and external API integrations.

Features
User Authentication

Doctor and Patient sign-up

Secure login using Django authentication

Password hashing for security

Role-based access control

Doctor Features

Doctor dashboard

Create and manage availability slots

View booked appointments

Patient Features

View available doctors

View available time slots

Book appointments

Appointment Management

Prevents double booking

Uses database transactions to avoid race conditions

Google Calendar Integration

Automatically creates an event in Google Calendar when an appointment is booked.

Email Notifications

Email notifications are sent using a serverless email service.

Emails sent:

Welcome email on signup

Appointment confirmation email on booking

Tech Stack

Backend Framework

Django

Database

PostgreSQL

Authentication

Django built-in authentication system

Serverless Email Service

Serverless Framework

AWS Lambda (simulated locally)

Email Delivery

Gmail SMTP

External API Integration

Google Calendar API

Local Development Tools

serverless-offline

Project Architecture
Browser
   ↓
Django Web Application
   ↓
PostgreSQL Database
   ↓
Google Calendar API
   ↓
Serverless Email Microservice
   ↓
SMTP (Gmail)
Project Structure
mini-hospital-system
│
├── hms_backend
│   ├── users
│   ├── doctors
│   ├── appointments
│   ├── templates
│   └── manage.py
│
├── email_service
│   ├── handler.py
│   ├── serverless.yml
│
├── requirements.txt
└── README.md
Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/mini-hospital-management-system.git
cd mini-hospital-management-system
2. Setup Python Environment
python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
3. Setup PostgreSQL Database

Create a PostgreSQL database.

Update settings.py with your database credentials.

Run migrations:

python manage.py migrate

Create admin user:

python manage.py createsuperuser
4. Run Django Server
python manage.py runserver

Application runs at:

http://127.0.0.1:8000
Running the Email Microservice

Navigate to email service folder:

cd email_service

Install serverless framework if needed:

npm install -g serverless

Install serverless-offline plugin:

npm install serverless-offline

Start serverless service:

serverless offline

Email endpoint:

POST http://localhost:3000/dev/send-email
Demo Flow

Doctor signs up and logs in

Doctor creates availability slots

Patient signs up and logs in

Patient views doctors and available slots

Patient books an appointment

Appointment confirmation email is sent

Google Calendar event is created

Key Learning Outcomes

This project demonstrates:

Backend development with Django

Database design with PostgreSQL

Role-based authentication

Handling concurrency using database transactions

Integration with external APIs

Serverless microservice architecture

Email notification systems

Future Improvements

Add REST API using Django REST Framework

Add frontend using React

Implement payment integration

Add appointment cancellation

Improve UI design

Author

Harsh Pandey

Computer Science Student
Web Development & Backend Development Enthusiast

License

This project is created for educational 