from app import app
from api.route import api
from auth.route import auth


def run_server(from_docker=False):
    app.register_blueprint(api)
    app.register_blueprint(auth)

    if from_docker:
        app.config.from_object("config.DockerConfig")

    return app


if __name__ == "__main__":
    run_server().run(debug=True, port=8000)
