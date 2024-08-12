class PostgresqlConfig:
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost/swagger"
=======
    SQLALCHEMY_DATABASE_URI = "postgresql://user_name:password@server_name/db_name"
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33
    SQLALCHEMY_TRACK_MODIFICATIONS = False


from pymongo import MongoClient

mongo_url = "mongodb://localhost:27017/"
client = MongoClient(mongo_url)
mdb = client["swaggerLogs"] # db name

<<<<<<< HEAD
user_logs = mdb["user_logs"]
=======
# MongoDB Collections
user_logs = mdb["user_logs"] # collection name
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33
crud_logs = mdb["crud_logs"]
error_logs = mdb["error_logs"]
