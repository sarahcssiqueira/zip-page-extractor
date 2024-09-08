# Zip Page Extractor

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release Version](https://img.shields.io/github/release/sarahcssiqueira/zip-page-extractor.svg)](https://github.com/sarahcssiqueira/zip-page-extractor/releases/latest)
[![Support Level](https://img.shields.io/badge/support-may_take_time-yellow.svg)](#support-level)

Python-based tool for web scraping and content archiving, extracting HTML, CSS, and JavaScript files from a given URL. It also compresses the extracted files into a single ZIP archive for easy distribution. 

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

- Clone a .env-example file

Clone in the project root with the following contents:

```
BASE_URL=https://example.com
OUTPUT_DIR=output
ZIP_FILE=archive.zip
```

- Run the Extraction Scripts

    - Extract HTML:

    `python extract-html.py --output-dir <output-directory>`

    - Extract CSS:

    `python extract-css.py --output-dir <output-directory>`

    - Extract Inline CSS:

    `python extract-inline-css.py --output-file <output-file>`

    - Extract JavaScript:

    `python extract-js.py --output-dir <output-directory>`

    - Extract Inline JavaScript:

    `python extract-inline-js.py --output-file <output-file>`

Replace <output-directory> with the desired directory for CSS and JavaScript files and <output-file> with the desired file names for inline CSS and JavaScript.

- Compress the Files:

After extracting the files, run the compression script to create a ZIP archive:

`python compress-files.py --output-dir <output-directory> --zip-file <zip-file-name>`

Replace <output-directory> with the directory where the extracted files are located and <zip-file-name> with the desired name for the ZIP archive.

## Scripts List

- **extract-html.py:** Extracts HTML content from the URL and saves it to a file in the specified directory.
- **extract-css.py:** Extracts linked CSS files from the URL and saves them in the specified directory.
- **extract-inline_css.py:** Extracts inline CSS styles from the HTML content and saves them to a specified file.
- **extract-js.py:** Extracts linked JavaScript files from the URL and saves them in the specified directory.
- **extract-inline_js.py:** Extracts inline JavaScript from the HTML content and saves them to a specified file.
- **compress-files.py:** Compresses all extracted files into a ZIP archive, saving it with the specified name.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.