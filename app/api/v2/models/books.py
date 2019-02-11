from . import db
from flask import jsonify, make_response

class Book():
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def save_book(self):
        save_book_query = """
        INSERT INTO books(name, author) VALUES(
            '{}', '{}'
        )""".format(self.name, self.author)

        db.query_data_from_db(save_book_query)
