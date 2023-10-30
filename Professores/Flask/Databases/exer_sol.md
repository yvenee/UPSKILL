
### Exercise 1: Unique One-to-Many Relationship

#### File Structure:
```
/one_to_many_relationship
├── app.py
├── database.db
└── templates
    └── index.html
```

#### `app.py`:
```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Models
class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cities = db.relationship('City', backref='country', lazy=True)

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Sample data to test the relationship
country = Country(name='United States')
city1 = City(name='New York', country=country)
city2 = City(name='Los Angeles', country=country)

@app.route('/')
def index():
    return render_template('index.html', country=country)

if __name__ == '__main__':
    app.run(debug=True)
```

#### `templates/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Country and Cities</title>
</head>
<body>
    <h1>Country: {{ country.name }}</h1>
    <h2>Cities:</h2>
    <ul>
        {% for city in country.cities %}
            <li>{{ city.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Exercise 2: Diverse Many-to-One Relationship

#### File Structure:
```
/many_to_one_relationship
├── app.py
├── database.db
└── templates
    └── index.html
```

#### `app.py`:
```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Models
class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    department = db.relationship('Department', backref='employees')

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Sample data to test the relationship
department = Department(name='IT')\

employee1 = Employee(name='John Doe', department=department)
employee2 = Employee(name='Jane Smith', department=department)

@app.route('/')
def index():
    return render_template('index.html', department=department)

if __name__ == '__main__':
    app.run(debug=True)
```

#### `templates/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Employees and Department</title>
</head>
<body>
    <h1>Department: {{ department.name }}</h1>
    <h2>Employees:</h2>
    <ul>
        {% for employee in department.employees %}
            <li>{{ employee.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

Certainly! Let's proceed with Exercise 3: Unusual Many-to-Many Relationship.

### Exercise 3: Unusual Many-to-Many Relationship

#### File Structure:
```
/many_to_many_relationship
├── app.py
├── database.db
└── templates
    └── index.html
```

#### `app.py`:
```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Association Table for many-to-many relationship
authors_books = db.Table('authors_books',
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True)
)

# Models
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', secondary=authors_books, backref=db.backref('authors', lazy=True))

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Sample data to test the relationship
author1 = Author(name='Author 1')
author2 = Author(name='Author 2')
book1 = Book(title='Book 1')
book2 = Book(title='Book 2')
author1.books.append(book1)
author2.books.append(book1)
author2.books.append(book2)

@app.route('/')
def index():
    return render_template('index.html', authors=[author1, author2], books=[book1, book2])

if __name__ == '__main__':
    app.run(debug=True)
```

#### `templates/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Authors and Books</title>
</head>
<body>
    <h1>Authors and their Books</h1>
    <ul>
        {% for author in authors %}
            <li>{{ author.name }} wrote:
                <ul>
                    {% for book in author.books %}
                        <li>{{ book.title }}</li>
                    {% endfor %}
                </ul>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Exercise 4: Self-Referential Relationship

#### File Structure:
```
/self_referential_relationship
├── app.py
├── database.db
└── templates
    └── index.html
```

#### `app.py`:
```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Model for self-referential relationship
class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    manager = db.relationship('Employee', remote_side=[id], backref='subordinates')

# Create the database
with app.app_context():
    db.create_all()

# Sample data to test the relationship
manager = Employee(name='Manager')
employee1 = Employee(name='Employee 1', manager=manager)
employee2 = Employee(name='Employee 2', manager=manager)

@app.route('/')
def index():
    return render_template('index.html', manager=manager)

if __name__ == '__main__':
    app.run(debug=True)
```

#### `templates/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Employees and Manager</title>
</head>
<body>
    <h1>Manager: {{ manager.name }}</h1>
    <h2>Subordinates:</h2>
    <ul>
        {% for subordinate in manager.subordinates %}
            <li>{{ subordinate.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Exercise 5: Polymorphic Relationship

#### File Structure:
```
/polymorphic_relationship
├── app.py
├── database.db
└── templates
    └── index.html
```

#### `app.py`:
```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    likes = relationship('Like', back_populates='user', cascade='all, delete-orphan')

class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    likes = relationship('Like', back_populates='admin', cascade='all, delete-orphan')

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    likes = relationship('Like', back_populates='post', cascade='all, delete-orphan')

class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    liked_by_type = db.Column(db.String(50), nullable=False)
    liked_by_id = db.Column(db.Integer, nullable=False)
    
    post_id = db.Column(db.Integer, ForeignKey('posts.id'))
    post = relationship('Post', back_populates='likes')

    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='likes')

    admin_id = db.Column(db.Integer, ForeignKey('admins.id'))
    admin = relationship('Admin', back_populates='likes')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


#### `templates/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Users and Likes</title>
</head>
<body>
    <h1>Users and their Likes</h1>
    <ul>
        {% for user in users %}
            <li>{{ user.name }} likes:
                <ul>
                    {% for like in user.likes %}
                        <li>{{ like.liked_by.name if like.liked_by else 'Unknown' }}</li>
                    {% endfor %}
                </ul>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```
