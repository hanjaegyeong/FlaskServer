from flask import Flask

def create_app():
    app = Flask(__name__)

    import blueprint
    app.register_blueprint(blueprint.bp)

    return app
