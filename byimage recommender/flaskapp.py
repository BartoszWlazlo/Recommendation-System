from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    """Landing page."""
    return render_template('/index.html', title="Lame Site")

"""from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
"""
if __name__== "__main__":
    app.run()