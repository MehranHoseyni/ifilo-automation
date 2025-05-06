import os

IFILO_USER = os.getenv("IFILO_USER")
IFILO_PASS = os.getenv("IFILO_PASS")
DOWNLOAD_DIR = "downloads"

def upload_to_ifilo(video_path):
    print(f"Uploading {video_path} to ifilo as {IFILO_USER}...")
    # عملیات واقعی آپلود اینجا شبیه‌سازی شده است
    return True

if __name__ == "__main__":
    for filename in os.listdir(DOWNLOAD_DIR):
        if filename.endswith(".mp4"):
            full_path = os.path.join(DOWNLOAD_DIR, filename)
            upload_to_ifilo(full_path)
