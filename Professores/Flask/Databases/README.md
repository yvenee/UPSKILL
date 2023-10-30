The URI (Uniform Resource Identifier) formats for connecting to PostgreSQL, MongoDB, and Redis databases can vary based on the specific database technology and the configuration of the server where the database is hosted.

### PostgreSQL URI:

The URI format for connecting to a PostgreSQL database typically follows this structure:

```
postgresql://username:password@host:port/database
```

Here's an example URI:

```
postgresql://myusername:mypassword@localhost:5432/mydatabase
```

### MongoDB URI:

The URI format for connecting to a MongoDB database using the standard connection string typically looks like this:

```
mongodb://username:password@host:port/database
```

Here's an example URI:

```
mongodb://myusername:mypassword@localhost:27017/mydatabase
```

### Redis URI:

For Redis, the connection typically doesn't involve a username and password but rather a host and port:

```
redis://host:port
```

Here's an example URI:

```
redis://localhost:6379
```

### Code Differences in Flask:

When using these URIs in a Flask application to connect to databases, the main difference lies in how you configure the database connection in your Flask application configuration.

For PostgreSQL with SQLAlchemy, you might set the URI like this:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@host:port/database'
```

For MongoDB with PyMongo, you would configure it this way:

```python
app.config['MONGO_URI'] = 'mongodb://username:password@host:port/database'
```

For Redis with Redis-Py, you would configure it this way:

```python
app.config['REDIS_URL'] = 'redis://host:port'
```

Depending on the specific libraries you're using (e.g., SQLAlchemy for PostgreSQL, PyMongo for MongoDB, Redis-Py for Redis), you would then set up the respective connection and use it in your Flask application accordingly.

---

Step-by-step guide to using CRUD operations (Create, Read, Update, Delete) with SQLAlchemy in Python for a Flask application. We'll use a SQLite database for demonstration purposes, but you can adapt it for other production databases like PostgreSQL, MySQL, or Oracle.

### Step 1: Set up the Flask Application
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@host:port/database'
db = SQLAlchemy(app)
```

### Step 2: Create a Model
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
```

### Step 3: Initialize the Database
```python
with app.app_context():
    db.create_all()
```

### Step 4: Implement CRUD Operations

#### Create (POST)
```python
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201
```

#### Read (GET)
```python
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = [{'name': user.name, 'email': user.email} for user in users]
    return jsonify(result), 200
```

#### Update (PUT)
```python
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200
```

#### Delete (DELETE)
```python
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200
```

### Step 5: Run the Flask Application
```python
if __name__ == '__main__':
    app.run(debug=True)
```
---
To restrict access to a database entry without actually deleting it (often referred to as "soft deletion"), you can use a flag or a status field in your database table to mark the entry as inactive or deleted. This way, you can prevent users from accessing or modifying the entry while retaining the information in the database.

Here's a step-by-step approach to implementing this in SQLAlchemy and Flask:

### Step 1: Add a Status Field to the Model

Add a field to your model to represent the status of the entry (e.g., active, inactive, deleted). This field will be used to mark the entry's status.

```python
from sqlalchemy import Column, Integer, String, Boolean

class YourModel(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)  # Flag to indicate if the entry is active or not

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True
```

### Step 2: Create Functions to Deactivate and Activate Entries

In the model, create functions to deactivate and activate the entry based on the status field.

```python
class YourModel(db.Model):
    # ... (existing code)

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True
```

### Step 3: Use Deactivate and Activate Functions as Needed

Whenever you want to "delete" an entry, you'll call the `deactivate()` function to set the status to inactive.

```python
# Example usage
entry = YourModel.query.get(entry_id)
entry.deactivate()
db.session.commit()
```

If you want to allow access again, you can call the `activate()` function to set the status back to active.

```python
# Example usage to activate
entry = YourModel.query.get(entry_id)
entry.activate()
db.session.commit()
```

By using this approach, the entry remains in the database, but its status is used to control access and behavior within your application.

---

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # Update for production DB
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

with app.app_context():
    db.create_all()

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = [{'name': user.name, 'email': user.email} for user in users]
    return jsonify(result), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

---

There are several popular database technologies that you can use with a Flask application. I'll provide examples for three different types: PostgreSQL (a relational database), MongoDB (a NoSQL database), and Redis (a key-value store).

### 1. PostgreSQL (Relational Database)

#### Step 1: Install the necessary package
Ensure you have `psycopg2` installed, which is a PostgreSQL adapter for Python.

```bash
pip install psycopg2-binary
```

#### Step 2: Configure Flask App for PostgreSQL

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'  # Replace with your PostgreSQL connection details
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
```

### 2. MongoDB (NoSQL Database)

#### Step 1: Install the necessary package
Install `pymongo`, the official Python driver for MongoDB.

```bash
pip install pymongo
```

#### Step 2: Configure Flask App for MongoDB

```python
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dbname'  # Replace with your MongoDB connection details
mongo = PyMongo(app)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    users_collection = mongo.db.users
    user_id = users_collection.insert_one({'name': data['name'], 'email': data['email']}).inserted_id
    return jsonify({'message': 'User created successfully', 'user_id': str(user_id)}), 201
```

### 3. Redis (Key-Value Store)

#### Step 1: Install the necessary package
Install `redis` for interacting with a Redis server.

```bash
pip install redis
```

#### Step 2: Use Redis in Flask App

```python
from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379)  # Replace with your Redis server details

@app.route('/counter', methods=['GET'])
def get_counter():
    counter_value = redis_client.get('counter')
    return f'Counter value: {counter_value}'

@app.route('/counter', methods=['POST'])
def increment_counter():
    current_value = redis_client.incr('counter')
    return f'Counter incremented. Current value: {current_value}'
```

---
Comparison of PostgreSQL (a relational database), MongoDB (a NoSQL database), and Redis (a key-value store) in terms of their differences, strengths, and weaknesses.

### PostgreSQL (Relational Database):

#### Differences:
1. **Data Model:**
   - Relational databases like PostgreSQL use a structured data model based on tables, with defined relationships between entities.
  
2. **Query Language:**
   - Utilizes SQL (Structured Query Language) for querying and manipulating data.
  
3. **Schema:**
   - Requires a predefined schema, meaning the structure of the data (table, columns, types) is defined before inserting data.

#### Strengths:
1. **ACID Compliance:**
   - Provides strong ACID (Atomicity, Consistency, Isolation, Durability) compliance, ensuring data integrity even in the face of failures.
  
2. **Complex Queries:**
   - Supports complex queries and transactions, making it ideal for applications that require complicated relationships between data.

3. **Joins:**
   - Efficiently handles joins between related tables, allowing for complex data retrieval.

#### Weaknesses:
1. **Scalability:**
   - Traditional relational databases can face challenges with horizontal scalability (scaling across multiple machines) compared to some NoSQL databases.

2. **Performance for Certain Use Cases:**
   - In high-velocity, read-heavy applications, NoSQL databases might outperform PostgreSQL due to their simpler data models.

### MongoDB (NoSQL Database):

#### Differences:
1. **Data Model:**
   - Utilizes a document-based, key-value data model which is flexible and allows for more complex, hierarchical data structures.
  
2. **Query Language:**
   - Uses a query language similar to JavaScript for querying and manipulation, allowing for a more dynamic approach compared to SQL.

3. **Schema:**
   - Is schema-less, meaning each document (equivalent to a row in a relational DB) can have a different structure.

#### Strengths:
1. **Flexibility:**
   - Offers greater flexibility in data modeling, making it suitable for evolving schemas and semi-structured or unstructured data.

2. **Scalability:**
   - Typically excels in horizontal scalability and distributed database systems, handling a high volume of read and write operations.

3. **Performance for Read-Heavy Operations:**
   - Often performs well for read-heavy operations due to its ability to retrieve entire documents in one query.

#### Weaknesses:
1. **Consistency:**
   - In some configurations, MongoDB may prioritize performance over strict consistency, leading to eventual consistency rather than immediate consistency.

2. **Learning Curve:**
   - Developers familiar with SQL may need time to adjust to the NoSQL way of querying and thinking about data.

### Redis (Key-Value Store):

#### Differences:
1. **Data Model:**
   - Uses a simple key-value data model, where each value is associated with a unique key.

2. **Query Language:**
   - Typically offers basic operations such as `GET`, `SET`, and other commands for more advanced data types.

3. **Schema:**
   - Is schema-less and can store various types of data, including strings, hashes, lists, sets, and more.

#### Strengths:
1. **Speed:**
   - Offers extremely fast read and write operations due to its in-memory nature and direct key-based access.

2. **Caching:**
   - Commonly used for caching frequently accessed data, improving application performance by reducing load on primary databases.

3. **Real-Time Applications:**
   - Ideal for real-time applications like leaderboards, session management, and pub/sub systems due to its low latency and high throughput.

#### Weaknesses:
1. **Durability:**
   - Being an in-memory database, it may not provide the same level of durability as disk-based databases like PostgreSQL, especially during system failures.

2. **Limited Query Capabilities:**
   - Designed primarily for simple operations based on keys and lacks the complex querying capabilities of relational databases.

In summary, the choice of database technology depends on the specific requirements of your application, including data structure, scalability needs, consistency requirements, performance expectations, and ease of development. PostgreSQL offers strong consistency and complex queries, MongoDB provides flexibility and scalability, while Redis excels in speed and caching for real-time applications. Consider the trade-offs and align your choice with your application's needs.

---
In SQLAlchemy, the `lazy` parameter is used to specify how related items should be loaded from the database. The `lazy` parameter accepts different values, each representing a different loading strategy. Here are the common lazy-loading options:

1. **'select' (default):** Loads the related items as needed when they are accessed. It uses individual SELECT statements to load the related items one by one.

2. **'joined':** Loads the related items using a SQL JOIN statement. It's efficient when querying and loading multiple related items.

3. **'subquery':** Similar to 'joined', but uses a subquery to load the related items.

4. **'dynamic':** Returns a `Query` object that can be further refined before execution. It allows for more complex queries to be built by chaining additional filters or options.

Let's demonstrate each of these lazy-loading strategies with a brief example.

### Example: Lazy Loading Strategies

```python
from sqlalchemy.orm import relationship

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    
    # Using 'select' (default) lazy loading
    children_select = relationship('Child', lazy='select')

    # Using 'joined' lazy loading
    children_joined = relationship('Child', lazy='joined')

    # Using 'subquery' lazy loading
    children_subquery = relationship('Child', lazy='subquery')

    # Using 'dynamic' lazy loading
    children_dynamic = relationship('Child', lazy='dynamic')
```

In this example, we've defined a `Parent` model with different lazy-loading strategies for its relationship with a `Child` model. Depending on your use case and performance requirements, you can choose the appropriate lazy-loading strategy.

---
Different types of relationships between databases in a web application. We'll use a Flask web framework and SQLAlchemy for database interactions.

### Example 1: One-to-Many Relationship

**Objective:**
Create a simple blog where one user can have multiple blog posts.

#### Step 1: Set up the Flask Application and Database

Follow the steps mentioned in the previous examples to set up a Flask application and configure a PostgreSQL or SQLite database.

#### Step 2: Define Models

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```

#### Step 3: Run the Application

Run the application and use the defined models to create users and blog posts, establishing a one-to-many relationship between users and posts.

### Example 2: Many-to-Many Relationship

**Objective:**
Create a system where users can have multiple roles.

#### Step 1: Update Models

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    roles = db.relationship('Role', secondary='user_role', backref=db.backref('users', lazy=True))

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Association Table for Many-to-Many Relationship
user_role = db.Table('user_role',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)
```

#### Step 2: Run the Application

Run the application and create users with multiple roles, establishing a many-to-many relationship between users and roles.

### Example 3: One-to-One Relationship

**Objective:**
Create a system where each user has a single profile.

#### Step 1: Update Models

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    profile = db.relationship('Profile', backref='user', uselist=False, lazy=True)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
```

#### Step 2: Run the Application

Run the application and create users with individual profiles, establishing a one-to-one relationship between users and profiles.

### Example 4: Self-Referential Relationship

**Objective:**
Create a system where users can follow other users.

#### Step 1: Update Models

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    followers = db.relationship('User', secondary='followers',
                               primaryjoin=(id == followers.c.followed_id),
                               secondaryjoin=(id == followers.c.follower_id),
                               backref=db.backref('following', lazy='dynamic'), lazy='dynamic')

# Association Table for Self-Referential Relationship
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)
```

#### Step 2: Run the Application

Run the application and allow users to follow other users, establishing a self-referential relationship.

### Example 5: Polymorphic Relationship

**Objective:**
Create a system where various types of content (e.g., posts, comments) can be liked.

#### Step 1: Update Models

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import polymorphic_identity

Base = declarative_base()

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    liked_item_id = Column(Integer, nullable=False)
    liked_item_type = Column(String(50), nullable=False)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    content = Column(String(200))

    likes = relationship(Like, backref='liked_post', primaryjoin="and_(Post.id==Like.liked_item_id, Like.liked_item_type=='post')")

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(200))

    likes = relationship(Like, backref='liked_comment', primaryjoin="and_(Comment.id==Like.liked_item_id, Like.liked_item_type=='comment')")
```

#### Step 2: Run the Application

Run the application and allow users to like posts and comments, establishing a polymorphic relationship.

---

1. Create a folder structure like this:
   ```
   /your_project_folder
   ├── app.py
   ├── templates
   │   └── index.html
   └── models.py
   ```

2. Populate `app.py`:
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/create_post', methods=['POST'])
def create_post():
    data = request.form
    new_post = Post(title=data['title'], content=data['content'], user_id=data['user_id'])
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

3. Populate `templates/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Blog</title>
</head>
<body>
    <h1>Blog</h1>
    <form action="/create_post" method="POST">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title"><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content"></textarea><br>
        <label for="user_id">User ID:</label><br>
        <input type="number" id="user_id" name="user_id"><br><br>
        <input type="submit" value="Create Post">
    </form>
    <h2>Users</h2>
    <ul>
        {% for user in users %}
            <li>
                User ID: {{ user.id }}, Name: {{ user.name }}
                <ul>
                    {% for post in user.posts %}
                        <li>
                            Post ID: {{ post.id }}, Title: {{ post.title }}, Content: {{ post.content }}
                        </li>
                    {% endfor %}
                </ul>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

4. Run the application:
   ```
   python app.py
   ```

---

More complex example involving a multi-page web application with various relationships and features. In this example, we'll create a platform for managing books, authors, and genres.

1. Folder structure:
   ```
   /your_project_folder
   ├── app.py
   ├── templates
   │   ├── index.html
   │   ├── book_form.html
   │   └── author_form.html
   ├── models.py
   └── database.db
   ```

2. Populate `models.py`:
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
```

3. Populate `app.py`:
```python
from flask import Flask, render_template, request, redirect, url_for
from models import db, Author, Book, Genre

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/')
def index():
    authors = Author.query.all()
    genres = Genre.query.all()
    return render_template('index.html', authors=authors, genres=genres)

@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        new_author = Author(name=name)
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('author_form.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author_id = request.form['author']
        genre_id = request.form['genre']
        new_book = Book(title=title, author_id=author_id, genre_id=genre_id)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))
    authors = Author.query.all()
    genres = Genre.query.all()
    return render_template('book_form.html', authors=authors, genres=genres)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

4. Populate HTML templates (`templates/index.html`, `templates/author_form.html`, `templates/book_form.html`) with appropriate content and forms.


### `templates/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Book Management</title>
</head>
<body>
    <h1>Book Management</h1>

    <h2>Authors</h2>
    <ul>
        {% for author in authors %}
            <li>{{ author.name }}</li>
        {% endfor %}
    </ul>

    <h2>Genres</h2>
    <ul>
        {% for genre in genres %}
            <li>{{ genre.name }}</li>
        {% endfor %}
    </ul>

    <h2>Add Author</h2>
    <a href="/add_author">Add Author</a>

    <h2>Add Book</h2>
    <a href="/add_book">Add Book</a>
</body>
</html>
```

### `templates/author_form.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Author</title>
</head>
<body>
    <h1>Add Author</h1>
    <form action="/add_author" method="POST">
        <label for="name">Author Name:</label><br>
        <input type="text" id="name" name="name"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

### `templates/book_form.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Book</title>
</head>
<body>
    <h1>Add Book</h1>
    <form action="/add_book" method="POST">
        <label for="title">Book Title:</label><br>
        <input type="text" id="title" name="title"><br>
        <label for="author">Author:</label><br>
        <select id="author" name="author">
            {% for author in authors %}
                <option value="{{ author.id }}">{{ author.name }}</option>
            {% endfor %}
        </select><br>
        <label for="genre">Genre:</label><br>
        <select id="genre" name="genre">
            {% for genre in genres %}
                <option value="{{ genre.id }}">{{ genre.name }}</option>
            {% endfor %}
        </select><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```



5. Run the application:
   ```
   python app.py
   ```

This application allows you to manage authors, books, and genres. Authors can have multiple books, and books can belong to multiple genres. The relationships are more complex, allowing for a robust representation of real-world scenarios. You can add authors, books, and genres through the respective forms.

---

### Step 1: Set Up the Flask Application and Database

1. Create a new directory for your project and navigate into it:
   ```bash
   mkdir ecommerce_platform
   cd ecommerce_platform
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate
   ```

3. Install Flask and SQLAlchemy in the virtual environment:
   ```bash
   pip install Flask SQLAlchemy
   ```

4. Create a Python file named `app.py` and open it in your text editor.

5. In `app.py`, import necessary modules and set up the Flask application:
   ```python
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
   db = SQLAlchemy(app)
   ```



### Step 2: Create a Product Model

1. In `app.py`, below the existing code, define a Product model:
   ```python
   class Product(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(100), nullable=False)
       price = db.Column(db.Float, nullable=False)
       description = db.Column(db.Text)

       def __repr__(self):
           return f'<Product {self.name}>'
   ```

   Here, we define a Product model with attributes like `name`, `price`, and `description`.

2. Below the Product model, add the code to create the database tables:
   ```python
   if __name__ == '__main__':
       with app.app_context():
           db.create_all()
       app.run(debug=True)
   ```



### Step 3: Seed the Database with Example Products

1. In `app.py`, below the existing code, add a function to seed the database with example products:
   ```python
   def seed_database():
       products = [
           Product(name='Product 1', price=10.99, description='This is the first product.'),
           Product(name='Product 2', price=19.99, description='This is the second product.'),
           Product(name='Product 3', price=7.99, description='This is the third product.')
       ]

       for product in products:
           db.session.add(product)

       db.session.commit()
   ```

2. Modify the `if __name__ == '__main__':` block to call the `seed_database()` function before running the app:
   ```python
   if __name__ == '__main__':
       with app.app_context():
           db.create_all()
           seed_database()
       app.run(debug=True)
   ```

This function `seed_database()` creates some example products and inserts them into the database.

Now, when you run the application, it will create the Product table and populate it with example products.


1. Ensure you are in the project directory.

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your web browser and visit `http://127.0.0.1:5000/`.

You should see the product catalog displaying the example products we seeded. Each product will have its name, price, and description listed.

