from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] =='anythingreally'

    
    from blogip.main.routes import main
    app.register_blueprint(main)
    return app
