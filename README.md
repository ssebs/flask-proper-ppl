# ppl-proper

Proper Flask REST API implementation, for use in production.

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
- Auth
  - POST `/login/`
    - Login via email / password
  - POST `/password-reset/`
    - Reset a password
  - POST `/register/`
    - Register for a new account
  - POST `/refresh/`
    - Refresh JWT
