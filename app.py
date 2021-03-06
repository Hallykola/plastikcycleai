
import datetime
import os
from flask import Flask,request
import json
from predict import download_model_weights, get_predictions

app = Flask(__name__)


@app.route('/')
def form():
    html = '''
        <!DOCTYPE html>
    <html>
    <header>
    <title>
    Get Parameters</title>
    </header>
    <body>
    <form action="predict" method="post" enctype="multipart/form-data">
        <label>Enter image url:</label>
        <input type="file" name="bottleimage"  accept="image/*">
        <input type="submit" name="submit" value="Send">
    </form>
    </body>
    </html>
    '''
    return html

@app.route('/try')
def tryme():
    result  = get_predictions('rubbish text as raw_image')
    #print(result)
    #stringresult =  ''.join(str(e) for e in result)
    #return '[{}]'.format(stringresult)
    return json.dumps(result)

@app.route('/predict', methods = ['POST'])
def hello_world():
    uploaded_file = request.files['bottleimage']
    if uploaded_file.filename != '':
        UPLOAD_FOLDER = os.path.join(os.getcwd(), "images")
        newfilename = os.path.join(UPLOAD_FOLDER,'{}-{}'.format(int(datetime.datetime.now().timestamp()),uploaded_file.filename))
        uploaded_file.save(newfilename)
        result  = get_predictions(newfilename)
        #print(result)
        #stringresult =  ''.join(str(e) for e in result)
        return json.dumps(result)


if __name__ == '__main__':
    app.run()
