from flask import *
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras.preprocessing import image as image_utils
from PIL import Image
import requests
from io import BytesIO

app=Flask(__name__)

app.config['UPLOAD_FOLDER']="/home/Desktop/VIT/'Aarush Hackathon'/SeeFood"
img_width, img_height = 128, 128
model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
model = load_model(model_path)
model._make_predict_function()
model.load_weights(model_weights_path)

@app.route('/')
def upload():
    return render_template("front.html")

@app.route('/take', methods=['GET', 'POST'])
def take():
    if(request.method=='POST'):
        if request.files:
            print("Thank you for choosing a image!")
            f = request.files['photo']
            f.save(f.filename)
            print (f.filename)

            test_image = Image.open(open(f.filename,'rb'))
            print ("Hello")
            test_image = test_image.resize((128,128))  
            test_image = image_utils.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)

            result = model.predict_on_batch(test_image)
            print (result)

            if result[0][0] == 1:
                ans = 'Biriyani'
            elif result[0][1] == 1:
                ans = 'Butter Naan'
            elif result[0][2] == 1:
                ans = 'Dosa'
            elif result[0][3] == 1:
                ans = 'Idly'
            elif result[0][4] == 1:
                ans = 'Medhu Vada'
            
            return '<h1>'+ans+'</h1>'

        else:
            return 'No File Uploaded'

if __name__=="__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)