import sys
from PIL import Image # pip install Pillow

def convert_bmp_to_32bit(input_file, output_file):
    # Open the BMP file
    with Image.open(input_file) as img:
        # Convert the image to RGBA (32-bit)
        img = img.convert("RGBA")
        
        # Get the raw data of the image
        raw_data = img.tobytes()
        
        # Write the raw data to the output file
        with open(output_file, 'wb') as f:
            f.write(raw_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_bmp.py <input_file.bmp> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_bmp_to_32bit(input_file, output_file)
    print(f"Converted {input_file} to {output_file} in 32-bit color format without header.")