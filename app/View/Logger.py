from flask import Flask, request, jsonify
from app.Models.Logging import Logger
from flask_restx import Namespace, Resource
from app.config import (
    access_logs,
    error_logs,
    system_logs,
    activity_logs,
    application_logs,
)
import json


api_logger = Namespace("Logs", description="Operations related to Logs")


@api_logger.route("/activity_logs")
class DataResource(Resource):
    def get(self):
        documents = activity_logs.find()
        result = [json.loads(json.dumps(doc, default=str)) for doc in documents]
        return jsonify(result)


@api_logger.route("/access_logs")
class DataResource(Resource):
    def get(self):
        documents = access_logs.find()
        result = [json.loads(json.dumps(doc, default=str)) for doc in documents]
        return jsonify(result)


@api_logger.route("/error_logs")
class DataResource(Resource):
    def get(self):
        documents = error_logs.find()
        result = [json.loads(json.dumps(doc, default=str)) for doc in documents]
        return jsonify(result)


@api_logger.route("/system_logs")
class DataResource(Resource):
    def get(self):
        documents = system_logs.find()
        result = [json.loads(json.dumps(doc, default=str)) for doc in documents]
        return jsonify(result)


@api_logger.route("/application_logs")
class DataResource(Resource):
    def get(self):
        documents = application_logs.find()
        result = [json.loads(json.dumps(doc, default=str)) for doc in documents]
        return jsonify(result)
