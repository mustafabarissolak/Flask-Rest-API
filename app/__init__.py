from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api

pdb = SQLAlchemy()
migrate = Migrate()
api = Api()


def create_app():

    app = Flask(__name__)
    app.config.from_object("app.config.PostgresqlConfig")

    pdb.init_app(app)
    migrate.init_app(app, pdb)
    api.init_app(app)

    with app.app_context():
        from app.resources.Customer import api_customer
        from app.resources.User import api_users
        from app.resources.DeviceType import api_device_type
        from app.resources.CustomerDevice import api_customer_device
        from app.resources.Logger import api_logger

        api.add_namespace(api_customer)
        api.add_namespace(api_users)
        api.add_namespace(api_device_type)
        api.add_namespace(api_customer_device)
        api.add_namespace(api_logger)

    return app
