# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Love1981@localhost/jobportal'
# Disable the modification tracking feature of SQLAlchemy (which you don't need)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the UserSearchData model to map to your table
class UserSearchData(db.Model):
    __tablename__ = 'user_search_data'
    
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45))
    browser = db.Column(db.String(100))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    search_role = db.Column(db.String(100))
    search_location = db.Column(db.String(100))
    search_time = db.Column(db.DateTime)

# Define the route to display the data
@app.route('/')
def index():
    # Query all records from the user_search_data table
    records = UserSearchData.query.all()
    # Render the table template with the queried data
    return render_template('table.html', records=records)

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5002, debug=True)