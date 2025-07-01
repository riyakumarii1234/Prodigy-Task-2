Prodigy Infotech Task 2 – Persistent Storage with Database Integration
Project Overview
This project is a Flask REST API integrated with a MySQL database for persistent storage. It allows anyone to add users via a web form or API, and view all users as JSON or in an HTML table.

Features
User CRUD operations via REST API
MySQL database integration using SQLAlchemy ORM
Database migrations with Flask-Migrate
Environment variables for configuration
Connection pooling support
Add users via web form (no authentication required)
View users as JSON or in an HTML table
Setup Instructions
Clone the repository and navigate to the project folder.

Install dependencies:

pip install -r requirements.txt
Set up your .env file (create one if it doesn't exist):

DATABASE_URL=mysql://root:yourpassword@localhost:3306/prodigy_db
SECRET_KEY=dev
POOL_SIZE=5
MAX_OVERFLOW=10
Replace yourpassword with your actual MySQL root password.

Create the MySQL database:

CREATE DATABASE prodigy_db;
Run migrations:

flask db migrate -m "init"
flask db upgrade
Start the app:

python app.py
Usage
Add a user via web form:
http://127.0.0.1:5000/add_user

View all users (HTML table):
http://127.0.0.1:5000/list_users

View all users (JSON API):
http://127.0.0.1:5000/api/users

Add a user via API (POST):

POST http://127.0.0.1:5000/api/users
Content-Type: application/json
{
  "username": "testuser",
  "email": "test@example.com"
}
Notes
Anyone can add users; there is no authentication.
Make sure your MySQL server is running and accessible.
For any issues, check your terminal for error messages or contact the project author.
