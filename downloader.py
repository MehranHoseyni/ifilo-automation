import os
import requests
from pytube import YouTube

API_KEY = os.getenv("YOUTUBE_API_KEY")
MAX_VIDEOS = int(os.getenv("MAX_VIDEOS", 3))
SEARCH_QUERY = "motivational speech"
DOWNLOAD_DIR = "downloads"

def search_videos(query, max_results):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q={query}&maxResults={max_results}&key={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("items", [])

def download_video(video_id, title):
    yt_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(yt_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    stream.download(output_path=DOWNLOAD_DIR, filename=f"{title}.mp4")
    print(f"Downloaded: {title}")

def main():
    print("Starting download process...")
    videos = search_videos(SEARCH_QUERY, MAX_VIDEOS)
    for video in videos:
        video_id = video["id"]["videoId"]
        title = video["snippet"]["title"].replace("/", "_").replace("\\", "_")
        download_video(video_id, title)

if __name__ == "__main__":
    main()
