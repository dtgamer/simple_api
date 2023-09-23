# Django API Project README

This Django project implements a simple API for user management, allowing you to create and retrieve user records.

## Prerequisites

Before getting started, make sure you have the following installed on your system:

- Python (3.6+)
- Django
- Django Rest Framework (DRF)
- Postman (optional, for testing)

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/DT-GAMER/simple_api.git
  
2. Create a virtual environment (optional but recommended):

```   
python -m venv venv (for Linux and MacOS)
```
```
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install project dependencies:
```
pip install -r requirements.txt
```

4. Perform database migrations:
```
python manage.py makemigrations
python manage.py migrate
```
5. Start the development server:
```
 python manage.py runserver
```
 Your API should be accessible at http://localhost:8000/api/.

#API Endpoints

1. Create User (POST)

    URL: /api/user/

    Method: POST

    Request Body:

    json
```
{
    "name": "John Terry",
    "email": "johnt92@gmail.com",
    "password": "shuush_it's_secret"
}
```
Response:

json
```
    {
        "message": "User created successfully."
    }
```
2. Retrieve User (GET)

    URL: /api/user/?email=johnt92@gmail.com&password=shuush_it's_secret

    Method: GET

    Response:

    json
```
    {
        "name": "John Terry",
        "email": "johnt92@gmail.com",
        "password": "shuush_it's_secret"
    }
```

You can use Postman or any API testing tool to interact with the API endpoints.

#Error Handling Information

    If a required field is missing in the POST request, the API will respond with a 400 Bad Request error.
    If a user with the same email already exists when creating a user, the API will respond with a 400 Bad Request error.
    If a user is not found when retrieving by email and password, the API will respond with a 404 Not Found error.

