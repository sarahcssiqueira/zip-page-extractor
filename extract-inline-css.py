from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import argparse

# Load environment variables from .env file
load_dotenv()

# Access environment variables
base_url = os.getenv('BASE_URL')
output_file = os.getenv('OUTPUT_FILE', 'inline_styles.css')

# Set up argument parser
parser = argparse.ArgumentParser(description='Extract inline CSS from a URL.')
parser.add_argument('--output-file', type=str, default=output_file, help='File to save the extracted inline CSS')
args = parser.parse_args()

def fetch_inline_css(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract inline styles
    styles = []
    for tag in soup.find_all(style=True):
        styles.append(tag.get('style'))
    
    # Save inline styles to a file
    with open(args.output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(styles))
    
    print(f"Saved inline styles to {args.output_file}")

fetch_inline_css(base_url)

