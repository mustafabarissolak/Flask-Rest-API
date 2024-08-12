from flask import jsonify
from flask_restx import Namespace, Resource
import json
from app.Models.ModelsLogging import crud_logs, user_logs, error_logs


api_logger = Namespace("Logs")


@api_logger.route("/user_logs")
class UserDataResource(Resource):
    def get(self):
        documents = user_logs.find()
        result = [json.loads(json.dumps(doc, default=str)) for doc in documents]
        return jsonify(result, {"code": 200})


@api_logger.route("/crud_logs")
class CrudDataResource(Resource):
    def get(self):
        documents = crud_logs.find()
        result = [json.loads(json.dumps(doc, default=str)) for doc in documents]
        return jsonify(result, {"code": 200})


@api_logger.route("/error_logs")
class ErrorDataResource(Resource):
    def get(self):
        documents = error_logs.find()
        result = [json.loads(json.dumps(doc, default=str)) for doc in documents]
        return jsonify(result, {"code": 200})
