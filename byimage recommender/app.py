import sys
import os
sys.path.append("..")  # Adds higher directory to python modules path.
from img_to_vec import Img2Vec
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity


input_path = './static/resources/img/test_images'

img2vec = Img2Vec()

pics = {}
for file in os.listdir(input_path):
    filename = os.fsdecode(file)
    img = Image.open(os.path.join(input_path, filename))
    vec = img2vec.get_vec(img)
    pics[filename] = vec

def get_similiar_products():
    pic_name = "bluza1.jpg"
    print()
    sims = {}
    for key in list(pics.keys()):
        if key == pic_name:
            continue

        sims[key] = cosine_similarity(pics[pic_name].reshape((1, -1)), pics[key].reshape((1, -1)))[0][0]

        d_view = [(v, k) for k, v in sims.items()]
        d_view.sort(reverse=True)

    similiar_products=d_view[:6]
    return(similiar_products)