from flask import Flask, after_this_request, render_template, request, send_file
import os
import shutil
import tempfile
from scripts.extract_html import extract_html
from scripts.extract_css import extract_css
from compress_files import compress_files, default_archive_name
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        work_dir = tempfile.mkdtemp(prefix="zip-page-extractor-", dir=tempfile.gettempdir())
        output_dir = os.path.join(work_dir, "output")

        @after_this_request
        def cleanup(response):
            shutil.rmtree(work_dir, ignore_errors=True)
            return response

        # Run extraction using the URL from the form for all scripts
        extract_html(url, output_dir)
        extract_css(url, output_dir)  # Ensure the form URL is passed to each script
        # Add other script calls here

        # Compress the output files
        zip_name = os.path.basename(os.getenv("ZIP_FILE") or default_archive_name(url))
        zip_file = os.path.join(work_dir, zip_name)
        compress_files(output_dir, zip_file)

        # Serve the ZIP file
        return send_file(zip_file, as_attachment=True, download_name=zip_name)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
