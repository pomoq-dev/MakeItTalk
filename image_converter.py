import os

from PIL import Image


def convert_images(directory):
    file_names = os.listdir(directory)
    for file_name in file_names:
        if file_name.endswith('.jpeg') or file_name.endswith('.png') or file_name.endswith('.jpg'):
            print(file_name)
            just_name = '.'.join(file_name.split('.')[:-1])
            img = Image.open(os.path.join(directory, file_name))
            rgb_img = img.convert('RGB')
            rgb_img = rgb_img.resize((256, 256))
            rgb_img.save(os.path.join(directory, '{}.jpg'.format(just_name)))
            os.remove(os.path.join(directory, file_name))
