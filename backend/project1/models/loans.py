# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import ForeignKeyConstraint
# from datetime import datetime, timedelta

# db=SQLAlchemy()

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

