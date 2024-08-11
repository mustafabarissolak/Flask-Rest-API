# PostgreSQL Configuration
class PostgresqlConfig:
    postgresqlUserName = "your user name"
    postgresqlPassword = "your password"
    postgresqlDbName = "your database name "
    SQLALCHEMY_DATABASE_URI = f"postgresql://{postgresqlUserName}:{postgresqlPassword}@localhost/{postgresqlDbName}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# app/config.py
import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt-secret-key")


# MongoDB Configuration
from pymongo import MongoClient

mongo_url = "mongodb://localhost:27017/"
client = MongoClient(mongo_url)
mdb = client["swaggerLogs"]

# MongoDB Collections
application_logs = mdb[
    "application_logs"
]  # Uygulama logları: Uygulama ile ilgili genel logları tutar
error_logs = mdb[
    "error_logs"
]  # Hata logları: Uygulama veya sistemde oluşan hataları kaydeder
access_logs = mdb[
    "access_logs"
]  # Erişim logları: Uygulamanın kimler tarafından erişildiğini ve ne zaman erişildiğini gösterir
activity_logs = mdb[
    "activity_logs"
]  # Aktivite logları: Kullanıcı aktiviteleri ve işlemlerini kaydeder
system_logs = mdb[
    "system_logs"
]  # Sistem logları: Sistemle ilgili genel durum ve olayları tutar


# Dummy data to ensure collections are created
# application_logs.insert_one({"init": "collection created"})
# error_logs.insert_one({"init": "collection created"})
# access_logs.insert_one({"init": "collection created"})
# activity_logs.insert_one({"init": "collection created"})
# system_logs.insert_one({"init": "collection created"})
