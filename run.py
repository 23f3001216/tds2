# run.py
import requests
from pathlib import Path

# Your deployed API endpoint
API_URL = "https://tds2-glf7.onrender.com/api"

files = {}
# Attach questions.txt
if Path("questions.txt").exists():
    files["questions.txt"] = open("questions.txt", "rb")
else:
    print("Error: questions.txt not found")
    exit(1)

# Attach image.png if it exists
if Path("image.png").exists():
    files["image.png"] = open("image.png", "rb")

try:
    response = requests.post(API_URL, files=files, timeout=300)  # 5-minute timeout
    print(response.text)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
