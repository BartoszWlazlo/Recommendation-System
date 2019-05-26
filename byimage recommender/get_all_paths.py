import sys
import os
sys.path.append("..")  # Adds higher directory to python modules path.
input_path = './static/resources/img/test_images'
all_paths = []
def GET_ALL():
    for file in os.listdir(input_path):
        filename = os.fsdecode(file)
        all_paths.append("./static/resources/img/test_images/"+filename)
    return all_paths
aa=GET_ALL()
print(aa)