import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"


def readbooks():
    response = requests.get(URL)
    return response.json()


def createbook(book):
    response = requests.post(URL, json=book)
    return response.json()


def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    return response.json()


def updatebook(id, book):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()


def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


def averageprice():
    books = readbooks()
    total = 0
    count = 0

    for book in books:
        price = book.get("price")

        if price is not None:
            total += price
            count += 1

    return total / count


if __name__ == "__main__":
    newbook = {
        "title": "Sample Book",
        "author": "Sophia",
        "price": 200
    }

    createdbook = createbook(newbook)
    print("Created:", createdbook)

    bookid = createdbook["id"]

    updatedbook = {
        "title": "Updated Sample Book",
        "author": "Sophia",
        "price": 250
    }

    print("Updated:", updatebook(bookid, updatedbook))
    print("Read back:", readbook(bookid))
    print("Deleted:", deletebook(bookid))
    print("Average price:", averageprice())