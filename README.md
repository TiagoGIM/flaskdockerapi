# Python Flask CRUD Project

This is a Python CRUD project using Flask, Docker and PostgreSQL. It includes a Dockerfile, Python source code, and SQLAlchemy for easy database configuration. CRUD capabilities enable create, read, update, and delete operations. Code is structured in a modular, clean way for easy maintenance. 

This application uses the Model-View-Controller (MVC) pattern to separate the different parts of the application into three distinct components. I believe that this approach can make my code more modular, easier to maintain and update, and facilitate collaboration among us developers. In brief, the use of the MVC pattern makes my application more robust, scalable, and easy to maintain.

For a step-by-step tutorial on how to set up and run this app, please check out our tutorial at [link](https://dev.to/francescoxx/build-a-crud-rest-api-in-python-using-flask-sqlalchemy-postgres-docker-28lo)

## Project Structure
```
├── controllers/
│   └── user_controller.py
├── models/
│   ├── __init__.py
│   └── user.py
├── repositories/
│   └── user_repository.py
├── services/
│   └── user_service.py
├── app.py
├── docker-compose.yml
├── Dockerfile
├── extensions.py
└── routes.py
```
- `app.py`: main Flask application file
- `extensions.py`: module for extensions (e.g. DB) initialization and connection to database (`db.session`)
- `routes.py`: directory for Flask routes
- `Dockerfile`: Dockerfile for building the app
- `requirements.txt`: requirements file for pip
- `services`: 
- `controllers`:
- `models`: directory for database models

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


## Supporting Material

- [How to Use Flask-SQLAlchemy With Flask Blueprints (youtube)](https://www.youtube.com/watch?v=WhwU1-DLeVw&ab_channel=CaravanaCloud)
- [SOLID Principles: Improve Object-Oriented Design in Python](https://realpython.com/solid-principles-python/)
- [Minimal Flask Application using MVC design pattern](https://medium.com/@arslanaut/minimal-flask-application-using-mvc-design-pattern-842845cef703)
- [Design the infrastructure persistence layer](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design)
- [How to Use Flask-SQLAlchemy to Interact with Databases in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application)
## Contributing

To contribute to this project, please fork the repository and submit a pull request.
