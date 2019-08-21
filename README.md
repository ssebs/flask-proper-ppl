# ppl-proper

Proper Flask REST API implementation.

Includes Python Flask Package, SQLAlchemy ORM, Testing, venv, etc.

## Routes
- People
  - GET `/people/`
    - List all people
  - POST `/people/`
    - Create a person
  - GET `/people/:id`
    - Get a person
  - PUT `/people/:id`
    - Update a person
  - DELETE `/people/id`
    - Deactivate a person
- Auth (registration is done via POSTing a person)
  - POST `/login/`
    - Login via email / password
  - POST `/password-reset/`
    - Reset a password
  - POST `/refresh/`
    - Refresh JWT

## Install
- Install Python 3.6+
- Clone the repo / download code & cd to it
```
$ python3 -m venv env
$ . ./env/bin/activate
$ pip install -r requirements.txt
```

## Testing
- `$ python test_pplproper.py`

## Running
- First time?
  - Follow install instructions
  - `$ python init_db.py`
- Dev?
  - `$ python run.py`
- Production?
  - Install gunicorn, use `wsgi:app` as the app pkg & setup SSL/reverse proxy via nginx or apache, and setup a .service file for systemd
  - e.g.
    - `$ gunicorn wsgi:app`
