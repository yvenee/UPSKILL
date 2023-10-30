from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.db'  

db = SQLAlchemy(app)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    cities = db.relationship('City', backref='country', lazy=True) #

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)

@app.route('/add_country/<country_name>', methods=['GET'])

def add_country(country_name):
    country = Country(name=country_name)
    db.session.add(country)
    db.session.commit()
    return f"Country {country_name} added!"
 
@app.route('/add_city/<country_name>/<city_name>', methods=['GET'])
def add_city(country_name, city_name):
    country = Country.query.filter_by(name=country_name).first()
    if country:
        city = City(name=city_name, country=country)
        db.session.add(city)
        db.session.commit()
        return f"City {city_name} added to {country_name}!"
    return f"Country {country_name} not found!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)