from flask import Blueprint, render_template


render= Blueprint('render', __name__)

@render.route('/books')
def index():
    return render_template('books/index.html')

@render.route('/customers')
def index():
    return render_template('customers/index.html')


@render.route('/loans')
def index():
    return render_template('loans/index.html')