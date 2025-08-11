import os
import requests

# Create 'images' folder
os.makedirs("images", exist_ok=True)

# List of sample image URLs
image_urls = [
    "https://picsum.photos/1200/800",
    "https://picsum.photos/800/1200",
    "https://picsum.photos/1000/1000",
    "https://picsum.photos/1920/1080"
]

# Download each image
for idx, url in enumerate(image_urls, start=1):
    response = requests.get(url)
    if response.status_code == 200:
        file_path = f"images/sample_{idx}.jpg"
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Downloaded {file_path}")
    else:
        print(f"❌ Failed to download image {idx}")

print("All sample images downloaded successfully!")
