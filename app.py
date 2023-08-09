from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb+srv://14042002a:luongkhoi123@cluster0.xro9zib.mongodb.net/')
db = client['livestreamdb']
users_collection = db['User']
video_collection = db['Video']


# Define API routes
@app.route('/admin_users', methods=['GET'])
def admin_users():
    data = list(users_collection.find({'UserRole': 'admin'}, {'_id': 1, 'UserFullName': 1, 'UserPhone': 1, 'UserEmail': 1, 'UserAddress': 1, 'UserRole': 1}))
    
    # Convert ObjectId to string for JSON serialization
    for item in data:
        if '_id' in item:
            item['_id'] = str(item['_id'])
    
    return jsonify(data)

@app.route('/total_videos', methods=['GET'])
def total_videos():
    data = video_collection.count_documents({})
    return jsonify(data)

if __name__ == '__main__':
    app.run()
