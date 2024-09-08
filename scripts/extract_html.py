import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def extract_html(url=None, output_dir=None):
    if not url:
        url = os.getenv('BASE_URL')  # Use URL from .env if no URL is provided
    if not output_dir:
        output_dir = os.getenv('OUTPUT_DIR', 'output')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    os.makedirs(output_dir, exist_ok=True)
    html_file = os.path.join(output_dir, 'index.html')

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    print(f"HTML extracted to {html_file}")

# Command-line usage
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Extract HTML from URL')
    parser.add_argument('--url', help='URL to extract HTML from')
    parser.add_argument('--output-dir', help='Directory to save HTML file')
    args = parser.parse_args()

    extract_html(args.url, args.output_dir)
