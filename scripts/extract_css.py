import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def extract_css(url=None, output_dir=None):
    if not url:
        url = os.getenv('BASE_URL')  # Fallback to URL from .env if none provided
    if not output_dir:
        output_dir = os.getenv('OUTPUT_DIR', 'output')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    os.makedirs(output_dir, exist_ok=True)

    for link in soup.find_all('link', rel='stylesheet'):
        css_url = urljoin(url, link.get('href'))
        css_response = requests.get(css_url)

        css_filename = os.path.join(output_dir, os.path.basename(css_url))

        with open(css_filename, 'w', encoding='utf-8') as f:
            f.write(css_response.text)

        print(f"CSS saved to {css_filename}")

# Command-line usage
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Extract CSS from URL')
    parser.add_argument('--url', help='URL to extract CSS from')
    parser.add_argument('--output-dir', help='Directory to save CSS files')
    args = parser.parse_args()

    extract_css(args.url, args.output_dir)
