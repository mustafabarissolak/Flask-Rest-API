from datetime import datetime, timezone
from app.config import crud_logs, user_logs, error_logs


class Logger:

    def log_users(self, info):
        log_entry = {
            "DATETIME": datetime.now(),
            "USER info": info,
        }
        user_logs.insert_one(log_entry)

    def log_crud(self, info, table_name):
        log_entry = {
            "DATETIME": datetime.now(),
            "CRUD info": info,
            "TABLE name": table_name,
        }
        crud_logs.insert_one(log_entry)

    def log_error(self, info):
        log_enty = {
            "DATETIME": datetime.now(),
            "ERROR": info,
        }
        error_logs.insert_one(log_enty)
