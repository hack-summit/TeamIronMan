from flask import *

app=Flask(__name__)
app.config['UPLOAD_FOLDER']="/home/akash/Desktop/img"

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def pic_save():
    if request.method=='POST':
        if request.files:            
            f=request.files['photo']
            print (f.filename)
            f.save(f.filename)
            return 'File Saved!'
        else:
            return 'No file'

    else:
        return 'Method not possible'

if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)