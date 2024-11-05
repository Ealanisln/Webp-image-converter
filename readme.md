# Image to WebP Converter

A Python script to convert various image formats (PNG, JPG, JPEG) to WebP format with customizable quality settings.

## Requirements

- Python 3
- Pillow library

## Installation

1. Make sure you have Python 3 installed:
```bash
python3 --version
```

2. If Python is not installed, install it:
### For macOS (using Homebrew):
```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python3
```

3. Install the required Pillow library:
```bash
pip3 install Pillow
```

## Usage

The script provides several options for converting images:

### Basic Usage
```bash
python3 convert_images.py
```
This will use default settings:
- Quality: 80%
- Formats: PNG, JPG, JPEG
- Default path: /Users/ealanis/Development/utils/image-converter/Images-to-be-converted

### Custom Options

1. Specify a different path:
```bash
python3 convert_images.py --path /path/to/your/images
# or
python3 convert_images.py -p /path/to/your/images
```

2. Set custom quality (0-100):
```bash
python3 convert_images.py --quality 90
# or
python3 convert_images.py -q 90
```

3. Select specific formats to convert:
```bash
python3 convert_images.py --formats png jpg
# or
python3 convert_images.py -f png jpg
```

4. Combine multiple options:
```bash
python3 convert_images.py -p /custom/path -q 95 -f png jpg jpeg
```

## Directory Structure

The script expects one of the following:

1. A folder named `images-to-convert` in the same directory as the script, or
2. A custom path specified via the `--path` argument

### Setting up the directory:

```bash
# Option 1: Create default directory
mkdir images-to-convert
# Place your images in this directory

# Option 2: Use a custom directory
python3 convert_images.py --path /path/to/your/images
```

If the default directory doesn't exist, the script will offer to create it for you.

## Output

- Converted images are saved in a new `webp_converted` folder within the input directory
- The script maintains original filenames but changes the extension to `.webp`
- Progress is displayed during conversion, showing:
  - Number of files being converted
  - Individual file conversion status
  - File size comparison
  - Overall conversion success rate

## Features

- Supports multiple input formats (PNG, JPEG, JPG)
- Adjustable output quality (0-100)
- Shows file size comparison for each conversion
- Reports conversion success rate
- Command-line arguments for easy customization
- Error handling for each file

## Options Reference

| Option | Short | Description | Default |
|--------|--------|-------------|---------|
| --path | -p | Input directory path | /Users/ealanis/Development/utils/image-converter/Images-to-be-converted |
| --quality | -q | WebP quality (0-100) | 80 |
| --formats | -f | Image formats to convert | png jpg jpeg |

## Example Output
```
Image to WebP Converter
======================
Input path: /path/to/images
Selected formats: png, jpg, jpeg
Quality setting: 80
======================
Found 5 images to convert...
Converted (1/5): image1.png -> image1.webp
  Original: 150.5KB, Converted: 45.2KB
  Size reduction: 70.0%
[...]
```

## Error Handling

The script will:
- Skip files that can't be converted
- Continue processing if one file fails
- Report any errors encountered during conversion
- Show final success/failure count

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.