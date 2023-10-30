from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///self.db'
db = SQLAlchemy(app)

# Define the many-to-many relationship for self-referential relationship
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    followers = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('following', lazy='dynamic'), lazy='dynamic')

# Create the database
with app.app_context():
    db.create_all()

# Sample data to test the relationship
user1 = User(username='user1')
user2 = User(username='user2')
user3 = User(username='user3')
user1.following.append(user2)
user1.following.append(user3)
user3.following.append(user1)
user2.following.append(user3)

@app.route('/')
def index():
    
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()
    return render_template('index.html', users=[user1, user2, user3])

if __name__ == '__main__':
    app.run(debug=True)
