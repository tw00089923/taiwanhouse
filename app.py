# Loading Flask
from flask import Flask
# Loading Config
from config import app_config
# Loading Flask-rest
from flask_restful import Api
# Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. http://flask.pocoo.org/
from flask_sqlalchemy import SQLAlchemy
# 關連式資料庫 ORM http://flask-sqlalchemy.pocoo.org/2.3/
from flask_bcrypt import Bcrypt
# flask_bcrypt 密碼加密 http://flask-bcrypt.readthedocs.io/en/latest/ 
from flask_login import LoginManager
# flask_jwt  https://pythonhosted.org/Flask-JWT/
from flask_jwt import JWT, jwt_required, current_identity
# Flask(__name__ , template_folder='application/templates') 可頁面修改參數
app = Flask(__name__, template_folder='application/templates',static_url_path="/static")

api = Api(app)
# config from dictionary
app.config.from_object(app_config["development"])

login_manager = LoginManager()

login_manager.init_app(app)

db = SQLAlchemy(app)

flask_bcrypt = Bcrypt()

flask_bcrypt.init_app(app)

from security import authenticate, identity

jwt = JWT(app, authenticate, identity)

### import router ..... 
import application.router

import application.api


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)