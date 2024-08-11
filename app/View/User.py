from flask import request, jsonify
from flask_restx import Resource, fields, Namespace
from app.Models.User import Users

# Model tanım
api_users = Namespace("Users", description="Operations related to Users")

users_model = api_users.model(
    "Users",
    {
        "Id": fields.Integer(readonly=True, description="User Id"),
        "user_name": fields.String(required=True, description="User username"),
        "password": fields.String(required=True, description="User password"),
    },
)

userIsLogin = False


@api_users.route("/user_login")
class UserLogin(Resource):
    @api_users.expect(users_model)
    def post(self):
        global userIsLogin
        # JSON verilerini al
        data = request.json

        userUserName = data.get("user_name")
        userPassword = data.get("password")

        # Kullanıcıyı veritabanında bul
        user = Users.query.filter_by(
            user_name=userUserName, password=userPassword
        ).first()

        if user:
            if not userIsLogin:
                # logger("login", "Login başarılı", userUserName)
                userIsLogin = True
                return jsonify({"login": userUserName, "code": 201})
            else:
                # logger("login", "Kullanıcı zaten login", userUserName)
                return jsonify({"message": "Kullanıcı zaten login", "code": 200})
        else:
            # logger("login", "Login başarısız", userUserName)
            return jsonify({"error": "Kullanıcı bulunamadı", "code": 401})


@api_users.route("/user_logout")
class UserLogout(Resource):
    @api_users.expect(users_model)
    def post(self):
        global userIsLogin
        # JSON verilerini al
        data = request.json
        userUserName = data.get("user_name")
        userPassword = data.get("password")

        # Kullanıcıyı veritabanında bul
        user = Users.query.filter_by(
            user_name=userUserName, password=userPassword
        ).first()

        if user:
            if userIsLogin:
                # logger("logout", "Logout başarılı", userUserName)
                userIsLogin = False
                return jsonify({"logout": userUserName, "code": 200})
            else:
                # logger("logout", "Kullanıcı login değil", userUserName)
                return jsonify({"message": "Kullanıcı login değil", "code": 400})
        else:
            # logger("logout", "Logout başarısız", userUserName)
            return jsonify({"error": "Invalid credentials", "code": 401})


