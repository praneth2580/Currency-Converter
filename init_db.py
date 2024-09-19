import requests
from app import app, db, ExchangeRate

#All currencies
currencies = ["USD","EUR","GBP","JPY","AUD","CAD","CHF","CNY","SEK","NZD","MXN","SGD","HKD","NOK","KRW","TRY","RUB","INR","BRL","ZAR"];

# Replace with your actual API URL and key
API_URL = 'https://api.exchangerate-api.com/v4/latest/'

def fetch_rates():
    try:
        print("FETCHING RATES")
        for currency in currencies:
            print(f"Fetching Currency {currency} Progress [{int((currencies.index(currency) / len(currencies)) * 100)}%]", end='\r', flush=True)
            response = requests.get(API_URL + currency)
            response.raise_for_status()
            data = response.json()
            if data['rates']:
                update_db_with_rates(data['rates'], currency)
            else:
                print(f"Failed to fetch rates [{currency}]. Database not updated.")

    except requests.RequestException as e:
        print(f"Error fetching rates: {e}")
        return None

def clean_db():
    with app.app_context():
        # Clear existing rates (optional)
        db.session.query(ExchangeRate).delete()
        db.session.commit()
        print('---------------------')
        print('DB CLEARED')
        print('---------------------')

def update_db_with_rates(rates, from_currency):
    with app.app_context():
        db.create_all()  # Ensure the table is created

        # Add or update rates
        for to_currency, rate in rates.items():
            # if to_currency == 'USD':
            #     continue  # Skip USD to avoid redundant entries
            existing_rate = ExchangeRate.query.filter_by(from_currency=from_currency, to_currency=to_currency).first()
            if existing_rate:
                existing_rate.rate = rate
            else:
                new_rate = ExchangeRate(from_currency=from_currency, to_currency=to_currency, rate=rate)
                db.session.add(new_rate)

        db.session.commit()

if __name__ == '__main__':
    clean_db()
    fetch_rates()
    print("Database updated with current rates.")
