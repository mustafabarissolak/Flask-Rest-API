from flask_restx import Resource, fields, Namespace
from app import api, pdb
from app.Models import Customer
from app.Models.ModelsLogging import Logger
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

log = Logger()


@api_customer.route("/customers")
class CustomerList(Resource):
    def get(self):

        customers = Customer.query.all()
        log.log_crud(info="Get", table_name="Customers")
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
        log.log_crud(info="Post", table_name="Customers")
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

        customer = Customer.query.get_or_404(id)
        log.log_crud(info="Get", table_name=f"Customers {id}")
        return jsonify(
            {
                "id": customer.id,
                "name": customer.name,
                "firstName": customer.firstName,
                "mail": customer.mail,
                "phoneNumber": customer.phoneNumber,
                "address": customer.address,
            }
        )

    @api_customer.expect(customer_model)
    def put(self, id):

        data = request.json
        customer = Customer.query.get_or_404(id)
        customer.name = data["name"]
        customer.firstName = data["firstName"]
        customer.mail = data["mail"]
        customer.phoneNumber = data["phoneNumber"]
        customer.address = data["address"]
        pdb.session.commit()
        log.log_crud(info="Put", table_name=f"Customers {id}")
        return jsonify(
            {
                "id": customer.id,
                "name": customer.name,
                "firstName": customer.firstName,
                "mail": customer.mail,
                "phoneNumber": customer.phoneNumber,
                "address": customer.address,
            }
        )

    def delete(self, id):

        customer = Customer.query.get_or_404(id)
        pdb.session.delete(customer)
        pdb.session.commit()
        log.log_crud(info="Delete", table_name=f"Customers {id}")
        return "", 204
