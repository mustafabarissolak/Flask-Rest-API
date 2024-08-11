from flask import request, jsonify
from flask_restx import Resource, fields, Namespace
from app import pdb
from app.Models import DeviceType

api_device_type = Namespace(
    "Device Type", description="Operations related to Device Type"
)

device_type_model = api_device_type.model(
    "DeviceType",
    {
        "id": fields.Integer(readonly=True, description="Device Type ID"),
        "deviceType": fields.String(required=True, description="Device Type Name"),
        "protocol": fields.String(required=True, description="Device Protocol"),
        "command": fields.String(required=True, description="Device Commands"),
    },
)


@api_device_type.route("/device_types")
class DeviceTypeList(Resource):
    def get(self):
        deviceTypes = DeviceType.query.all()
        return jsonify(
            [
                {
                    "id": device.id,
                    "deviceType": device.deviceType,
                    "protocol": device.protocol,
                    "command": device.command,
                }
                for device in deviceTypes
            ]
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
        return jsonify(
            {
                "id": new_device_type.id,
                "deviceType": new_device_type.deviceType,
                "protocol": new_device_type.protocol,
                "command": new_device_type.command,
            },
            {"Code": 201},
        )


@api_device_type.route("/device_types/<int:id>")
class DeviceTypeResource(Resource):
    def get(self, id):
        device = DeviceType.query.get_or_404(id)
        return jsonify(
            {
                "id": device.id,
                "deviceType": device.deviceType,
                "protocol": device.protocol,
                "command": device.command,
            }
        )

    @api_device_type.expect(device_type_model)
    def put(self, id):
        data = request.json
        device = DeviceType.query.get_or_404(id)
        device.deviceType = data["deviceType"]
        device.protocol = data["protocol"]
        device.command = data["command"]
        pdb.session.commit()
        return jsonify(
            {
                "id": device.id,
                "deviceType": device.deviceType,
                "protocol": device.protocol,
                "command": device.command,
            }
        )

    def delete(self, id):
        device = DeviceType.query.get_or_404(id)
        pdb.session.delete(device)
        pdb.session.commit()
        return "", 204
