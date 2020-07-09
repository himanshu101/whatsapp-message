# Messaging-Restful-API's  

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists. (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs.
* Mysql

* #### Dependencies
  ##### First Method (Recommended)
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd wahtsapp-message
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Copy env file and change according to your system
        ```bash
            $ cp .env.example .env
        ```
    5. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the api service on your browser by using
    ```
        http://localhost:8000/api/v1/
    ```

* ####  To Run Tests
    ```bash
        $ python manage.py test message_api.tests
    ```

* #### APIs
    ```bash
        1. /api/v1/groups/{{group_id}}/add - POST
        2. /api/v1/groups - LIST, CREATE
        3. /api/v1/messages/groups/{{group_id}} - LIST, POST
        4. /api/v1/messages/groups/{{group_id}}?sender_id={{sender_id}} - POST, LIST
    ```