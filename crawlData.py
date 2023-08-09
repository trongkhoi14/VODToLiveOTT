# Thư viện feedparser ấy và phân tích thông tin từ các nguồn cấp dữ liệu định dạng RSS 
import feedparser
from pymongo import MongoClient

# Đường dẫn đến MRSS feeds
url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UC2fu6CiFfNYz5UFORvFyc0w'

# Sử dụng feedparser để lấy dữ liệu từ MRSS feeds
feed = feedparser.parse(url)

# Kết nối tới MongoDB  
client = MongoClient('mongodb://localhost:27017/')

db = client['livestreamdb']

video_collection = db['Video']

feed_data = {
    'FeedUrl': url,
    'Author': feed.get('author', ''),
    'Title': feed.get('title', ''),
    'Link': feed.get('link', ''),
    'Published': feed.get('published', ''),
    'Updated': feed.get('updated', '')
}

mrss_feeds_collection = db['MRSSFeed']
mrss_feed_id = mrss_feeds_collection.insert_one(feed_data).inserted_id

# Lặp qua các mục trong feeds và trích xuất thông tin cần thiết
for entry in feed.entries:
    video_id = entry.get('yt_videoid')
    video_title = entry.get('title')
    video_url = entry.get('link')
    published_date = entry.get('published')
    video_desc = entry.get('description')
    category = ''

    # ... thêm các bước làm sạch dữ liệu nếu cần ...

    # Tạo một dictionary lưu thông tin video
    video_data = {
        'VideoID': video_id,
        'VideoTitle': video_title,
        'VideoUrl': video_url,
        'PublishedDate': published_date,
        'VideoDesc': video_desc,
        'CategoryId': category,
        'MRSSFeedId': mrss_feed_id

        # ... thêm các thông tin khác nếu cần ...
    }

    # Lưu dữ liệu vào MongoDB
    video_collection.insert_one(video_data)

# Đóng kết nối tới MongoDB
client.close()
