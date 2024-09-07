from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import argparse

# Load environment variables from .env file
load_dotenv()

# Access environment variables
base_url = os.getenv('BASE_URL')
output_file = os.getenv('OUTPUT_FILE', 'inline_scripts.js')

# Set up argument parser
parser = argparse.ArgumentParser(description='Extract inline JavaScript from a URL.')
parser.add_argument('--output-file', type=str, default=output_file, help='File to save the extracted inline JavaScript')
args = parser.parse_args()

def fetch_inline_js(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract inline scripts
    scripts = []
    for script in soup.find_all('script'):
        if not script.get('src'):
            scripts.append(script.string)
    
    # Save inline scripts to a file
    with open(args.output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(scripts))
    
    print(f"Saved inline scripts to {args.output_file}")

fetch_inline_js(base_url)
