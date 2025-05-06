import os
import requests

IFILO_USER = os.getenv("IFILO_USER")
IFILO_PASS = os.getenv("IFILO_PASS")
UPLOAD_URL = "https://ifilo.net/api/upload"
DOWNLOAD_DIR = "downloads"

def authenticate():
    # فرض بر این است که iFilo از Basic Auth استفاده می‌کند
    return (IFILO_USER, IFILO_PASS)

def upload_video(file_path):
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(UPLOAD_URL, files=files, auth=authenticate())
        response.raise_for_status()
        print(f"Uploaded: {os.path.basename(file_path)}")

def main():
    print("Starting upload process...")
    if not os.path.exists(DOWNLOAD_DIR):
        print("Download directory does not exist.")
        return
    for filename in os.listdir(DOWNLOAD_DIR):
        if filename.endswith(".mp4"):
            file_path = os.path.join(DOWNLOAD_DIR, filename)
            upload_video(file_path)

if __name__ == "__main__":
    main()
