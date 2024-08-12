from flask_restx import Resource, fields, Namespace
from app import pdb
from app.Models import Customer
from app.Models.ModelsLogging import Logger
from flask import request, jsonify


<<<<<<< HEAD
api_customer = Namespace("Customers")
=======
api_customer = Namespace("Customers", description="Operations related to Customers")
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33

customer_model = api_customer.model(
    "Customer",
    {
        "id": fields.Integer(readonly=True),
        "name": fields.String(required=True),
        "firstName": fields.String(required=True),
        "mail": fields.String(required=True),
        "phoneNumber": fields.String(required=True),
        "address": fields.String(required=True),
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
            ],
            {"code": 200},
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
<<<<<<< HEAD
            },
            {"code": 200},
=======
            }
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33
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
<<<<<<< HEAD
            },
            {"code": 200},
=======
            }
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33
        )

    def delete(self, id):

        customer = Customer.query.get_or_404(id)
        pdb.session.delete(customer)
        pdb.session.commit()
        log.log_crud(info="Delete", table_name=f"Customers {id}")
<<<<<<< HEAD
        return jsonify(
            {"delete": id},
            {"code": 200},
        )
=======
        return "", 204
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33
