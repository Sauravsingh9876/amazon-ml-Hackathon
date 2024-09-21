import requests
import os

def download_images(image_url, save_path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {save_path}")
        else:
            print(f"Failed to download: {image_url}")
    except Exception as e:
        print(f"Error downloading {image_url}: {str(e)}")
