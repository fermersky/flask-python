from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_executor import Executor
from celery_staff.celery import make_celery


app = Flask(__name__)
app.config.from_object("config.Config")

app.config['EXECUTOR_MAX_WORKERS'] = 4
app.config['EXECUTOR_TYPE'] = 'process'

# app.config.update(
#     CELERY_BROKER_URL='redis://localhost:6379',
#     CELERY_RESULT_BACKEND='redis://localhost:6379'
# )

# celery = make_celery(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
executor = Executor(app)
