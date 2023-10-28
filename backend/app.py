
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,template_folder="../../frontend/html", static_folder='../../frontend/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)

from project1.books import books
from project1.customers import customers
from project1.loans import loans


# Register the blueprints with the Flask app
app.register_blueprint(books)
app.register_blueprint(customers)
app.register_blueprint(loans)

if __name__ == "__main__":
    app.run(debug=True)
