from flask import Flask
from os import environ
from extensions import db, migrate
from routes import user as user_routes_blueprint


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
    db.init_app(app)
    migrate.init_app(app, db)
    return app


app = create_app()

app.register_blueprint(user_routes_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
