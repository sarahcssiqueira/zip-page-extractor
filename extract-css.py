from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import argparse

# Load environment variables from .env file
load_dotenv()

# Access environment variables
base_url = os.getenv('BASE_URL')
output_dir = os.getenv('OUTPUT_DIR', 'css')

# Set up argument parser
parser = argparse.ArgumentParser(description='Extract CSS files from a URL.')
parser.add_argument('--output-dir', type=str, default=output_dir, help='Directory to save the extracted CSS files')
args = parser.parse_args()

# Ensure the output directory exists
if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

def fetch_css_files(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all linked CSS files
    for link in soup.find_all('link', rel='stylesheet'):
        css_url = link.get('href')
        if css_url.startswith('//'):
            css_url = 'https:' + css_url
        elif not css_url.startswith('http'):
            css_url = requests.compat.urljoin(url, css_url)
        
        css_response = requests.get(css_url)
        
        # Save the CSS to a file
        css_filename = os.path.join(args.output_dir, os.path.basename(css_url))
        with open(css_filename, 'w', encoding='utf-8') as css_file:
            css_file.write(css_response.text)
        
        print(f"Saved CSS from {css_url} to {css_filename}")

fetch_css_files(base_url)
