from flask import request, jsonify
from flask_restx import Resource, fields, Namespace
from app import pdb
from app.Models import DeviceType
from app.Models.ModelsLogging import Logger
<<<<<<< HEAD
=======

>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33


api_device_type = Namespace("Device Type")

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


@api_device_type.route("/device_types")
class DeviceTypeList(Resource):
    def get(self):
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
            {"code": 200},
        )

    @api_device_type.expect(device_type_model)
    def post(self):
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
            {"Code": 200},
        )


@api_device_type.route("/device_types/<int:id>")
class DeviceTypeResource(Resource):
    def get(self, id):
        device = DeviceType.query.get_or_404(id)
        log.log_crud(info="Get", table_name="Device Type")
        return jsonify(
            {
                "id": device.id,
                "deviceType": device.deviceType,
                "protocol": device.protocol,
                "command": device.command,
            },
            {"code": 200},
        )

    @api_device_type.expect(device_type_model)
    def put(self, id):
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
            {"code": 200},
        )

    def delete(self, id):
        device = DeviceType.query.get_or_404(id)
        pdb.session.delete(device)
        pdb.session.commit()
        log.log_crud(info="Delete", table_name="Device Type")
<<<<<<< HEAD
        return jsonify(
            {"delete": id},
            {"code": 200},
        )
=======
        return "", 204
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33
