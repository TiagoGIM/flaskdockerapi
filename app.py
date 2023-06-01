from routes import all_routes
from extensions import db, migrate
from flask import Flask
from os import environ

URL_DB = environ.get('DB_URL')

if not URL_DB:
    import os
    from dotenv import load_dotenv
    load_dotenv(".env")
    URL_DB = environ.get('DATABASE_URL')


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = URL_DB

    db.init_app(app)
    migrate.init_app(app, db)
    return app


app = create_app()

for rt in all_routes:
    app.register_blueprint(rt)


if __name__ == '__main__':
    app.run(debug=True)
