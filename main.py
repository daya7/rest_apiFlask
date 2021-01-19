from flask import Flask, jsonify, request

app = Flask(__name__)

from books import books

#routes
#server initial test

@app.route('/')
def first():
    return jsonify({"message": "First ok"})
    
@app.route('/look')
def look():
    return jsonify({"message": "Ok, looking"})
    
#filedata
@app.route('/books')
def getBooks():
    return jsonify({"Books": books, "message": "Books List"})
    
#datafilter  
@app.route('/books/<string:book_name>')
def getBk(book_name):
  booking = [book for book in books if book['name'] == book_name]
  if (len(booking) > 0):
    return jsonify({"Book": booking[0]})
  return jsonify({"message": "Book not found"})
  
#adding
@app.route('/books', methods=['POST'])
def addBooks():
  new_book= {
    "name": request.json['name'],
    "author": request.json['author'],
    "year": request.json["year"]
  }
  books.append(new_book)
  return jsonify({"message": "Book added successfully", "Books": books})
  
#editing
@app.route('/books/<string:book_name>', methods=['PUT'])
def modfbook(book_name):
  booking = [book for book in books if book['name'] == book_name]
  if (len(booking) > 0):
      booking[0]['name'] = request.json['name']
      booking[0]['author'] = request.json['author']
      booking[0]['year'] = request.json['year']
      return jsonify({"message": "Book updated", "Book": booking[0]})
  return jsonify({"message": "Book does not register"})
  
#deleting
@app.route('/books/<string:book_name>', methods=['DELETE'])
def delbook(book_name):
  booking = [book for book in books if book['name'] == book_name]
  if (len(booking) > 0):
      books.remove(booking[0])
      return jsonify({"message": "Book deleted successfully", "Book": books})
  return jsonify({"message": "Book does not register"})


if __name__ == '__main__':
    
    app.run(debug=True, port=4000)
    