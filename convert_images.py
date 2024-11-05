from PIL import Image
import os
import argparse

def convert_images(input_dir, output_dir=None, quality=80, formats=None):
    """
    Convert images to WebP format.
    
    Args:
        input_dir (str): Input directory path
        output_dir (str): Output directory path (optional)
        quality (int): Output image quality (0-100)
        formats (list): List of input formats to convert (e.g., ['PNG', 'JPEG', 'JPG'])
    """
    # Default formats if none specified
    if formats is None:
        formats = ['PNG', 'JPEG', 'JPG']
    
    # Normalize formats to lowercase
    formats = [fmt.lower() for fmt in formats]
    
    # Create output directory if not specified
    if output_dir is None:
        output_dir = os.path.join(input_dir, 'webp_converted')
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get all eligible files
    image_files = [
        f for f in os.listdir(input_dir) 
        if any(f.lower().endswith(f'.{fmt}') for fmt in formats)
    ]
    total_files = len(image_files)
    
    if total_files == 0:
        print(f"No images with formats {formats} found in the directory!")
        return
    
    print(f"Found {total_files} images to convert...")
    print(f"Quality setting: {quality}")
    
    # Process all image files in the input directory
    success_count = 0
    for index, filename in enumerate(image_files, 1):
        try:
            # Open image
            input_path = os.path.join(input_dir, filename)
            image = Image.open(input_path)
            
            # Create output filename
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_dir, output_filename)
            
            # Convert and save as WebP
            image.save(output_path, 'WEBP', quality=quality)
            
            # Get file sizes for comparison
            original_size = os.path.getsize(input_path) / 1024  # KB
            converted_size = os.path.getsize(output_path) / 1024  # KB
            size_reduction = ((original_size - converted_size) / original_size) * 100
            
            print(f'Converted ({index}/{total_files}): {filename} -> {output_filename}')
            print(f'  Original: {original_size:.1f}KB, Converted: {converted_size:.1f}KB')
            print(f'  Size reduction: {size_reduction:.1f}%')
            
            success_count += 1
            
        except Exception as e:
            print(f'Error converting {filename}: {str(e)}')
    
    print(f"\nConversion complete! Successfully converted {success_count} of {total_files} files.")
    print(f"Check the 'webp_converted' folder in: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert images to WebP format')
    parser.add_argument('--path', '-p', 
                       default="/Users/ealanis/Development/utils/image-converter/Images-to-be-converted",
                       help='Path to the directory containing images')
    parser.add_argument('--quality', '-q', type=int, default=80,
                       help='WebP quality (0-100, default: 80)')
    parser.add_argument('--formats', '-f', nargs='+', 
                       default=['png', 'jpg', 'jpeg'],
                       help='Image formats to convert (default: png jpg jpeg)')

    args = parser.parse_args()

    print("Image to WebP Converter")
    print("======================")
    print(f"Input path: {args.path}")
    print(f"Selected formats: {', '.join(args.formats)}")
    print(f"Quality setting: {args.quality}")
    print("======================")

    if os.path.exists(args.path):
        convert_images(args.path, quality=args.quality, formats=args.formats)
    else:
        print("Error: Directory not found! Please make sure the path exists.")