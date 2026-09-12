import os
import zipfile
import argparse
from datetime import date
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def default_archive_name(url=None):
    url = url or os.getenv("BASE_URL")
    hostname = urlparse(url).hostname if url else None
    site_name = (hostname or "siteurl").removeprefix("www.")
    return f"pagefetcher-{site_name}-{date.today():%Y%m%d}.zip"

def compress_files(output_dir, zip_file):
    os.makedirs(os.path.dirname(zip_file) or ".", exist_ok=True)

    with zipfile.ZipFile(zip_file, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        for root, _, filenames in os.walk(output_dir):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                arcname = os.path.relpath(file_path, output_dir)
                zipf.write(file_path, arcname)

    print(f"Created ZIP archive: {zip_file}")


if __name__ == "__main__":
    output_dir = os.getenv("OUTPUT_DIR", "tmp/output")
    zip_file = os.getenv("ZIP_FILE") or os.path.join("tmp", default_archive_name())

    parser = argparse.ArgumentParser(description="Compress extracted files into a ZIP archive.")
    parser.add_argument("--output-dir", type=str, default=output_dir, help="Directory containing the extracted files")
    parser.add_argument("--zip-file", type=str, default=zip_file, help="Name of the output ZIP file")
    args = parser.parse_args()

    compress_files(args.output_dir, args.zip_file)
