# PostgreSQL Configuration
class PostgresqlConfig:
    SQLALCHEMY_DATABASE_URI = "postgresql://user_name:password@server_name/db_name"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# MongoDB Configuration
from pymongo import MongoClient

mongo_url = "mongodb://localhost:27017/"
client = MongoClient(mongo_url)
mdb = client["swaggerLogs"] # db name

# MongoDB Collections
user_logs = mdb["user_logs"] # collection name
crud_logs = mdb["crud_logs"]
error_logs = mdb["error_logs"]
