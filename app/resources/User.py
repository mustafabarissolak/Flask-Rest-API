from flask import request, jsonify
from flask_restx import Resource, fields, Namespace
from app.Models.ModelsUser import Users
from app.Models.ModelsLogging import Logger


<<<<<<< HEAD
api_users = Namespace("Users")
=======
api_users = Namespace("Users", description="Operations related to Users")
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33

users_model = api_users.model(
    "Users",
    {
<<<<<<< HEAD
        "id": fields.Integer(readonly=True),
        "user_name": fields.String(required=True),
        "password": fields.String(required=True),
=======
        "id": fields.Integer(readonly=True, description="User Id"),
        "user_name": fields.String(required=True, description="User username"),
        "password": fields.String(required=True, description="User password"),
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33
    },
)

userIsLogin = False
log = Logger()


@api_users.route("/user_login")
class UserLogin(Resource):
    @api_users.expect(users_model)
    def post(self):
        try:
            global userIsLogin
            data = request.json

            login_user_name = data.get("user_name")
            login_user_password = data.get("password")

            user = Users.query.filter_by(
                user_name=login_user_name,
                password=login_user_password,
            ).first()

            if user:
                if not userIsLogin:
                    userIsLogin = True
                    log.log_users(f"{login_user_name} is login! ")
                    return jsonify(
                        {"message": f"{login_user_name} is login"},
<<<<<<< HEAD
                        {"code": 200},
=======
                        {"code": 201},
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33
                    )
                else:
                    log.log_users(f"{login_user_name} already logged in!")
                    return jsonify(
                        {"message": f"{login_user_name} already logged in"},
                        {"code": 200},
                    )
            else:
                log.log_error(
                    info=(
                        {"login_error": "Invalid credentials"},
                        {"user_name": login_user_name},
                        {"password": login_user_password},
<<<<<<< HEAD
                        {"code": 404},
                    )
                )
                return jsonify({"error": "Invalid credentials!"}, {"code": 404})
=======
                    )
                )
                return jsonify({"error": "Invalid credentials!"}, {"code": 401})
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33

        except Exception as e:
            log.log_error(e)
            return jsonify({"error": e})


@api_users.route("/user_logout")
class UserLogout(Resource):
    @api_users.expect(users_model)
    def post(self):
        global userIsLogin
        try:
            data = request.json
            logout_user_name = data.get("user_name")
            logout_user_password = data.get("password")

            user = Users.query.filter_by(
                user_name=logout_user_name, password=logout_user_password
            ).first()

            if user:
                if userIsLogin:
                    userIsLogin = False
                    log.log_users(f"{logout_user_name} logout")
                    return jsonify(
                        {"logout": logout_user_name},
                        {"code": 200},
                    )
                else:
                    log.log_users(f"{logout_user_name} already not logged in !")
                    return jsonify(
                        {"message": "User not logged in"},
                        {"code": 400},
                    )
            else:
                log.log_error({"logout_error": "Invalid credentials"})
<<<<<<< HEAD
                return (
                    jsonify(
                        {"error": "Invalid credentials"},
                    ),
=======
                return jsonify(
                    {"error": "Invalid credentials"},
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33
                    {"code": 401},
                )

        except Exception as e:
            log.log_error(e)
<<<<<<< HEAD
            return {"error": e}
=======
            return jsonify({"error": e})
>>>>>>> d41db3ffc0964435eebb9f199e89c9e928a36d33
