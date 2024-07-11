from PIL import Image
import os

def crop_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(input_dir, filename)
            with Image.open(image_path) as img:
                width, height = img.size
                left = width - 222 - 8
                top = height - 45 - 4
                right = width - 8
                bottom = height - 4
                cropped_img = img.crop((left, top, right, bottom))
                
                output_path = os.path.join(output_dir, filename)
                cropped_img.save(output_path)

input_directory = 'D:/Data/img/vv/训练/Train'
output_directory = 'D:/Data/img/vv/训练/Output'

crop_images(input_directory, output_directory)
