from flask import Flask, render_template, request, send_file
import os
from scripts.extract_html import extract_html
from scripts.extract_css import extract_css
from compress_files import compress_files
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        output_dir = os.getenv('OUTPUT_DIR', 'output')

        # Run extraction using the URL from the form for all scripts
        extract_html(url, output_dir)
        extract_css(url, output_dir)  # Ensure the form URL is passed to each script
        # Add other script calls here

        # Compress the output files
        zip_file = os.getenv('ZIP_FILE', 'archive.zip')
        compress_files(output_dir, zip_file)

        # Serve the ZIP file
        return send_file(zip_file, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
