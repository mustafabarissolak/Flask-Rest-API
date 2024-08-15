from flask import request, jsonify
from flask_restx import Resource, fields, Namespace
from app.Models.ModelsUser import Users
from app.Models.ModelsLogging import Logger


api_users = Namespace("users")


users_model = api_users.model(
    "Users",
    {
        "id": fields.Integer(readonly=True, description="User Id"),
        "user_name": fields.String(required=True, description="User username"),
        "password": fields.String(required=True, description="User password"),
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
                        {"message": f"{login_user_name} is login"}, {"code": 200}
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
                        {"code": 404},
                    )
                )
                return jsonify({"error": "Invalid credentials!"}, {"code": 404})

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
                return (
                    jsonify(
                        {"error": "Invalid credentials"},
                    ),
                    {"code": 401},
                )

        except Exception as e:
            log.log_error(e)
            return {"error": e}


from flask import request, jsonify
from flask_restx import Resource, fields, Namespace
from app.Models.ModelsUser import Users
from app.Models.ModelsLogging import Logger
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api_users = Namespace("users")
log = Logger()

users_model = api_users.model(
    "Users",
    {
        "id": fields.Integer(readonly=True, description="User Id"),
        "user_name": fields.String(required=True, description="User username"),
        "password": fields.String(required=True, description="User password"),
    },
)


@api_users.route("/user_login")
class UserLogin(Resource):
    @api_users.expect(users_model)
    def post(self):
        try:
            data = request.json
            login_user_name = data.get("user_name")
            login_user_password = data.get("password")

            user = Users.query.filter_by(
                user_name=login_user_name,
                password=login_user_password,
            ).first()

            if user:
                # JWT token oluşturma
                access_token = create_access_token(identity=login_user_name)
                log.log_users(f"{login_user_name} is login!")
                return jsonify(
                    access_token=access_token,
                    message=f"{login_user_name} is login",
                    code=200,
                )
            else:
                log.log_error(
                    info={
                        "login_error": "Invalid credentials",
                        "user_name": login_user_name,
                        "password": login_user_password,
                        "code": 404,
                    }
                )
                return jsonify(error="Invalid credentials!", code=404)

        except Exception as e:
            log.log_error(e)
            return jsonify(error=str(e))


@api_users.route("/user_logout")
class UserLogout(Resource):
    @jwt_required()  # Kullanıcı sadece oturum açtıysa bu işlemi yapabilir
    def post(self):
        try:
            current_user = get_jwt_identity()
            log.log_users(f"{current_user} has logged out")
            return jsonify(message=f"{current_user} logged out", code=200)

        except Exception as e:
            log.log_error(e)
            return jsonify(error=str(e))
