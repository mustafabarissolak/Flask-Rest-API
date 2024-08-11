from flask import request, jsonify
from flask_restx import Resource, fields, Namespace
from app import pdb
from app.Models import CustomerDevice

# Veri modeli tanımı
api_customer_device = Namespace("Customer Devices", description="Operations related to Customer Devices")

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


@api_customer_device.route("/customer_devices")
class CustomerDeviceList(Resource):
    # Tüm müşteri cihazlarını al
    def get(self):
        customer_devices = CustomerDevice.query.all()
        # logger("get", "CustomerDevice")
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

    # Yeni müşteri cihazı ekle
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
        # logger("post", "CustomerDevice")
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
    # Belirli bir müşteri cihazı bilgilerini al
    def get(self, id):
        device = CustomerDevice.query.get_or_404(id)
        # logger("get", f"CustomerDevice, Id:{id}")
        return jsonify(
            {
                "id": device.id,
                "customerId": device.customerId,
                "deviceTypeId": device.deviceTypeId,
                "port": device.port,
                "ipHost": device.ipHost,
            }
        )

    # Belirli bir müşteri cihazı bilgilerini güncelle
    @api_customer_device.expect(customer_device_model)
    def put(self, id):
        data = request.json
        device = CustomerDevice.query.get_or_404(id)
        device.customerId = data["customerId"]
        device.deviceTypeId = data["deviceTypeId"]
        device.port = data["port"]
        device.ipHost = data["ipHost"]
        pdb.session.commit()
        # logger("put", f"CustomerDevice, Id:{id}")
        return jsonify(
            {
                "id": device.id,
                "customerId": device.customerId,
                "deviceTypeId": device.deviceTypeId,
                "port": device.port,
                "ipHost": device.ipHost,
            }
        )

    # Belirli bir müşteri cihazı sil
    def delete(self, id):
        device = CustomerDevice.query.get_or_404(id)
        pdb.session.delete(device)
        pdb.session.commit()
        # logger("delete", f"CustomerDevice, Id:{id}")
        return "", 204
