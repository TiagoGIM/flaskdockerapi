from flask import Flask, jsonify, make_response
from os import environ
from extensions import db
from controllers.user_controller import user_controller

app = Flask(__name__)
# // environ.get('DB_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgrespw@localhost:49153'
app.register_blueprint(user_controller)
db.init_app(app)
# db.create_all()


# generic 500 error handler for all exceptions.  If you want to handle specific exceptions, use the '@app
@app.errorhandler(500)
@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route'}), 200)


if __name__ == '__main__':
    app.run(debug=True)
