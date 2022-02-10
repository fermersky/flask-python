class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123@localhost:5432/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "123"
    DEBUG = True
    SQLALCHEMY_ECHO = False


class DockerConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123@172.17.0.2:5432/flask"
