from flask import request, jsonify
from flask_restx import Resource, fields, Namespace
from app import pdb
from app.Models import CustomerDevice
from app.Models.ModelsLogging import Logger


# Veri modeli tanımı
api_customer_device = Namespace(
    "Customer Devices", description="Operations related to Customer Devices"
)

customer_device_model = api_customer_device.model(
    "CustomerDevice",
    {
        "id": fields.Integer(readonly=True, description="Customer Device ID"),
        "customerId": fields.Integer(required=True, description="Customer ID"),
        "deviceTypeId": fields.Integer(required=True, description="Device Type ID"),
        "port": fields.String(required=True, description="Device Port"),
        "ipHost": fields.String(
            required=True, description="Device IP Address or Hostname"
        ),
    },
)
log = Logger()


@api_customer_device.route("/customer_devices")
class CustomerDeviceList(Resource):
    def get(self):
        customer_devices = CustomerDevice.query.all()
        log.log_crud(info="Get", table_name="Customer Devices ")
        return jsonify(
            [
                {
                    "id": device.id,
                    "customerId": device.customerId,
                    "deviceTypeId": device.deviceTypeId,
                    "port": device.port,
                    "ipHost": device.ipHost,
                }
                for device in customer_devices
            ]
        )

    @api_customer_device.expect(customer_device_model)
    def post(self):
        data = request.json
        new_device = CustomerDevice(
            customerId=data["customerId"],
            deviceTypeId=data["deviceTypeId"],
            port=data["port"],
            ipHost=data["ipHost"],
        )
        pdb.session.add(new_device)
        pdb.session.commit()
        log.log_crud(info="Post", table_name="Customer Devices ")
        return jsonify(
            {
                "id": new_device.id,
                "customerId": new_device.customerId,
                "deviceTypeId": new_device.deviceTypeId,
                "port": new_device.port,
                "ipHost": new_device.ipHost,
            }
        )


@api_customer_device.route("/customer_devices/<int:id>")
class CustomerDeviceResource(Resource):
    def get(self, id):
        device = CustomerDevice.query.get_or_404(id)
        log.log_crud(info="Get", table_name=f"Customer Devices {id}")
        return jsonify(
            {
                "id": device.id,
                "customerId": device.customerId,
                "deviceTypeId": device.deviceTypeId,
                "port": device.port,
                "ipHost": device.ipHost,
            }
        )

    @api_customer_device.expect(customer_device_model)
    def put(self, id):
        data = request.json
        device = CustomerDevice.query.get_or_404(id)
        device.customerId = data["customerId"]
        device.deviceTypeId = data["deviceTypeId"]
        device.port = data["port"]
        device.ipHost = data["ipHost"]
        pdb.session.commit()
        log.log_crud(info="Put", table_name=f"Customer Devices {id}")
        return jsonify(
            {
                "id": device.id,
                "customerId": device.customerId,
                "deviceTypeId": device.deviceTypeId,
                "port": device.port,
                "ipHost": device.ipHost,
            }
        )

    def delete(self, id):
        device = CustomerDevice.query.get_or_404(id)
        pdb.session.delete(device)
        pdb.session.commit()
        log.log_crud(info="Delete", table_name=f"Customer Devices {id}")
        return "", 204
