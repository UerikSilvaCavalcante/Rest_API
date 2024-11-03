# REST API
- Using Django and Django-ninja

## Function
This is a REST API developed in **Python** and **Django**, using the django-ninja library to facilitate the organization and creation of the **CRUD** for this **API**.

## Objective
This API has a simple objective, as it was made purely for learning purposes. It is a book manager, where you can store books and also review them by giving a rating and adding a comment.

## Technologies
- Python
- Django
- Djnago-Ninja
- SQLite3

## How to use
- (Optional) create a Python virtual environment
- Activate it
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
- Install Django
    ```
        pip install django
    ```

- Install Django-Ninja

    ```
        pip install django-ninja
    ```

- Run the makemigrations from manage.py to update the migrations

    ``` 
        python manage.py makemigration
    ```
- Run the migrate from manage.py to apply the migrations to the database

    ``` 
        python manage.py migrate
    ```

- Run the server to start the API

    ``` 
        python manage.py runserver
    ```
