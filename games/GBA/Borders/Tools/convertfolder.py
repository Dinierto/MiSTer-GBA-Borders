import os
from PIL import Image  # pip install Pillow

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

def convert_all_bmps_in_folder(folder_path):
    # Iterate over all files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.bmp'):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.bor")
            convert_bmp_to_32bit(input_file, output_file)
            print(f"Converted {input_file} to {output_file} in 32-bit color format.")

if __name__ == "__main__":
    folder_path = "."
    convert_all_bmps_in_folder(folder_path)