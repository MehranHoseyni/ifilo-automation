import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

IFILO_USER = os.getenv("IFILO_USER")
IFILO_PASS = os.getenv("IFILO_PASS")
DOWNLOAD_DIR = "downloads"

options = Options()
options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

def login(driver):
    driver.get("https://ifilo.net/login")
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys(IFILO_USER)
    driver.find_element(By.NAME, "password").send_keys(IFILO_PASS)
    driver.find_element(By.XPATH, "//button[contains(text(),'ورود')]").click()
    time.sleep(4)

def upload_all():
    driver = webdriver.Chrome(options=options)
    try:
        login(driver)
        for fname in os.listdir(DOWNLOAD_DIR):
            if fname.endswith('.mp4'):
                path = os.path.join(DOWNLOAD_DIR, fname)
                driver.get("https://ifilo.net/upload")
                time.sleep(2)
                driver.find_element(By.NAME, "title").send_keys(fname)
                driver.find_element(By.NAME, "file").send_keys(path)
                driver.find_element(By.XPATH, "//button[contains(text(),'آپلود')]").click()
                time.sleep(5)
                print(f"Uploaded: {fname}")
    finally:
        driver.quit()