import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin, urlparse

# Function to scrape a website with deep crawling
def scrape_website(url, max_depth=2, max_pages=150, download_images=True, visited=None):
    if visited is None:
        visited = set()
    
    # Get current date
    date_str = datetime.now().strftime("%Y-%m-%d")
    download_folder = os.path.join(os.path.expanduser("~/Downloads"), date_str)
    os.makedirs(download_folder, exist_ok=True)
    
    print(f"Saving content to: {download_folder}")
    
    # Headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    }
    
    # Stop if page limit is reached
    if len(visited) >= max_pages or max_depth < 0 or url in visited:
        return
    visited.add(url)
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve {url} (Status Code: {response.status_code})")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all text content
    all_text = "\n".join([element.get_text(strip=True) for element in soup.find_all() if element.name not in ['script', 'style', 'meta', 'link']])
    
    # Save content to a text file
    url_slug = urlparse(url).path.replace("/", "_").strip("_") or "index"
    content_file = os.path.join(download_folder, f"{url_slug}.txt")
    with open(content_file, "w", encoding="utf-8") as file:
        file.write(f"Extracted Content from {url}:\n")
        file.write(all_text)
    
    print(f"✅ Text content saved ({len(all_text)} characters) in: {content_file}")
    
    if download_images:
        # Download images
        img_folder = os.path.join(download_folder, "images")
        os.makedirs(img_folder, exist_ok=True)
        
        img_tags = soup.find_all('img')
        img_count = 0
        for i, img in enumerate(img_tags):
            img_url = urljoin(url, img.get('src'))
            try:
                img_data = requests.get(img_url, headers=headers).content
                img_name = os.path.join(img_folder, f"{url_slug}_image_{i+1}.jpg")
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_data)
                print(f"🖼️ Downloaded image: {img_name}")
                img_count += 1
            except Exception as e:
                print(f"❌ Failed to download image {img_url}: {e}")
        
        print(f"✅ Downloaded {img_count} images from {url}")
    
    # Extract and crawl links
    links = [urljoin(url, a.get('href')) for a in soup.find_all('a', href=True)]
    links = list(set([link for link in links if urlparse(link).netloc == urlparse(url).netloc]))
    
    print(f"🔗 Found {len(links)} internal links on {url}")
    
    # Save links
    links_file = os.path.join(download_folder, "links.txt")
    with open(links_file, "a", encoding="utf-8") as file:
        file.write(f"Links from {url}:\n")
        file.write("\n".join(links) + "\n")
    
    # Recursively crawl found links
    for link in links:
        scrape_website(link, max_depth - 1, max_pages, download_images, visited)
    
    # Generate summary report
    report_file = os.path.join(download_folder, "report.txt")
    with open(report_file, "w", encoding="utf-8") as file:
        file.write("Scraping Report:\n")
        file.write(f"Total pages crawled: {len(visited)}\n")
        file.write(f"Total images downloaded: {img_count if download_images else 0}\n")
        file.write(f"Total links extracted: {len(links)}\n")
    
    print(f"📄 Report saved in: {report_file}")
    
    print(f"🎉 Scraping complete! All content saved in {download_folder}")

# Example usage
if __name__ == "__main__":
    url = input("Enter URL to scrape: ")
    download_images = input("Download images? (yes/no): ").strip().lower() == 'yes'
    scrape_website(url, max_depth=2, max_pages=150, download_images=download_images)