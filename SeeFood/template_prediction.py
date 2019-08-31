import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras.preprocessing import image as image_utils
from PIL import Image
import requests
from io import BytesIO

img_width, img_height = 128, 128
model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

test_image = Image.open(BytesIO())
put_image = test_image.resize((400,400)) 
test_image = test_image.resize((128,128))  
test_image = image_utils.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)


result = model.predict_on_batch(test_image)
print (result)

if result[0][1] == 1:
    ans = 'Butter Naan'
elif result[0][0] == 1:
    ans = 'Medhu Vadai'
'''elif result[0][2] == 1:
    ans = 'samosa' '''

out = Label(window, text  = 'Predicted answer : ' +  ans, font=("Helvetica", 16))
out.pack()
