from pymongo import MongoClient

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://14042002a:luongkhoi123@cluster0.xro9zib.mongodb.net/')
db = client['livestreamdb']
users_collection = db['User']
video_collection = db['Video']

# Sample data for collection "User"
sample_users = []
for i in range(1000):
    user = {
        'UserFullName': f'User {i}',
        'UserPhone': f'123456789{i}',
        'UserEmail': f'user{i}@example.com',
        'UserAddress': f'Address {i}',
        'UserRole': 'user'
    }
    sample_users.append(user)

# Sample data for collection "Video"
sample_videos = []
for i in range(1000):
    video = {
        'VideoTitle': f'Video {i}',
        'VideoUrl': f'https://www.youtube.com/watch?v=abc{i}',
        'PublishedDate': '2023-08-09',
        'VideoDesc': f'Description for Video {i}',
        'CategoryId': '123',
        'MRSSFeedId': '456'
    }
    sample_videos.append(video)

# Add data to collection "User" và "Video"
users_collection.insert_many(sample_users)
video_collection.insert_many(sample_videos)

print("Sample data inserted successfully.")