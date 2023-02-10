import math
import PIL
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import datetime

def create_profile_picture(percentage_filled, image_path):
    # Open the image to insert
    inner_image = Image.open(image_path)
    
    # Resize the inner image to fit inside the circle with a 5px margin
    size = min(inner_image.width, inner_image.height)
    size = math.floor(size * 2.4)
    inner_image = inner_image.resize((size, size), Image.ANTIALIAS)
    
    # Create a mask to crop the inner image to a circular shape
    mask = Image.new('L', inner_image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((57, 57, size-57, size-57), fill=255)
    
    # Apply the mask to the inner image to make it round
    inner_image = inner_image.copy()
    inner_image.putalpha(mask)
    
    # Create a blank image with a white background
    image = Image.new('RGB', (500, 500), (0,0,0))
    draw = ImageDraw.Draw(image)
    
    # Draw the circle outline
    draw.ellipse((0, 0, 500, 500), outline='black')
    
    # Calculate the angle to fill based on the percentage filled
    fill_angle = 360 * percentage_filled
    
    # Fill the circle with the specified percentage
    draw.pieslice((0, 0, 500, 500), 90, 90 + fill_angle, fill='rgba(4,85,254,255)')
    
    # Convert the image to RGBA format
    image = image.convert("RGBA")
    
    # Crop the image to the smallest bounding box that contains the filled circle
    image = image.crop(image.getbbox())

    # Calculate the position of the inner image
    x = (500 - size) / 2
    y = (500 - size) / 2
    
    # Insert the inner image
    image.paste(inner_image, (int(x), int(y)), inner_image)
    
    return image

# Calculate the number of days left in the year
today = datetime.datetime.now()
end_of_year = datetime.datetime(today.year, 12, 31)
days_left = (end_of_year - today).days
percentage_filled = 1 - (days_left / 365)

# Create and save the profile picture
image = create_profile_picture(percentage_filled, 'bobba.jpg')
image.save('profile_picture2.png')