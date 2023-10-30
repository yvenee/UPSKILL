from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:z3rt6@localhost:1111/mystoredb'

db = SQLAlchemy(app)

# Models
class Country(db.Model):
    __tablename__='countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cities = db.relationship('City', backref='country', lazy=True)
    
class City(db.Model):
    __tablename__='cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    
#Create all tables
with app.app_context():
    db.create_all()
    
#Sample Data 
country = Country(name='United States')
city1=City(name='New York', country=country)
city2=City(name='Los Angeles', country=country)

@app.route('/')
def index():
    return render_template('index.html', country=country)

if __name__=='__main__':
    app.run(debug=True)