from flask import Flask, request, jsonify
from utils.db_connect import get_mongo_client
from functools import wraps
import os
from dotenv import load_dotenv
load_dotenv()
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

try:
    db = get_mongo_client()
    print("Database connection established successfully.")
except Exception as e:
    print(f"Error connecting to the database: {e}")

# Decorator to require authentication for certain routes
def require_auth(f):
    @wraps(f) # This decorator preserves the original function's metadata
    def decorated_function(*args, **kwargs):
        if request.headers.get('x-api-key') != os.getenv('MY_API_KEY'):
            print("Unauthorized access attempt detected.")
            return jsonify({"error": "Unauthorized"}), 401
        else:
            return f(*args, **kwargs)
    return decorated_function
        

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/records', methods=['GET'])
def get_records():
    try:
        collection = db['records']
        records = list(collection.find())
        if not records:
            return jsonify({"message": "No records found"}), 404
        # Convert ObjectId to string for JSON serialization
        for record in records:
            record['_id'] = str(record['_id'])
        
        return jsonify(records)
    except Exception as e:
        print(f"Error fetching records: {e}")
        return jsonify({"error": "An error occurred while fetching records"}), 500
    
@app.route('/records', methods=['POST'])
@require_auth
def add_record():
    try:
        collection = db['records']
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        result = collection.insert_one(data)
        return jsonify({"message": "Record added"}), 201
    except Exception as e:
        print(f"Error adding record: {e}")
        return jsonify({"error": "An error occurred while adding the record"}), 500
    
@app.route('/records/<record_id>', methods=['DELETE'])
@require_auth
def delete_record(record_id):
    try:
        collection = db['records']
        result = collection.delete_one({'_id': ObjectId(record_id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Record not found"}), 404
        return jsonify({"message": "Record deleted"}), 200
    except Exception as e:
        print(f"Error deleting record: {e}")
        return jsonify({"error": "An error occurred while deleting the record"}), 500
    
@app.route('/records/<record_id>', methods=['PUT'])
@require_auth
def update_record(record_id):
    try:
        collection = db['records']
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        result = collection.update_one({'_id': ObjectId(record_id)}, {'$set': data})
        if result.matched_count == 0:
            return jsonify({"error": "Record not found"}), 404
        
        return jsonify({"message": "Record updated"}), 200
    except Exception as e:
        print(f"Error updating record: {e}")
        return jsonify({"error": "An error occurred while updating the record"}), 500

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')