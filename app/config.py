class PostgresqlConfig:
    SQLALCHEMY_DATABASE_URI = "postgresql://user_name:password@localhost/db_name"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis config.py
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0


from pymongo import MongoClient

mongo_url = "mongodb://localhost:27017/"
client = MongoClient(mongo_url)
mdb = client["swaggerLogs"] 

user_logs = mdb["user_logs"]
crud_logs = mdb["crud_logs"]
error_logs = mdb["error_logs"]
