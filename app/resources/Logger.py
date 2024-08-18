from flask import jsonify
from flask_restx import Namespace, Resource
import json
from app.Models.ModelsLogging import crud_logs, user_logs, error_logs
from app.Models.ModelsToken import token_required


api_logger = Namespace("logs")


@api_logger.route("/user_log")
class UserDataResource(Resource):
    @api_logger.doc(security="apikey")
    @token_required
    def get(self, user_id, token):
        documents = user_logs.find()
        result = [json.loads(json.dumps(doc, default=str)) for doc in documents]
        return jsonify(
            result,
            {
                "code": 200,
                "user id": user_id,
            },
        )


@api_logger.route("/crud_log")
class CrudDataResource(Resource):
    @api_logger.doc(security="apikey")
    @token_required
    def get(self, user_id):
        documents = crud_logs.find()
        result = [json.loads(json.dumps(doc, default=str)) for doc in documents]
        return jsonify(
            result,
            {
                "code": 200,
                "user id": user_id,
            },
        )


@api_logger.route("/error_log")
class ErrorDataResource(Resource):
    @api_logger.doc(security="apikey")
    @token_required
    def get(self, user_id):
        documents = error_logs.find()
        result = [json.loads(json.dumps(doc, default=str)) for doc in documents]
        return jsonify(
            result,
            {
                "code": 200,
                "user id": user_id,
            },
        )
