# Recommendation System for e-commerce - based on image

The web-based application recommends similar products based on the similarity of product images.

## Technologies
App is based on **Python 3.6**
It uses the following technologies:
- Python 3.6
	- Flask
	- img_to_vec
	- sklearn
	- PIL
	- PyTorch 1.1
- HTML
- CSS
- JavaScript
- Bootstrap 4

`IMG_TO_VEC - github` : <https://github.com/christiansafka/img2vec>

## How to use
In order to get this app up&running you need to open Windows command line and write following :
```
pip install --upgrade pip
pip install flask
pip install sklearn
pip3 install https://download.pytorch.org/whl/cu90/torch-1.1.0-cp36-cp36m-win_amd64.whl
pip3 install https://download.pytorch.org/whl/cu90/torchvision-0.3.0-cp36-cp36m-win_amd64.whl

```
After that move in command line to : *Recommendation-System/byimage recommender/ * and open up app.

`python flaskapp.py`

## Example of usage
**Homepage view**
![alt text](https://github.com/BartoszWlazlo/Recommendation-System/blob/master/readme/1.png)

**Product view**
![alt text](https://github.com/BartoszWlazlo/Recommendation-System/blob/master/readme/2.png)

**Recommendation for X product**
![alt text](https://github.com/BartoszWlazlo/Recommendation-System/blob/master/readme/3.png)
