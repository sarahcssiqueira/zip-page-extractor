import os
import zipfile
import argparse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
output_dir = os.getenv('OUTPUT_DIR', 'output')
zip_file = os.getenv('ZIP_FILE', 'archive.zip')

# Set up argument parser
parser = argparse.ArgumentParser(description='Compress extracted files into a ZIP archive.')
parser.add_argument('--output-dir', type=str, default=output_dir, help='Directory containing the extracted files')
parser.add_argument('--zip-file', type=str, default=zip_file, help='Name of the output ZIP file')
args = parser.parse_args()

def compress_files(output_dir, zip_file):
    # List of directories and files to include in the zip
    directories = ['css', 'js']
    files = ['page.html', 'inline_styles.css', 'inline_scripts.js']
    
    # Create a zip file
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        # Add directories and their contents
        for folder in directories:
            folder_path = os.path.join(output_dir, folder)
            for root, dirs, filenames in os.walk(folder_path):
                for filename in filenames:
                    filepath = os.path.join(root, filename)
                    # Add file to the zip file
                    zipf.write(filepath, os.path.relpath(filepath, output_dir))
        
        # Add individual files
        for file in files:
            file_path = os.path.join(output_dir, file)
            if os.path.exists(file_path):
                zipf.write(file_path)
    
    print(f"Created ZIP archive: {zip_file}")

# Call the function to compress the files
compress_files(args.output_dir, args.zip_file)
