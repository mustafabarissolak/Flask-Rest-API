from flask_restx import Resource, fields, Namespace
from app import pdb
from app.Models import Customer
from app.Models.ModelsLogging import Logger
from flask import request, jsonify


api_customer = Namespace("customers")

customer_model = api_customer.model(
    "Customer",
    {
        "id": fields.Integer(readonly=True),
        "firstName": fields.String(required=True),
        "lastName": fields.String(required=True),
        "mail": fields.String(required=True),
        "phoneNumber": fields.String(required=True),
        "address": fields.String(required=True),
    },
)

log = Logger()


@api_customer.route("/customer")
class CustomerList(Resource):
    def get(self):
        customers = Customer.query.all()
        log.log_crud(info="Get", table_name="Customers")
        return jsonify(
            [
                {
                    "id": customer.id,
                    "firstName": customer.firstName,
                    "lastName": customer.lastName,
                    "mail": customer.mail,
                    "phoneNumber": customer.phoneNumber,
                    "address": customer.address,
                }
                for customer in customers
            ],
            {"code": 200},
        )

    @api_customer.expect(customer_model)
    def post(self):
        data = request.json
        new_customer = Customer(
            firstName=data["firstName"],
            lastName=data["lastName"],
            mail=data["mail"],
            phoneNumber=data["phoneNumber"],
            address=data["address"],
        )
        pdb.session.add(new_customer)
        pdb.session.commit()
        log.log_crud(info="Post", table_name="Customers")
        return jsonify(
            {
                "id": new_customer.id,
                "firstName": new_customer.firstName,
                "lastName": new_customer.lastName,
                "mail": new_customer.mail,
                "phoneNumber": new_customer.phoneNumber,
                "address": new_customer.address,
            },
            {"Code": 201},
        )


@api_customer.route("/customer/<int:id>")
class CustomerResource(Resource):
    def get(self, id):
        customer = Customer.query.get_or_404(id)
        log.log_crud(info="Get", table_name=f"Customers {id}")
        return jsonify(
            {
                "id": customer.id,
                "firstName": customer.firstName,
                "lastName": customer.lastName,
                "mail": customer.mail,
                "phoneNumber": customer.phoneNumber,
                "address": customer.address,
            },
            {"code": 200},
        )

    @api_customer.expect(customer_model)
    def put(self, id):
        data = request.json
        customer = Customer.query.get_or_404(id)
        customer.firstName = data["firstName"]
        customer.lastName = data["lastName"]
        customer.mail = data["mail"]
        customer.phoneNumber = data["phoneNumber"]
        customer.address = data["address"]
        pdb.session.commit()
        log.log_crud(info="Put", table_name=f"Customers {id}")
        return jsonify(
            {
                "id": customer.id,
                "firstName": customer.firstName,
                "lastName": customer.lastName,
                "mail": customer.mail,
                "phoneNumber": customer.phoneNumber,
                "address": customer.address,
            },
            {"code": 200},
        )

    def delete(self, id):
        customer = Customer.query.get_or_404(id)
        pdb.session.delete(customer)
        pdb.session.commit()
        log.log_crud(info="Delete", table_name=f"Customers {id}")
        return jsonify(
            {"delete": id},
            {"code": 200},
        )
