import os
from PIL import Image

input_folder = "images"
output_folder = "resized"  
new_size = (800, 800)       
output_format = "JPEG"       

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img_resized = img.resize(new_size)

        base_name, _ = os.path.splitext(filename)
        new_filename = f"{base_name}.{output_format.lower()}"
        save_path = os.path.join(output_folder, new_filename)

        img_resized.save(save_path, output_format)

        print(f"Resized & saved: {save_path}")

print("✅ All images have been resized and saved.")
