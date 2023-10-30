from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
db = SQLAlchemy(app)

# Define the Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    commenter_name = db.Column(db.String(100), nullable=False)
    commentable_id = db.Column(db.Integer)
    commentable_type = db.Column(db.String(20))

    def __repr__(self):
        return f'<Comment {self.content}>'

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    def __repr__(self):
        return f'<Post {self.title}>'

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
