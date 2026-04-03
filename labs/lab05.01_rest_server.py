from flask import Flask, request, abort

app = Flask(__name__)

books = [
    {"id": 1, "title": "Harry Potter", "author": "J.K. Rowling", "price": 20},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 15},
    {"id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "price": 12},
]


@app.route("/")
def index():
    return "Hello"


@app.route("/books", methods=["GET"])
def getall():
    return {"books": books}


@app.route("/books/<int:id>", methods=["GET"])
def findbyid(id):
    for book in books:
        if book["id"] == id:
            return book
    abort(404)


@app.route("/books", methods=["POST"])
def create():
    if not request.json:
        abort(400)

    new_book = {
        "id": books[-1]["id"] + 1 if books else 1,
        "title": request.json.get("title"),
        "author": request.json.get("author"),
        "price": request.json.get("price"),
    }

    books.append(new_book)
    return new_book, 201


@app.route("/books/<int:id>", methods=["PUT"])
def update(id):
    found_book = None
    for book in books:
        if book["id"] == id:
            found_book = book
            break

    if found_book is None:
        abort(404)

    if not request.json:
        abort(400)

    found_book["title"] = request.json.get("title", found_book["title"])
    found_book["author"] = request.json.get("author", found_book["author"])
    found_book["price"] = request.json.get("price", found_book["price"])

    return found_book


@app.route("/books/<int:id>", methods=["DELETE"])
def delete(id):
    for i, book in enumerate(books):
        if book["id"] == id:
            deleted_book = books.pop(i)
            return {"deleted": deleted_book}

    abort(404)


if __name__ == "__main__":
    app.run(debug=True)