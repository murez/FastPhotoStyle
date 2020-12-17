from FPS_api import FPS
from flask import Flask, request, jsonify, send_file
from PIL import Image
import base64
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')
@app.route('/FPS/', methods = ['POST'], strict_slashes=False)
def return_fps():
    content = request.json
    # print("get json success")
    content_image = base64.b64decode(str(content['content']))
    style_image = base64.b64decode(str(content['style']))
    content_image = Image.open(io.BytesIO(content_image))
    style_image = Image.open(io.BytesIO(style_image))
    # print("decode success")
    result_image = FPS(content_image,style_image)
    # print("get fpsed success")
    im_file = io.BytesIO()
    im = result_image.save(im_file, format="JPEG")
    im_file.seek(0)
    # print('success')
    return send_file(im_file, mimetype="image/jpeg")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=10086)
