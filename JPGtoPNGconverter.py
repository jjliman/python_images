import sys
import os
from PIL import Image


def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)
    return


def save_to_png(source_path, output_path):
    img = Image.open(source_path)
    img.save(output_path, 'png')


source_folder_path = sys.argv[1]
output_folder_path = sys.argv[2]

create_directory(output_folder_path)

source_files = os.listdir(source_folder_path)

for source_file in source_files:
    source_file_path = source_folder_path + source_file
    source_file_clean = os.path.splitext(source_file)[0]
    output_file_path = output_folder_path + source_file_clean + '.png'

    save_to_png(source_file_path, output_file_path)
