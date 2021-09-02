import psycopg2
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class mailinglist(db.Model):
    __tablename__ = 'mailinglist'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200), unique=True)
    source = db.Column(db.String(200))

    def __init__(self, customer, email, source):
        self.customer = customer
        self.email = email
        self.source = source

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/health")
def health():
    return render_template('code200.html')

@app.route("/ready")
def test():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='db' port='5432' password='postgres' connect_timeout=1")
        conn.close()
        return render_template('code200.html')
    except:
        return render_template('code503.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        email = request.form['email']
        source = request.form['source']
        if customer == '' or email == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(mailinglist).filter(mailinglist.customer == customer).count() == 0:
            data = mailinglist(customer, email, source)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')
        return render_template('index.html', message='You have already signed up to our newsletter.')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 