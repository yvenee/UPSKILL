#CTI- Clas Table Inheritance
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments_cti.db'
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    commenter_name = db.Column(db.String(100), nullable=False)

class PostComment(Comment):
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', backref='comments', lazy=True)

class ReplyComment(Comment):
    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    parent_comment = db.relationship('Comment', backref='replies', remote_side=[Comment.id])

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)


'''
5

When specifying a relationship between two tables, one of the tables has a foreign key. 
This foreign key "marks" one or more columns as being "connected" to columns in another table.

When specifying relationships in SQLAlchemy, we're using the term "remote" when talking about 
the columns "on the other side" of the foreign-key columns. Or, whichever columns the "foreign" columns are "linked to".

For example, consider a "Customer" table with a "Order" table:

+---------------+         +------------------+
|  Customer     |         | Order            |
+---------------+         +------------------+
|  customer-id  | ------- | customer_id [FK] |
|  name         |         | order_id         |
+---------------+         +------------------+
Assume the order table has a relationship with the customer table via the customer_id column.

In that case, the foreign key will be located on the Order table, and it will "point to" the 
Customer.customer_id column.

As we established earlier, the "remote side" in SQLAlchemy is the "other side" of the foreign key.

So in this particular example, the "remote side" is the Customer.customer_id column.

When working with self-referential tables the concept is the same. 
You have some columns defined as foreign keys "pointing to" other columns (but in the same table this time).
But the concept of "foreign" and "remote" remains the same for SA. 
You just have to adapt it as necessary for the self-referential relationship.
'''