from pymongo import MongoClient

# Replace with your MongoDB connection string
MONGO_URI = 'mongodb://localhost:27017/'
DB_NAME = 'your_database_name'
COLLECTION_NAME = 'your_collection_name'

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Example data to insert
data = [
    {"name": "John Doe", "age": 30},
    {"name": "Jane Smith", "age": 25}
]

collection.insert_many(data)
print("Data inserted successfully!")
