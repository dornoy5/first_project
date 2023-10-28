from flask import Blueprint, request , jsonify
from project1 import db
from project1.modelim import Book

books = Blueprint('books', __name__)

@books.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()

    book_list = [{'name': book.name, 'author': book.author, 'category': book.category, 
                'Total copies of the book': book.quantity,
                'Copies available for loan': book.available_quantity, 
                'book Type': book.category} for book in books]

    return jsonify({'books': book_list})

@books.route('/books', methods=['POST'])
def new_books():
    data = request.get_json()

    # Validate that required fields are present in the request data
    if 'name' not in data or 'author' not in data or 'category' not in data:
        return jsonify({'error': 'Required fields are missing in the request data (must be: name, author and category)'}, 400)
    
    name = data['name']
    author = data['author']
    category = data['category']
    quantity = data['quantity']
    
    # Validate that the name is not an empty string
    if not name:
        return jsonify({'error': 'name cannot be empty.'}), 400

    #Validation for category
    if category not in [1, 2, 3]:
        return jsonify({'error': 'Invalid category. It must be 1, 2, or 3'}, 400)
    
    quantity = data.get('quantity',1)
    new_book = Book(name=name, author=author, category=category, quantity=quantity, available_quantity=quantity)
    db.session.add(new_book)
    db.session.commit()

    return jsonify({'message': 'Book created successfully!'})

@books.route('/books/<int:book_id>/update', methods=['GET', 'POST'])
def update_book(bookID):
    data = request.get_json()
    new_name = data.get('name')
    new_author = data.get('author')
    new_category = data.get('category')
    new_quantity = data.get('quantity')

    # validate that this book exists
    book = Book.query.get(bookID)
    if book:
        #check for each object if exists, to allow edit just some of the book objects
        if new_name is not None:
            book.name = new_name
        if new_author is not None:
            book.author = new_author
        if new_category is not None:
            book.category = new_category
        if new_category is not None:
            book.category = new_category
        if new_quantity is not None:
            book.quantity = new_quantity

        db.session.commit()

        return jsonify({'message': 'Book updated successfully'})
    else:
        return jsonify({'error': 'Book not found'}, 404)

@books.route('/books/<int:bookID>', methods=['DELETE'])
def delete_book(bookID):
    #check if the book exists
    book = Book.query.get(bookID)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'error': 'Book not found'}, 404)