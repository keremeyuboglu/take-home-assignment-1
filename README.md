# Unplug Take Home Challenge

## Getting started - Docker
Just run API

### Prerequisites

You will need to install the following softwares:
1. Docker

### Run with Docker

Go to the root of the project and run these commands

- docker compose build
- docker compose up

## Getting started - Local - Debian
To additionally run tests

### Prerequisites

You will need to install the following softwares:
1. Python 3.11 +
2. Postgresql 15

### Run

Go to the root of the project and run these commands

- python -m venv venv
- source venv/bin/activate

Run the following code to install postgres and create db
- apt install postgresql
- psql -U postgres
- ALTER USER postgres PASSWORD 'postgres';
- \q

Change .env values according to your database config then
- python create_db.py
- pip install -r requirements-dev.txt
- flask run

To run tests 
- python -m pytest

### Postgres




### Notes

This api has created with following in mind:

- Added restaurant and menus to db. Also, created a default restaurant and menu. You may check the hiearchy in app/entites.py
- Deleting menu item means soft deletion.
- Updating menu item means changes in description, calorie etc. I've just made ranking attribute unique and didn't implement logic of changing all
the affected rows manipulation.
- API request and responses are in snake_case because sample_json was also in snake_case
- API docs with swagger UI in: http://localhost:5000/api/
- No gunicorn or uvicorn added