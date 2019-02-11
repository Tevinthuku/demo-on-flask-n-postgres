from flask import request, make_response, jsonify

from app.api.v2 import version2

from app.api.v2.models.books import Book

@version2.route("/book", methods=["POST"])
def newbook():
    try:
        data = request.get_json()
        name = data["name"]
        author = data["author"]
    except:
        return make_response(jsonify({ "status": 400, "error": "keys are absent" }), 400)

    book = Book(name=name, author=author)
    book.save_book()

    return make_response(jsonify({ "status": 201, "data": "Book has been created" }), 201)