from flask import request, jsonify
from flask_restx import Resource, fields, Namespace
from datetime import datetime, timedelta, UTC
import jwt
from app.Models.ModelsUser import Users
from app.Models.ModelsLogging import Logger
from app.Models.ModelsToken import token_required


api_users = Namespace("users")

users_model = api_users.model(
    "Users",
    {
        "id": fields.Integer(readonly=True, description="User Id"),
        "user_name": fields.String(required=True, description="User username"),
        "password": fields.String(required=True, description="User password"),
    },
)


log = Logger()


class UserToken:
    def __init__(self, user_id):
        self.id = user_id

    def get_token(self, expires=600):
        payload = {
            "user_id": self.id,
            "exp": datetime.now(UTC) + timedelta(seconds=expires),
            "used": False,
        }
        return jwt.encode(payload, "SECRET-KEY", algorithm="HS256")

    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(token, "SECRET-KEY", algorithms=["HS256"])
            if (
                datetime.now(UTC) <= datetime.fromtimestamp(payload["exp"], UTC)
                and not payload["used"]
            ):
                user_id = payload["user_id"]
                payload["used"] = True
                return user_id
            else:
                return None

        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None


userIsLogin = False


@api_users.route("/user_login")
class UserLogin(Resource):
    @api_users.expect(users_model)
    def post(self):
        global userIsLogin
        try:
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
                    log.log_users(f"{login_user_name} is login!")
                    user_token = UserToken(user.id)
                    token = user_token.get_token()
                    return jsonify(
                        {
                            "message": "login",
                            "user_name": login_user_name,
                            "token": token,
                            "code": 200,
                        }
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
            return jsonify({"error": str(e)})


@api_users.route("/user_logout")
class UserLogout(Resource):
    @api_users.doc(security="apikey")
    @token_required
    def post(self, user_id):
        global userIsLogin
        try:
            token = request.headers.get("Authorization")
            user_id = UserToken.verify_token(token)

            if user_id:
                if userIsLogin:
                    userIsLogin = False
                    log.log_users(f"User {user_id} logout")
                    return jsonify(
                        {"logout": f"User {user_id} logged out"},
                        {
                            "code": 200,
                            "user id": user_id,
                        },
                    )
                else:
                    log.log_users("User already not logged in!")
                    return jsonify(
                        {"message": "User not logged in"},
                        {
                            "code": 400,
                            "user id": user_id,
                        },
                    )
            else:
                log.log_error({"logout_error": "Invalid token"})
                return jsonify(
                    {"error": "Invalid token"},
                    {
                        "code": 401,
                        "user id": user_id,
                    },
                )

        except Exception as e:
            log.log_error(e)
            return jsonify({"error": str(e)})
