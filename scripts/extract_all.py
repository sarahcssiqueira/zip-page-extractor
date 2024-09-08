import os
import argparse

def run_extraction_scripts(url=None, output_dir=None):
    """Run all extraction scripts in sequence with optional URL and output directory."""
    base_command = "python"
    
    # Define the commands to run each script
    commands = [
        f"{base_command} extract_html.py --url {url} --output-dir {output_dir}",
        f"{base_command} extract_css.py --url {url} --output-dir {output_dir}",
        f"{base_command} extract_inline_css.py --url {url} --output-file {output_dir}/inline_styles.css",
        f"{base_command} extract_js.py --url {url} --output-dir {output_dir}",
        f"{base_command} extract_inline_js.py --url {url} --output-file {output_dir}/inline_scripts.js"
    ]

    # Execute each command
    for cmd in commands:
        print(f"Running: {cmd}")
        os.system(cmd)
    print("All scripts completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run all extraction scripts with a single command.")
    parser.add_argument("--url", help="URL to extract resources from", required=True)
    parser.add_argument("--output-dir", help="Directory to save extracted files", required=True)
    
    args = parser.parse_args()
    
    run_extraction_scripts(url=args.url, output_dir=args.output_dir)
