from flask import Flask

def create_app():
    app = Flask(__name__)

    from views import blueprint
    app.register_blueprint(blueprint.bp)

    return app
