from flask import request, jsonify
from flask_restx import Resource, fields, Namespace
from app import pdb
from app.Models import DeviceType
from app.Models.ModelsLogging import Logger
from app.Models.ModelsToken import token_required


api_device_type = Namespace("device_types")

device_type_model = api_device_type.model(
    "DeviceType",
    {
        "id": fields.Integer(readonly=True),
        "deviceType": fields.String(required=True),
        "protocol": fields.String(required=True),
        "command": fields.String(required=True),
    },
)

log = Logger()


@api_device_type.route("/device_type")
class DeviceTypeList(Resource):
    @api_device_type.doc(security="apikey")
    @token_required
    def get(self, user_id):
        deviceTypes = DeviceType.query.all()
        log.log_crud(info="Get", table_name="Device Type")
        return jsonify(
            [
                {
                    "id": device.id,
                    "deviceType": device.deviceType,
                    "protocol": device.protocol,
                    "command": device.command,
                }
                for device in deviceTypes
            ],
            {
                "code": 200,
                "user id": user_id,
            },
        )

    @api_device_type.doc(security="apikey")
    @api_device_type.expect(device_type_model)
    @token_required
    def post(self, user_id):
        data = request.json
        new_device_type = DeviceType(
            deviceType=data["deviceType"],
            protocol=data["protocol"],
            command=data["command"],
        )
        pdb.session.add(new_device_type)
        pdb.session.commit()
        log.log_crud(info="Post", table_name="Device Type")
        return jsonify(
            {
                "id": new_device_type.id,
                "deviceType": new_device_type.deviceType,
                "protocol": new_device_type.protocol,
                "command": new_device_type.command,
            },
            {
                "Code": 200,
                "user id": user_id,
            },
        )


@api_device_type.route("/device_type/<int:id>")
class DeviceTypeResource(Resource):
    @api_device_type.doc(security="apikey")
    @token_required
    def get(self, id, user_id):
        device = DeviceType.query.get_or_404(id)
        log.log_crud(info="Get", table_name="Device Type")
        return jsonify(
            {
                "id": device.id,
                "deviceType": device.deviceType,
                "protocol": device.protocol,
                "command": device.command,
            },
            {
                "code": 200,
                "user id": user_id,
            },
        )

    @api_device_type.doc(security="apikey")
    @api_device_type.expect(device_type_model)
    @token_required
    def put(self, id, user_id):
        data = request.json
        device = DeviceType.query.get_or_404(id)
        device.deviceType = data["deviceType"]
        device.protocol = data["protocol"]
        device.command = data["command"]
        pdb.session.commit()
        log.log_crud(info="Put", table_name="Device Type")
        return jsonify(
            {
                "id": device.id,
                "deviceType": device.deviceType,
                "protocol": device.protocol,
                "command": device.command,
            },
            {
                "code": 200,
                "user id": user_id,
            },
        )

    @api_device_type.doc(security="apikey")
    @token_required
    def delete(self, id, user_id):
        device = DeviceType.query.get_or_404(id)
        pdb.session.delete(device)
        pdb.session.commit()
        log.log_crud(info="Delete", table_name="Device Type")

        return jsonify(
            {"delete": id},
            {
                "code": 200,
                "user id": user_id,
            },
        )
