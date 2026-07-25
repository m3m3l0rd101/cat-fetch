from ascii_magic import AsciiArt
import shutil
import random

with open("all_img.txt", "+r") as f:
    image_paths = [line.strip() for line in f if line.strip()]

chosen_image = random.choice(image_paths)

terminal_width = shutil.get_terminal_size().columns - 2
output = AsciiArt.from_image(chosen_image)

output.to_terminal(
    columns=terminal_width,
    char=' .:oO0@',
    monochrome=False
)


