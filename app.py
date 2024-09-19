from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///currencies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model for storing currency exchange rates
class ExchangeRate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_currency = db.Column(db.String(3), nullable=False)
    to_currency = db.Column(db.String(3), nullable=False)
    rate = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<ExchangeRate {self.from_currency} to {self.to_currency}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = request.form.get('amount')
    from_currency = request.form.get('from-currency')
    to_currency = request.form.get('to-currency')

    if not amount or not from_currency or not to_currency:
        return jsonify({'error': 'Missing data'}), 400

    # Fetch exchange rate from the database
    exchange_rate = ExchangeRate.query.filter_by(from_currency=from_currency, to_currency=to_currency).first()

    if not exchange_rate:
        return jsonify({'error': 'Exchange rate not found'}), 404

    converted_amount = float(amount) * exchange_rate.rate
    return jsonify({'converted_amount': converted_amount})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True, port=5001)
