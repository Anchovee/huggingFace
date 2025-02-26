

__all__= ['is_cat', 'learn', 'classify_image', 'categories', 'image', 'label', 'examples', 'intf']

#Dependencies
import gradio as gr
from fastai.vision.all import *

def is_cat(x): return x[0].isupper()

#Get .pkl
learn = load_learner('model.pkl')

#Set labels and create a function to classify images based on learner
categories = ('Dog', 'Cat')

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

#De
image = gr.components.Image()
label = gr.components.Label()
examples = ['dog.jpg', 'cat.jpg', 'dunno.jpg']

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)