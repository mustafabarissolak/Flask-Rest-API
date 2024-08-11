# PostgreSQL Configuration
class PostgresqlConfig:
    postgresqlUserName = "postgres"
    postgresqlPassword = "1234"
    postgresqlDbName = "swagger"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{postgresqlUserName}:{postgresqlPassword}@localhost/{postgresqlDbName}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# MongoDB Configuration
from pymongo import MongoClient

mongo_url = "mongodb://localhost:27017/"
client = MongoClient(mongo_url)
mdb = client["swaggerLogs"]

# MongoDB Collections
application_logs = mdb["application_logs"]
error_logs = mdb["error_logs"]
access_logs = mdb["access_logs"]
activity_logs = mdb["activity_logs"]
system_logs = mdb["system_logs"]
