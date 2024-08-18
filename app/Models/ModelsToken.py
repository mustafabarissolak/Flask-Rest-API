import jwt
from flask import request, make_response, jsonify
from datetime import datetime, timedelta, timezone


class UserToken:
    def __init__(self, user_id):
        self.id = user_id

    def get_token(self, expires=600):
        payload = {
            "user_id": self.id,
            "exp": datetime.now(timezone.utc) + timedelta(seconds=expires),
            "used": False,
        }
        return jwt.encode(payload, "SECRET-KEY", algorithm="HS256")

    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(token, "SECRET-KEY", algorithms=["HS256"])
            if datetime.now(timezone.utc) <= datetime.fromtimestamp(
                payload["exp"], timezone.utc
            ) and not payload.get("used", False):
                return payload["user_id"]
            else:
                return None
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            print("2")
            return None


def token_required(token_info):
    def decorator(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return make_response(jsonify({"message": "Token is missing"}), 403)

        user_id = UserToken.verify_token(token)
        if not user_id:
            return make_response(jsonify({"message": "Invalid or expired token"}), 401)
        return token_info(user_id=user_id, *args, **kwargs)

    return decorator
