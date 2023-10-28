# from datetime import timedelta
# import datetime
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import CheckConstraint, ForeignKeyConstraint
# from sqlalchemy.orm import relationship

# db=SQLAlchemy()

# class Customer(db.Model):
#     __tablename__ = 'customers'

#     id = db.Column(db.Integer, primary_key=True)
#     customer_id= db.Column(db.String(20), nullable=False)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     phone_num = db.Column(db.String(20), nullable=False)
#     address = db.Column(db.String(200), nullable=False)
#     loans = db.relationship('Loan', backref='customer', lazy=True)

#     loans = relationship('Loan', backref='customer', lazy=True, cascade='all, delete-orphan')
#     __table_args__ = (
#         CheckConstraint('LENGTH(title) > 0', name='check_title_nonempty'),
#     )
 

#     def __repr__(self):
#         return f"Customer('{self.customer_id}''{self.first_name}, {self.last_name}', '{self.phone_num}','{self.address}')"

# class Book(db.Model):
#     __tablename__ = 'books'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     author = db.Column(db.String(100), nullable=False)
#     category = db.Column(db.String(50), nullable=False)
#     loans = db.relationship('Loan', backref='book', lazy=True)
#     quantity = db.Column(db.Integer, default=1)  # Total copies of the book
#     available_quantity = db.Column(db.Integer, default=1)  # Copies available for loan

#     __table_args__ = (
#         CheckConstraint('LENGTH(title) > 0', name='check_title_nonempty'),
#     )

#     # Establish a one-to-many relationship with loans (the 'cascade' needed to be able to delete a book with a loan record)
#     loans = relationship('Loan', backref='book', lazy=True, cascade='all, delete-orphan')

# class Loan(db.Model):
#     __tablename__ = 'loans'
#     id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
#     book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
#     date_of_loan = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     date_of_return = db.Column(db.DateTime, nullable=False)
#     loan_type = db.Column(db.String(10), nullable=False)
#     is_finished = db.Column(db.Boolean, default=False, nullable=False)

#     __table_args__ = (
#         ForeignKeyConstraint(['book_id'], ['books.book_id']),
#         ForeignKeyConstraint(['customer_id'], ['customers.customer_id']),
#     )
#     def __repr__(self):
#         return f"Loan('{self.customer_id}',
#           '{self.book_id}',
#             '{self.date_of_loan}',
#               '{self.date_of_return}', '{self.is_finished}')"

#     def set_return_date(self):
#         if self.loan_type == '3 days':
#             self.date_of_return = self.date_of_loan + timedelta(days=3)
#         elif self.loan_type == 'week':
#               self.date_of_return = self.date_of_loan + timedelta(weeks=1)
