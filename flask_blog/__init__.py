from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from flask_blog.config import Config
# from flask_mail import Mail


db = SQLAlchemy()
bycrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'

##########################################################
# login_manager.login_message_category = 'info'
# mail = Mail()
###########################################################



def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bycrypt.init_app(app)
    login_manager.init_app(app)
    # mail.init_app(app)


    from flask_blog.main.routs import main
    from flask_blog.users.routs import users
    from flask_blog.posts.routs import posts
    from flask_blog.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)


    return app
