from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Define the many-to-many relationship for students and courses
enrollments = db.Table('enrollments',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    courses = db.relationship('Course', secondary=enrollments, backref=db.backref('students', lazy='dynamic'), lazy='dynamic')

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Sample data to test the relationship
student1 = Student(name='John Doe')
student2 = Student(name='Alice Smith')
course1 = Course(name='Python Programming')
course2 = Course(name='Data Science 101')
student1.courses.append(course1)
student1.courses.append(course2)
student2.courses.append(course1)

@app.route('/')
def index():
     # Add the objects to the session
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(course1)
    db.session.add(course2)
    
    # Commit the session to save the changes to the database
    db.session.commit()
    return render_template('index.html', students=[student1, student2], courses=[course1, course2])

if __name__ == '__main__':
    app.run(debug=True)
