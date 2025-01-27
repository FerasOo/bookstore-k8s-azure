from application import app, bookstore
from flask import jsonify, render_template, url_for, redirect, request
from bson import ObjectId

@app.route('/', methods=['GET'])
def index():
    all_books = bookstore.find() 
    return render_template('index.html', books=all_books)

@app.route('/book/<id>', methods=['GET', 'HEAD', 'DELETE', 'PUT'])
def get_book(id):
  if request.method == 'HEAD':
    book_exists = bookstore.count_documents({"_id": ObjectId(id)}) > 0
    if book_exists:
      return '', 204  # No Content
    else:
      return '', 404  # Not Found
  if request.method == 'GET':
    #find book and display it in info.html
    book = bookstore.find_one({"_id": ObjectId(id)})
    if book:
      return render_template('info.html', book=book)
    else:
      return "Book not found", 404
  elif request.method == 'DELETE':
    result = bookstore.find_one_and_delete({"_id": ObjectId(id)})
    if result:
      return jsonify({"success": True})
    else:
      return jsonify({"error": "Book not found or already deleted"}), 404
  elif request.method == 'PUT':
    # Retrieve the updated data from the request
    updated_data = {}
    for k in ['title', 'isbn', 'year', 'category', 'page', 'price']:
      if request.json[k] != '':
        updated_data[k] = request.json[k]
    # if request.json['authorFirstName'] != '' or request.json['authorLastName'] != '':
    #   updated_data['author'] = {}
      if request.json['authorFirstName'] != '':
        updated_data['author.firstName'] = request.json['authorFirstName']
      if request.json['authorLastName'] != '':
        updated_data['author.lastName'] = request.json['authorLastName']
      if request.json['publisherName'] != '':
        updated_data['publisher.name'] = request.json['publisherName']
  
    #   print(updated_data)
    result = bookstore.update_one({"_id": ObjectId(id)}, {"$set": updated_data})

    if result.matched_count > 0:
      return jsonify({"success": True}), 200
    else:
      return jsonify({"error": "Book not found or unable to update"}), 404


@app.route('/book/isbn/<id>', methods=['GET'])
def get_book_by_isbn(id):
  if request.method == 'GET':
    #find book and display it in info.html
    book = bookstore.find_one({"isbn": id})
    if book:
      return render_template('info.html', book=book)
    else:
      return "Book not found", 404
    
@app.route('/book', methods=['GET', 'POST'])
def add_book():
  if request.method == "GET":
    return render_template('form.html')
  else:
    new_book = {
      'title': request.form['title'],
      'isbn': request.form['isbn'],
      'year': request.form['year'],
      'category': request.form['category'],
      'page': request.form['page'],
      'author': {
        'firstName': request.form['authorFirstName'],
        'lastName': request.form['authorLastName'],
      },
      'publisher': {
        'name':request.form['publisherName']
        },
      'price': request.form['price'],
    }
    bookstore.insert_one(new_book)
    return redirect('/')
  #  bookstore