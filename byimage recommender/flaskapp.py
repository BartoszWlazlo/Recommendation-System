from flask import Flask, render_template
import sys
import os
sys.path.append("..")  # Adds higher directory to python modules path.
from img_to_vec import Img2Vec
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
import re

sys.path.append("..")  # Adds higher directory to python modules path.
input_path = './static/resources/img/test_images'
all_paths = []

#lista dostepnych produktow
def GET_ALL():
    for file in os.listdir(input_path):
        filename = os.fsdecode(file)
        filename = os.path.splitext(filename)[0]
        all_paths.append(filename)
    return all_paths

datapaths=GET_ALL()
#HOMEPAGE
app = Flask(__name__, template_folder="templates")
@app.route('/')
def home():
    """Landing page."""
    return render_template('/index.html', title="SvA Inc.", allpaths=datapaths)


img2vec = Img2Vec()

pics = {}
for file in os.listdir(input_path):
    filename = os.fsdecode(file)
    img = Image.open(os.path.join(input_path, filename))
    vec = img2vec.get_vec(img)
    pics[filename] = vec

def get_similiar_products(product_name):
    pic_name = str(product_name)
    print()
    sims = {}
    for key in list(pics.keys()):
        if key == pic_name:
            continue

        sims[key] = cosine_similarity(pics[pic_name].reshape((1, -1)), pics[key].reshape((1, -1)))[0][0]

        d_view = [(v, k) for k, v in sims.items()]
        d_view.sort(reverse=True)

    similiar_products=d_view[:8]
    return(similiar_products)

@app.route('/product/<some_product>')
def some_place_page(some_product):
    recommended_products_list=get_similiar_products(some_product)
    product=os.path.splitext(some_product)[0]
    return render_template('/product.html',productname_extension=some_product,recommended_products=recommended_products_list, productname=product)


if __name__== "__main__":
    app.run()