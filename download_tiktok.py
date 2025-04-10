import gallery_dl
import os
import sys
import subprocess
from urllib.parse import urlparse

def download_tiktok(url):
    # Parse the URL to get the video ID
    parsed_url = urlparse(url)
    if parsed_url.netloc == "vt.tiktok.com":
        # For shortened URLs, just use as is - gallery-dl can handle them
        pass
    
    # Create a directory for downloads if it doesn't exist
    download_dir = "tiktok_downloads"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    # Let's use subprocess to call gallery-dl directly
    # This is more reliable than trying to use the API
    try:
        print(f"Downloading TikTok video from {url}...")
        
        # Build the command
        cmd = [
            "gallery-dl",
            url,
            "-d", download_dir,
            "-o", "extractor.tiktok.format=best",
            "-o", "extractor.tiktok.comments=false",
            "-o", "extractor.tiktok.likes=false",
            "-o", f"output.directory={download_dir}",
            "-o", "output.format={category}_{title}_{id}"
        ]
        
        # Run the command
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        # Print output
        if result.stdout:
            print(result.stdout)
            
        print(f"Download completed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error downloading content: {e}")
        if e.stdout:
            print("Output:", e.stdout)
        if e.stderr:
            print("Error:", e.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download_tiktok.py <tiktok_url>")
        sys.exit(1)
    
    url = sys.argv[1]
    download_tiktok(url)
