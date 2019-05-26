import sys
import os
sys.path.append("..")  # Adds higher directory to python modules path.
from PIL import Image

input_path = './static/resources/img/test_images'

all_paths = []
for file in os.listdir(input_path):
    filename = os.fsdecode(file)
    all_paths.append(filename)


print(filename)