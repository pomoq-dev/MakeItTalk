import os

from PIL import Image
from pydub import AudioSegment

EXAMPLES_DIR = 'examples'

file_names = os.listdir(EXAMPLES_DIR)
for file_name in file_names:
    if file_name.endswith('.mp3'):
        print(file_name)
        just_name = file_name.split('.')[0]
        sound = AudioSegment.from_mp3(os.path.join(EXAMPLES_DIR, file_name))
        sound.export(os.path.join(EXAMPLES_DIR, '{}.wav'.format(just_name)), format="wav")