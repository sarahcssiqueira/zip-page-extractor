from dotenv import load_dotenv
import os
import requests
import argparse

# Load environment variables from .env file
load_dotenv()

# Access environment variables
base_url = os.getenv('BASE_URL')
output_dir = os.getenv('OUTPUT_DIR', 'output')

# Set up argument parser
parser = argparse.ArgumentParser(description='Extract HTML from a URL.')
parser.add_argument('--output-dir', type=str, default=output_dir, help='Directory to save the extracted HTML file')
args = parser.parse_args()

# Ensure the output directory exists
if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

# Fetch and save HTML
response = requests.get(base_url)
output_path = os.path.join(args.output_dir, 'page.html')
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(response.text)

print(f"Saved HTML to {output_path}")
