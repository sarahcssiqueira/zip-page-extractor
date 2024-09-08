import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def extract_inline_css(url=None, output_file=None):
    if not url:
        url = os.getenv('BASE_URL')  # Fallback to URL from .env if none provided
    if not output_file:
        output_file = os.getenv('OUTPUT_DIR', 'inline_styles.css')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    inline_styles = [tag.get('style') for tag in soup.find_all(style=True) if tag.get('style')]

    with open(output_file, 'w', encoding='utf-8') as f:
        for style in inline_styles:
            f.write(style + '\n')

    print(f"Inline CSS saved to {output_file}")

# Command-line usage
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Extract inline CSS from URL')
    parser.add_argument('--url', help='URL to extract inline CSS from')
    parser.add_argument('--output-file', help='File to save inline CSS styles')
    args = parser.parse_args()

    extract_inline_css(args.url, args.output_file)
