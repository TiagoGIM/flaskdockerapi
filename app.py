from routes import user as user_routes_blueprint
from routes import stock as stock_routes_blueprint
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

app.register_blueprint(user_routes_blueprint)
app.register_blueprint(stock_routes_blueprint)
if __name__ == '__main__':
    app.run(debug=True)
