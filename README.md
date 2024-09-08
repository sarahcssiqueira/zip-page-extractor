# Zip Page Extractor

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release Version](https://img.shields.io/github/release/sarahcssiqueira/zip-page-extractor.svg)](https://github.com/sarahcssiqueira/zip-page-extractor/releases/latest)
[![Support Level](https://img.shields.io/badge/support-may_take_time-yellow.svg)](#support-level)

A Python-based tool for web scraping and content archiving, extracting HTML, CSS, and JavaScript files from a given URL. It also compresses the extracted files into a single ZIP archive for easy distribution. 

## Features

- Extracts HTML, CSS, and JavaScript from a web page.
- Compresses extracted files into a ZIP archive.
- Supports both local command-line execution and web-based extraction via a form.

## Installation

- Clone the Repository:

`git clone https://github.com/sarahcssiqueira/zip-page-extractor`

`cd zip-page-extractor`

- Create a Virtual Environment (optional but recommended):

`python -m venv venv`

`source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

- Install Required Packages:

Install the necessary Python packages using pip:

`pip install -r requirements.txt`

## Usage

### Command-Line Usage

To run the extraction scripts individually:

`python scripts/extract_html.py --url "https://example.com" --output-dir output`

Extract CSS:

`python scripts/extract_css.py --url "https://example.com" --output-dir output`

Replace "https://example.com" with your target URL and output with your desired directory.

Compress the files:

After extracting, compress them into a ZIP archive:

`python compress_files.py --output-dir output --zip-file archive.zip`

- Running All Scripts with a Single Command

To run all extraction scripts (HTML, CSS, JavaScript) in a single command, use the provided run_all.py script. This will automatically run all the extraction processes and store the output in the specified directory.

`python run_all.py --url <your-url> --output-dir <output-directory>`

This command will extract the HTML, CSS, and JavaScript files from https://example.com and store them in the output directory.

### Web-Based Usage

Run the Flask web server:

`python app.py`

Access the web form:

Visit http://127.0.0.1:5000/ in your browser. Submit the URL to extract HTML, CSS, and JS files, and download the ZIP archive.

Note: When using the web form, the provided URL will be used by all extraction scripts (HTML, CSS, JS). The URL in the .env file is only used when running the scripts locally without a provided URL.

## Scripts Overview

- **extract_html.py:** Extracts HTML content from the URL and saves it to a file in the specified directory.
- **extract_css.py:** Extracts linked CSS files from the URL and saves them in the specified directory.
- **extract_inline_css.py:** Extracts inline CSS styles from the HTML content and saves them to a specified file.
- **extract_js.py:** Extracts linked JavaScript files from the URL and saves them in the specified directory.
- **extract_inline_js.py:** Extracts inline JavaScript from the HTML content and saves them to a specified file.
- **compress_files.py:** Compresses all extracted files into a ZIP archive, saving it with the specified name.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.