from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db
from models.user import User
from resources.schedule import ScheduleListResource, ScheduleResource, SchedulePublishResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.app_context().push()

    register_extensions(app)
    register_resources(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)

    api.add_resource(ScheduleListResource, '/schedules')
    api.add_resource(ScheduleResource, '/schedules/<int:schedule_id>')
    api.add_resource(SchedulePublishResource, '/schedules/<int:schedule_id>/publish')


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
