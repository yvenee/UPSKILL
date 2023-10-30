from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///many_many.db'
db = SQLAlchemy(app)

authors_books = db.Table('authors_books',
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True)
)

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', secondary=authors_books, backref=db.backref('authors', lazy=True))

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    
with app.app_context():
    db.create_all()

    author1 = Author(name='Author 1')
    author2 = Author(name='Author 2')
    book1 = Book(title='Book 1')
    book2 = Book(title='Book 2')
    author1.books.append(book1)
    author2.books.append(book1)
    author2.books.append(book2)
    db.session.add(author1)
    db.session.add(author2)
    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()

@app.route('/')
def index():
    return render_template('index.html', authors=[author1, author2], books=[book1, book2])

if __name__ == '__main__':
    app.run(debug=True)
