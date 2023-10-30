#STI - Single Table Inheritance - comentários podem ser comentários de posts e/ou comentários a comentários

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments_sti.db'
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    commenter_name = db.Column(db.String(100), nullable=False)
    comment_type = db.Column(db.String(20))  # Discriminator column

    __mapper_args__ = {
        'polymorphic_identity': 'comment',
        'polymorphic_on': comment_type
    }

class PostComment(Comment):
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'post_comment'
    }

class ReplyComment(Comment):
    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'reply_comment'
    }

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    comments = db.relationship('PostComment', backref='post', lazy=True)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
