# Simple Inventory Management System using Django Rest Framework


This project provides a backend API for an Inventory Management System using Django Rest Framework (DRF), JWT-based authentication, PostgreSQL for the database, and Redis for caching. The API supports CRUD operations on inventory items, user authentication, and token-based access control.

## Prerequisites

- Python (version 3.x recommended)
- Django
- Django REST Framework
- Redis (for caching)
- PostgreSQL


## Setup Instructions

### 1. Clone the repository

First, you need to clone the repository to your local machine. You can do this using the following command:

```bash
git clone https://github.com/girishc24/Inventory-Management.git
cd Inventory-Management
```
### 2. Create a virtual environment

Create a virtual environment to install the project dependencies. This helps in maintaining project-specific dependencies and avoiding conflicts with other projects.

- For Linux/Mac:
```
python -m venv venv
source venv/bin/activate
```
- For Windows:
```
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies

With the virtual environment activated, install the required dependencies using the requirements.txt file:
```
pip install -r requirements.txt
```
### 4. Configure PostgreSQL
Create a PostgreSQL database and update DATABASES settings in settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```
### 5. Run database migrations
Before running the application, set up the database by running the migrations:
```
python manage.py makemigrations
python manage.py migrate
```
### 6. Set up Redis
Ensure Redis is running on localhost:6379. You can either install Redis manually or use Docker:
```
docker run --name redis -p 6379:6379 -d redis

```
### 7. Create a superuser
```
Create a superuser
```
### 8. Run the development server
Start the Django development server to test the application locally:
```
python manage.py runserver
```
You can now access the application at http://localhost:8000.


## API Documentation
Authentication
- Login to get JWT tokens
- Method POST
```
http://127.0.0.1:8000/auth/jwt/create/
```
Request body:
```
{
  "username": "your_username",
  "password": "your_password"
}

```
Response:
```
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}

```
## JWT Authentication in API Requests
All endpoints that require authentication use JWT as the prefix for the Authorization header instead of the default Bearer.
- n your requests, use this format:
```
authorization: JWT <access_token>
```
For example:

```
authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ...
```

## Item Endpoints
All the item endpoints require authentication. Include the JWT access token in the Authorization header for the requests.
1. Create Item
- POST /items/
- Request body:
```
{
  "name": "Item Name",
  "description": "Item Description"
}
```
Response:
```
{
  "id": 1,
  "name": "Item Name",
  "description": "Item Description"
}
```
2. Get All Items
- GET /items/
- Response
```
[
  {
    "id": 1,
    "name": "Item Name",
    "description": "Item Description"
  },
  {
    "id": 2,
    "name": "Another Item",
    "description": "Another Description"
  }
]
```
3.  Get Single Item
- GET /items/{item_id}/
- Response:
```
{
  "id": 1,
  "name": "Item Name",
  "description": "Item Description"
}
```
4. Update Item
- PUT /items/{item_id}/
- Request body:
```
{
  "name": "Updated Item Name",
  "description": "Updated Description"
}
```
- Responce 
```
{
  "name": "Updated Item Name",
  "description": "Updated Description"
}
```
5. Delete Item
- DELETE /items/{item_id}/
- Response:
```
{
  "message": "Item deleted successfully"
}
```
## Testing
To run unit tests for the application, use the following command:
```
python manage.py test

```

## Logging
Logging is configured to capture API usage, errors, and debugging information. Log files are stored in debug.log within the project directory.