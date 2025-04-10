# TikTok Downloader

A simple Python script to download TikTok videos using gallery-dl.

## Features

- Download TikTok videos from regular or shortened URLs
- Automatically organize downloads in a dedicated folder
- Set best quality for downloads
- Clean and simple command-line interface
- Works with both regular and shortened TikTok links

## Requirements

- Python 3.6+
- [gallery-dl](https://github.com/mikf/gallery-dl) (must be installed and accessible in your PATH)

## Installation

1. Make sure you have Python installed on your system
2. Install gallery-dl:

   ```bash
   pip install gallery-dl
   ```

3. Clone this repository or download the script:

   ```bash
   git clone https://github.com/yourusername/tiktok-downloader.git
   cd tiktok-downloader
   ```

## Usage

### Basic Usage

```bash
python download_tiktok.py <tiktok_url>
```

Example:

```bash
python download_tiktok.py https://vt.tiktok.com/ZSr5PSHtk/
```

### Output

Downloaded videos will be saved to a `tiktok_downloads` folder in the same directory as the script. The files will be named according to the pattern: `{category}_{title}_{id}`.

## How It Works

1. The script parses the provided TikTok URL
2. It creates a download directory if it doesn't exist
3. It uses `gallery-dl` to download the video with optimal settings
4. Videos are saved in high quality with a consistent naming scheme

## Customization

You can modify the script to:

- Change the download directory by editing the `download_dir` variable
- Adjust the file naming format
- Enable comments or likes download (disabled by default)

## Troubleshooting

If you encounter issues:

1. Make sure gallery-dl is properly installed and accessible in your PATH
2. Verify you have the correct URL format
3. Check the error messages for specific issues
4. For "SSL: CERTIFICATE_VERIFY_FAILED" errors, you may need to update your Python's SSL certificates

## License

[MIT License](LICENSE)

## Acknowledgments

- [gallery-dl](https://github.com/mikf/gallery-dl) - The excellent downloader that powers this script

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
