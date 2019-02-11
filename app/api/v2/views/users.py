from flask import request, make_response, jsonify
from app.api.v2 import version2

from app.api.v2.models.users import User

@version2.route("/auth/signup", methods=["POST"])
def CreateAccount():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        retypedpassword = data["retrypedpassword"]
    except:
        return make_response(jsonify({
            "status": 400,
            "error":"not valid keys"
        }), 400)

    if password != retypedpassword:
        return make_response(jsonify({
            "status": 400,
            "error": "passwords dont match"
        }))

    user = User(email=email, password=password)

    user.save_user()

    return make_response(jsonify({"status": 201, "data": "User Registered Successfully!"}), 201)


    