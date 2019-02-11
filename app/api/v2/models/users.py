from . import db
from flask import jsonify, make_response

class User():
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def save_user(self):
        # USERS_LEN.append(self)
        save_user_query = """
        INSERT INTO users(email, password) VALUES(
            '{}', '{}'
        )""".format(self.email, self.password)

        db.query_data_from_db(save_user_query)

        return make_response(jsonify({"status": 201, "data": "User Registered Successfully!"}), 201)
