from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

# Define Department model
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'<Department {self.name}>'

# Define Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    department = db.relationship('Department', backref=db.backref('employees', lazy=True))

    def __repr__(self):
        return f'<Employee {self.name}>'

# Sample data for demonstration
sample_data = [
    {"department": "HR", "employees": ["John Doe", "Jane Smith"]},
    {"department": "IT", "employees": ["Mark Johnson"]}
]

# Create database and insert sample data
with app.app_context():
    db.create_all()
    for data in sample_data:
        department_name = data["department"]
        department = Department.query.filter_by(name=department_name).first()
        if not department:
            department = Department(name=department_name)
            db.session.add(department)
            db.session.commit()

        for employee_name in data["employees"]:
            employee = Employee.query.filter_by(name=employee_name).first()
            if not employee:
                employee = Employee(name=employee_name, department=department)
                db.session.add(employee)
                db.session.commit()

@app.route('/')
def index():
    departments = Department.query.all()
    return render_template('index.html', departments=departments)

if __name__ == '__main__':
    app.run(debug=True)
