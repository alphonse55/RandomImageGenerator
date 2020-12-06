from PIL import Image
import random

width = 1000

pixels = []
for i in range(width ** 2):
    pixels.append(
        (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),  # RGBA
        )
    )
new_image = Image.new("RGBA", (width, width))
new_image.putdata(pixels)
new_image.save("image.png")