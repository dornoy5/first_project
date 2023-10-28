# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import CheckConstraint
# from sqlalchemy.orm import relationship

# db=SQLAlchemy()

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
