import os
from googleapiclient.discovery import build
import yt_dlp

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
TREND_REGION = "IR"
MAX_RESULTS = int(os.getenv("MAX_VIDEOS", 5))
DOWNLOAD_DIR = "downloads"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_trends():
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    response = youtube.videos().list(
        part="snippet,contentDetails",
        chart="mostPopular",
        regionCode=TREEND_REGION,
        maxResults=MAX_RESULTS
    ).execute()
    videos = [(item["id"], item["snippet"]["title"]) for item in response.get("items", [])]
    for vid, title in videos:
        out_path = os.path.join(DOWNLOAD_DIR, f"{vid}.mp4")
        if not os.path.exists(out_path):
            yt_dlp.YoutubeDL({'outtmpl': out_path,'format': 'bestvideo+bestaudio'}).download([f"https://www.youtube.com/watch?v={vid}"])
        print(f"Downloaded: {title}")