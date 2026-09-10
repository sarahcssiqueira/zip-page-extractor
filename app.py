from io import BytesIO

from flask import Flask, after_this_request, render_template, request, send_file
import os
import shutil
import tempfile
import requests
from scripts.extract_html import extract_html
from scripts.extract_css import extract_css
from scripts.extract_assets import extract_assets
from compress_files import compress_files, default_archive_name
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        work_dir = tempfile.mkdtemp(prefix="pagefetcher-", dir=tempfile.gettempdir())
        output_dir = os.path.join(work_dir, "output")

        @after_this_request
        def cleanup(response):
            shutil.rmtree(work_dir, ignore_errors=True)
            return response

        try:
            # Run extraction using the URL from the form for all scripts.
            extract_html(url, output_dir)
            extract_css(url, output_dir)
            extract_assets(url, output_dir)
        except requests.RequestException:
            shutil.rmtree(work_dir, ignore_errors=True)
            return "Unable to fetch that page. Please check the URL and try again.", 502

        # Compress the output files
        zip_name = os.path.basename(os.getenv("ZIP_FILE") or default_archive_name(url))
        zip_file = os.path.join(work_dir, zip_name)
        compress_files(output_dir, zip_file)

        # Read the archive before the response cleanup removes the work directory.
        with open(zip_file, "rb") as archive:
            archive_data = BytesIO(archive.read())

        return send_file(
            archive_data,
            as_attachment=True,
            download_name=zip_name,
            mimetype="application/zip",
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
