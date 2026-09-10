import argparse
import hashlib
import os
import re
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


def _asset_urls(page_url, soup):
    urls = set()
    attributes = {
        "img": ("src", "srcset"),
        "source": ("src", "srcset"),
        "video": ("src", "poster"),
        "audio": ("src",),
        "object": ("data",),
    }

    for tag_name, attribute_names in attributes.items():
        for tag in soup.find_all(tag_name):
            for attribute_name in attribute_names:
                value = tag.get(attribute_name)
                if not value:
                    continue
                if attribute_name == "srcset":
                    values = (candidate.strip().split()[0] for candidate in value.split(","))
                else:
                    values = (value,)
                urls.update(urljoin(page_url, candidate) for candidate in values if candidate)

    for link in soup.find_all("link", href=True):
        rel_values = {value.lower() for value in link.get("rel", [])}
        if rel_values & {"icon", "apple-touch-icon", "mask-icon", "preload"}:
            urls.add(urljoin(page_url, link["href"]))

    css_urls = [
        urljoin(page_url, link["href"])
        for link in soup.find_all("link", href=True)
        if "stylesheet" in {value.lower() for value in link.get("rel", [])}
    ]
    css_texts = [style.string or "" for style in soup.find_all("style")]
    for css_url in css_urls:
        css_response = requests.get(css_url)
        css_response.raise_for_status()
        css_texts.append(css_response.text)
    for css_text in css_texts:
        for value in re.findall(r"url\(\s*['\"]?([^'\")]+)", css_text):
            urls.add(urljoin(page_url, value.strip()))

    return {
        url
        for url in urls
        if urlparse(url).scheme in {"http", "https"}
    }


def _asset_filename(asset_url, used_names):
    parsed_url = urlparse(asset_url)
    filename = Path(unquote(parsed_url.path)).name or "asset"
    if filename in used_names:
        digest = hashlib.sha1(asset_url.encode("utf-8")).hexdigest()[:8]
        filename = f"{Path(filename).stem}-{digest}{Path(filename).suffix}"
    used_names.add(filename)
    return filename


def extract_assets(url=None, output_dir=None):
    url = url or os.getenv("BASE_URL")
    output_dir = output_dir or os.getenv("OUTPUT_DIR", "tmp/output")
    asset_dir = Path(output_dir) / "assets"
    asset_dir.mkdir(parents=True, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    used_names = set()

    for asset_url in sorted(_asset_urls(url, soup)):
        asset_response = requests.get(asset_url)
        asset_response.raise_for_status()
        asset_path = asset_dir / _asset_filename(asset_url, used_names)
        asset_path.write_bytes(asset_response.content)
        print(f"Asset saved to {asset_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract linked page assets")
    parser.add_argument("--url", help="URL to extract assets from")
    parser.add_argument("--output-dir", help="Directory to save extracted assets")
    args = parser.parse_args()

    extract_assets(args.url, args.output_dir)
