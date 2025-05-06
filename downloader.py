import os
import requests

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
MAX_VIDEOS = int(os.getenv("MAX_VIDEOS", 1))
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def fetch_trending_videos():
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=IR&maxResults={MAX_VIDEOS}&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    items = response.json().get("items", [])
    return [(item["id"], item["snippet"]["title"]) for item in items]

def download_video(video_id, title):
    filename = os.path.join(DOWNLOAD_DIR, f"{title}.mp4")
    # فقط لینک ساختگی برای تست، چون در اکشن واقعی امکان دانلود از یوتیوب نیست
    with open(filename, "w") as f:
        f.write(f"FAKE_VIDEO_DATA_FOR_{video_id}")

if __name__ == "__main__":
    for vid, title in fetch_trending_videos():
        safe_title = "".join(c for c in title if c.isalnum() or c in " _-")
        download_video(vid, safe_title)
