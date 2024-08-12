class PostgresqlConfig:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost/swagger"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


from pymongo import MongoClient

mongo_url = "mongodb://localhost:27017/"
client = MongoClient(mongo_url)
mdb = client["swaggerLogs"]

user_logs = mdb["user_logs"]
crud_logs = mdb["crud_logs"]
error_logs = mdb["error_logs"]
