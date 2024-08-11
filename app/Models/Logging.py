from datetime import datetime
from app.config import (
    application_logs,
    error_logs,
    access_logs,
    activity_logs,
    system_logs,
)
from flask_restx import Resource


class Logger(Resource):
    @staticmethod
    def log_application(message, level="INFO"):
        log_entry = {"timestamp": datetime, "level": level, "message": message}
        application_logs.insert_one(log_entry)

    @staticmethod
    def log_error(message, level="ERROR"):
        log_entry = {"timestamp": datetime, "level": level, "message": message}
        error_logs.insert_one(log_entry)

    @staticmethod
    def log_access(user, action):
        log_entry = {"timestamp": datetime, "user": user, "action": action}
        access_logs.insert_one(log_entry)

    @staticmethod
    def log_activity(user, activity):
        log_entry = {"timestamp": datetime, "user": user, "activity": activity}
        activity_logs.insert_one(log_entry)

    @staticmethod
    def log_system(message, level="SYSTEM"):
        log_entry = {"timestamp": datetime, "level": level, "message": message}
        system_logs.insert_one(log_entry)
