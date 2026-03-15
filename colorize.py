import sys
try:
    from PIL import Image
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

def colorize_image_gold(input_path, output_path):
    # Open the image and convert to RGBA
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    # Target gold color: #b68a52 -> RGB (182, 138, 82)
    new_data = []
    for item in datas:
        # Check alpha channel. If it's not transparent, colorize it.
        # It's an anti-aliased image, so we keep the original alpha value,
        # but change the RGB values.
        if item[3] > 0:
            new_data.append((182, 138, 82, item[3]))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")
    print("Successfully created scales_gold.png")

if __name__ == "__main__":
    colorize_image_gold("img/scales.png", "img/scales_gold.png")
