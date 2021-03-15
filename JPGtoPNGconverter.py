import sys
import os
from PIL import Image

source_folder_path = sys.argv[1]
output_folder_path = sys.argv[2]

source_folder = os.listdir(source_folder_path)

if not os.path.exists(output_folder_path):
    os.mkdir(output_folder_path)

for pokemon in source_folder:
    source_file_path = source_folder_path + pokemon
    output_file_path = output_folder_path + pokemon[0:-4] + '.png'

    img = Image.open(source_file_path)
    img.save(output_file_path, 'png')


