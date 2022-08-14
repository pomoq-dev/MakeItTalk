import os

from PIL import Image

EXAMPLES_DIR = 'examples'

file_names = os.listdir(EXAMPLES_DIR)
for file_name in file_names:
    if file_name.endswith('.jpeg') or file_name.endswith('.png'):
        print(file_name)
        just_name = file_name.split('.')[0]
        img = Image.open(os.path.join(EXAMPLES_DIR, file_name))
        rgb_img = img.convert('RGB')
        rgb_img.save(os.path.join(EXAMPLES_DIR, '{}.jpg'.format(just_name)))
        os.remove(os.path.join(EXAMPLES_DIR, file_name))
