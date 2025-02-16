Tweet-Project

Tweet-Project is a Django-based web application that allows users to view, create, update, and delete tweets. Users can also search for specific tweets.

Features

User authentication (Login & Signup)

Create, read, update, and delete tweets

View tweets from different users

Search functionality to find specific tweets

Installation

Prerequisites

Ensure you have the following installed:

Python (>=3.x)

Django (>=4.x)

Virtual environment (optional but recommended)

Setup

Clone the repository

git clone https://github.com/ashvin-007/Tweet-Project.git


Create and activate a virtual environment (optional but recommended)

python -m venv virt  

venv\Scripts\activate  



Run database migrations

python manage.py migrate

Create a superuser (for admin access)

python manage.py createsuperuser

Follow the prompts to set up the admin credentials.

Run the development server

python manage.py runserver

The project will be available at http://127.0.0.1:8000/

Usage

Sign up and log in to your account.

Post new tweets.

View tweets from other users.

Update or delete your own tweets.

Search for specific tweets using the search bar.

Technologies Used

Backend: Django, 

Database: SQLite (default, can be replaced with PostgreSQL/MySQL)

Frontend: HTML, CSS, JavaScript (if applicable)

Contributing

Contributions are welcome! Feel free to fork the repository and create a pull request with improvements.


Author

[Ashvin Parmar] - Created by @ashvin-007

