import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def extract_js(url=None, output_dir=None):
    if not url:
        url = os.getenv('BASE_URL')  # Fallback to URL from .env if none provided
    if not output_dir:
        output_dir = os.getenv('OUTPUT_DIR', 'output')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    os.makedirs(output_dir, exist_ok=True)

    for script in soup.find_all('script', src=True):
        js_url = urljoin(url, script.get('src'))
        js_response = requests.get(js_url)

        js_filename = os.path.join(output_dir, os.path.basename(js_url))

        with open(js_filename, 'w', encoding='utf-8') as f:
            f.write(js_response.text)

        print(f"JavaScript saved to {js_filename}")

# Command-line usage
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Extract JavaScript from URL')
    parser.add_argument('--url', help='URL to extract JavaScript from')
    parser.add_argument('--output-dir', help='Directory to save JavaScript files')
    args = parser.parse_args()

    extract_js(args.url, args.output_dir)
