from pathlib import Path

from PIL import Image


def enlarge_image(image_path: Path, scale: int, output_path: Path):
    # Open the original image
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size

    # Calculate the size of the new image
    new_width = original_width * scale
    new_height = original_height * scale

    # Create a new image with the scaled size
    new_image = Image.new("RGB", (new_width, new_height))

    # Loop through each pixel of the original image
    for x in range(original_width):
        for y in range(original_height):
            # Get the color of the pixel at (x, y)
            pixel_color = original_image.getpixel((x, y))

            # Draw a scale_factor x scale_factor block of the same color in the new image
            for i in range(scale):
                for j in range(scale):
                    new_image.putpixel((x * scale + i, y * scale + j), pixel_color)

    # Save the enlarged image
    new_image.save(output_path)
    print(f"Image saved to {output_path}")


# Parameters
input_image_path = Path("monster.png")  # Path to the original image
output_image_path = Path("monster_large.png")  # Path to save the enlarged image
scale_factor = 30  # Factor by which to enlarge the pixels

# Enlarge the image
enlarge_image(image_path=input_image_path, scale=scale_factor, output_path=output_image_path)
