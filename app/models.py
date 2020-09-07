from app import db
import enum

class Book(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(100))
    quantity = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    rental_id = db.Column(db.Integer, db.ForeignKey('rental.id'))

    def __str__(self):
        return f"Book {self.tittle}"

class Author(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    books = db.relationship("Book", backref="author_name")

    def __str__(self):
        return f"Author {self.name}"

class Status_Enum(enum.Enum):
    available = 'available'
    not_available = 'not_available'


class Rental(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(Status_Enum), default=Status_Enum.available)
    books = db.relationship("Book", backref="rental_status")

    def __str__(self):
        return f"Book is {self.status}"


class Shopping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(50))
    quantity = db.Column(db.Integer)


