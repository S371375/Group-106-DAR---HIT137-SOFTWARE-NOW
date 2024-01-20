from PIL import Image

# Load the image
image_path = 'extracted_files/chapter1.jpg'
original_image = Image.open(image_path)
width, height = original_image.size

# Generate a number based on the algorithm
import time
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print(generated_number)

# Create a new image with converted pixels
new_image = Image.new('RGB', (width, height))

# Iterate over each pixel in the original image
for y in range(height):
    for x in range(width):
        # Get the original pixel values
        r, g, b = original_image.getpixel((x, y))

        # Modify the pixel values based on the generated number
        r_new = (r + generated_number) % 256
        g_new = (g + generated_number) % 256
        b_new = (b + generated_number) % 256

        # Set the modified pixel values in the new image
        new_image.putpixel((x, y), (r_new, g_new, b_new))

# Save the new image
new_image_path = 'output/chapter1out.png'
new_image.save(new_image_path)

# Calculate the sum of red pixel values in the new image
red_sum = sum([new_image.getpixel((x, y))[0] for y in range(height) for x in range(width)])

# Print the sum for the next chapter
print(f"Sum of red pixel values: {red_sum}")
