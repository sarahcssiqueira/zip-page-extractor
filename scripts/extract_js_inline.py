import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def extract_inline_js(url=None, output_file=None):
    if not url:
        url = os.getenv('BASE_URL')  # Fallback to URL from .env if none provided
    if not output_file:
        output_file = os.getenv('OUTPUT_DIR', 'inline_scripts.js')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    inline_scripts = [script.string for script in soup.find_all('script') if script.string]

    with open(output_file, 'w', encoding='utf-8') as f:
        for script in inline_scripts:
            f.write(script + '\n')

    print(f"Inline JavaScript saved to {output_file}")

# Command-line usage
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Extract inline JavaScript from URL')
    parser.add_argument('--url', help='URL to extract inline JavaScript from')
    parser.add_argument('--output-file', help='File to save inline JavaScript')
    args = parser.parse_args()

    extract_inline_js(args.url, args.output_file)
