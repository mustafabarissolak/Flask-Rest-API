from flask_restx import Resource, fields, Namespace
from app import api, pdb
from app.Models import Customer
from flask import request, jsonify

api_customer = Namespace("Customers", description="Operations related to Customers")

customer_model = api_customer.model(
    "Customer",
    {
        "id": fields.Integer(readonly=True, description="Customer id"),
        "name": fields.String(required=True, description="Customer name"),
        "firstName": fields.String(required=True, description="Customer firstName"),
        "mail": fields.String(required=True, description="Customer mail"),
        "phoneNumber": fields.String(required=True, description="Customer Phone"),
        "address": fields.String(required=True, description="Customer address"),
    },
)


@api_customer.route("/customers")
class CustomerList(Resource):
    def get(self):
        customers = Customer.query.all()
        # logger("get", "Customer")
        return jsonify(
            [
                {
                    "id": customer.id,
                    "name": customer.name,
                    "firstName": customer.firstName,
                    "mail": customer.mail,
                    "phoneNumber": customer.phoneNumber,
                    "address": customer.address,
                }
                for customer in customers
            ]
        )

    @api_customer.expect(customer_model)
    def post(self):
        data = request.json
        yeni_Customer = Customer(
            name=data["name"],
            firstName=data["firstName"],
            mail=data["mail"],
            phoneNumber=data["phoneNumber"],
            address=data["address"],
        )
        pdb.session.add(yeni_Customer)
        pdb.session.commit()
        # logger("get", "Customer")
        return jsonify(
            {
                "id": yeni_Customer.id,
                "name": yeni_Customer.name,
                "firstName": yeni_Customer.firstName,
                "mail": yeni_Customer.mail,
                "phoneNumber": yeni_Customer.phoneNumber,
                "address": yeni_Customer.address,
            },
            {"Code": 201},
        )


@api_customer.route("/customers/<int:id>")
class CustomerResource(Resource):
    def get(self, id):
        musteri = Customer.query.get_or_404(id)
        # logger("get", f"Cutomer Id: {id}")
        return jsonify(
            {
                "id": musteri.id,
                "name": musteri.name,
                "firstName": musteri.firstName,
                "mail": musteri.mail,
                "phoneNumber": musteri.phoneNumber,
                "address": musteri.address,
            }
        )

    @api_customer.expect(customer_model)
    def put(self, id):
        data = request.json
        musteri = Customer.query.get_or_404(id)
        musteri.name = data["name"]
        musteri.firstName = data["firstName"]
        musteri.mail = data["mail"]
        musteri.phoneNumber = data["phoneNumber"]
        musteri.address = data["address"]
        pdb.session.commit()
        # logger("put", f"Customer Id: {id}")
        return jsonify(
            {
                "id": musteri.id,
                "name": musteri.name,
                "firstName": musteri.firstName,
                "mail": musteri.mail,
                "phoneNumber": musteri.phoneNumber,
                "address": musteri.address,
            }
        )

    def delete(self, id):
        musteri = Customer.query.get_or_404(id)
        pdb.session.delete(musteri)
        pdb.session.commit()
        # logger("delete", f"Customer Id: {id}")
        return "", 204
