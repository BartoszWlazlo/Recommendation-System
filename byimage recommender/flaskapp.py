from flask import Flask, render_template
import sys
import os

sys.path.append("..")  # Adds higher directory to python modules path.
input_path = './static/resources/img/test_images'
all_paths = []

def GET_ALL():
    for file in os.listdir(input_path):
        filename = os.fsdecode(file)
        all_paths.append(filename)
    return all_paths

datapaths=GET_ALL()

app = Flask(__name__, template_folder="templates")
@app.route('/')
def home():
    """Landing page."""
    return render_template('/index.html', title="Lame Site", allpaths=datapaths)




"""from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
"""
if __name__== "__main__":
    app.run()