from PIL import Image


def create_knitting_pattern_from_image(image_path, scale, black_pixel_spacing, output_path):
    # Open the original image
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size

    # Calculate the size of the new image including the black pixel spacing
    new_width = (original_width * scale) + ((original_width - 1) * black_pixel_spacing)
    new_height = (original_height * scale) + ((original_height - 1) * black_pixel_spacing)

    # Create a new image with the scaled size filled initially with black
    new_image = Image.new("RGB", (new_width, new_height), (0, 0, 0))  # (0, 0, 0) is black

    # Loop through each pixel of the original image
    for x in range(original_width):
        for y in range(original_height):
            # Get the color of the pixel at (x, y)
            pixel_color = original_image.getpixel((x, y))

            # Calculate the position in the new image, considering black pixel spacing
            new_x = x * (scale + black_pixel_spacing)
            new_y = y * (scale + black_pixel_spacing)

            # Draw a scale_factor x scale_factor block of the same color in the new image
            for i in range(scale):
                for j in range(scale):
                    new_image.putpixel((new_x + i, new_y + j), pixel_color)

    # Save the enlarged image with black pixels added
    new_image.save(output_path)
    print(f"Image saved to {output_path}")
