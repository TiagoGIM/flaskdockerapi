# Python Flask CRUD Project

This is a Python CRUD project using Flask, Docker and PostgreSQL. It includes a Dockerfile, Python source code, and SQLAlchemy for easy database configuration. CRUD capabilities enable create, read, update, and delete operations. Code is structured in a modular, clean way for easy maintenance. 

For a step-by-step tutorial on how to set up and run this app, please check out our tutorial at [link](https://dev.to/francescoxx/build-a-crud-rest-api-in-python-using-flask-sqlalchemy-postgres-docker-28lo)

## Project Structure

- `app.py`: main Flask application file
- `config.py`: configuration file for app
- `Dockerfile`: Dockerfile for building the app
- `requirements.txt`: requirements file for pip
- `app/static`: static files for the app (CSS, JS)
- `app/templates`: templates for the app (HTML)
- `app/models/`: directory for database models
- `app/routes/`: directory for Flask routes

## Getting Started

1. Clone the repository:
    ```
    git clone https://github.com/username/repo.git
    ```
2. To run the Postgres container, type:
    ```
    docker compose up -d flask_db
    ```
3. Go back to the folder where the docker-compose.yml is located and type:
    ```
    docker compose build

    ```
4. Run the flask_app service:
  ```
    docker compose up flask_app

  ```
5. Access the app in your browser at `http://localhost:5000/`.

## CRUD Operations

This app enables the following CRUD operations:

- `Create`: Adds a new entry to the database.
- `Read`: Retrieves data from the database.
- `Update`: Modifies an existing entry in the database.
- `Delete`: Removes an entry from the database.

## Contributing

To contribute to this project, please fork the repository and submit a pull request.
