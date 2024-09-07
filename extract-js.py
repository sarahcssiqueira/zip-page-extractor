from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import argparse

# Load environment variables from .env file
load_dotenv()

# Access environment variables
base_url = os.getenv('BASE_URL')
output_dir = os.getenv('OUTPUT_DIR', 'js')

# Set up argument parser
parser = argparse.ArgumentParser(description='Extract JavaScript files from a URL.')
parser.add_argument('--output-dir', type=str, default=output_dir, help='Directory to save the extracted JavaScript files')
args = parser.parse_args()

# Ensure the output directory exists
if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

def fetch_js_files(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all linked JavaScript files
    for script in soup.find_all('script', src=True):
        js_url = script.get('src')
        if js_url.startswith('//'):
            js_url = 'https:' + js_url
        elif not js_url.startswith('http'):
            js_url = requests.compat.urljoin(url, js_url)
        
        js_response = requests.get(js_url)
        
        # Save the JavaScript to a file
        js_filename = os.path.join(args.output_dir, os.path.basename(js_url))
        with open(js_filename, 'w', encoding='utf-8') as js_file:
            js_file.write(js_response.text)
        
        print(f"Saved JS from {js_url} to {js_filename}")

fetch_js_files(base_url)
