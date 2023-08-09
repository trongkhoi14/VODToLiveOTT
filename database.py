from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['livestreamdb']

user = db["User"]

user.insert_one({
    'UserFullName': '',
    'UserPhone': '',
    'UserEmail': '',
    'UserAddress': '',
    'UserRole': ''
})

channel = db["Channel"]

channel.insert_one({
    'ChannelName': '',
    'ChannelDesc': '',
    'ChannelStatus': ''
})

mrssfeed = db["MRSSFeed"]

mrssfeed.insert_one({
    'FeedUrl': '',
    'Author': '',
    'Title': '',
    'Link': '',
    'Published': '',
    'Updated': ''
})

video = db["Video"]

video.insert_one({
    'VideoID': '',
    'VideoTitle': '',
    'VideoUrl': '',
    'PublishedDate': '',
    'VideoDesc': '',
    'CategoryId': '',
    'MRSSFeedId': ''
})

comment = db["Comment"]

comment.insert_one({
    'CmtCreated': '',
    'CmtText': ''
})

like = db["Like"]

like.insert_one({
    'UserID': '',
    'VideoID': ''
})

dislike = db["Dislike"]

dislike.insert_one({
    'UserID': '',
    'VideoID': ''
})

schedule = db["Schedule"]

schedule.insert_one({
    'ScheduleStartTime': '',
    'ScheduleEndTime': ''
})

category = db["Category"]

category.insert_one({
    'CategoryName': ''
})