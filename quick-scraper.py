import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin

# Function to scrape the website
def scrape_website(url):
    # Get current date
    date_str = datetime.now().strftime("%Y-%m-%d")
    download_folder = os.path.join(os.path.expanduser("~/Downloads"), date_str)
    os.makedirs(download_folder, exist_ok=True)
    
    print(f"Saving content to: {download_folder}")
    
    # Headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    
    # Fetch the webpage
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve {url} (Status Code: {response.status_code})")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all text content
    all_text = "\n".join([element.get_text(strip=True) for element in soup.find_all() if element.name not in ['script', 'style', 'meta', 'link']])
    
    # Save content to a text file
    content_file = os.path.join(download_folder, "content.txt")
    with open(content_file, "w", encoding="utf-8") as file:
        file.write("Extracted Content:\n")
        file.write(all_text)
    
    if all_text.strip():
        print(f"✅ Text content saved ({len(all_text)} characters) in: {content_file}")
    else:
        print("⚠️ No text content extracted!")
    
    # Download images
    img_folder = os.path.join(download_folder, "images")
    os.makedirs(img_folder, exist_ok=True)
    
    img_tags = soup.find_all('img')
    img_count = 0
    for i, img in enumerate(img_tags):
        img_url = urljoin(url, img.get('src'))
        try:
            img_data = requests.get(img_url, headers=headers).content
            img_name = os.path.join(img_folder, f"image_{i+1}.jpg")
            with open(img_name, 'wb') as img_file:
                img_file.write(img_data)
            print(f"🖼️ Downloaded image: {img_name}")
            img_count += 1
        except Exception as e:
            print(f"❌ Failed to download image {img_url}: {e}")
    
    if img_count > 0:
        print(f"✅ Downloaded {img_count} images to: {img_folder}")
    else:
        print("⚠️ No images found to download.")
    
    print(f"🎉 Scraping complete! All content saved in {download_folder}")

# Example usage
if __name__ == "__main__":
    url = input("Enter URL to scrape: ")
    scrape_website(url)