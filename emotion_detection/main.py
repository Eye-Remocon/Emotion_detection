import base64
import cv2
import io

import numpy
import aws_emotion_detection
import home_emotion_detection
from PIL import Image
from flask import Flask, request, jsonify



app = Flask(__name__)
            
@app.route('/main', methods=['POST'])
def main():
    payload = request.form.to_dict(flat=False)
    im_b64 = payload['image'][0]
    im_binary = base64.b64decode(im_b64)
    buf = io.BytesIO(im_binary)
    face_img = Image.open(buf).convert('RGB')
    open_cv_face_image = numpy.array(face_img)



    detection_result = home_emotion_detection.detection(open_cv_face_image)
    if detection_result == '':
        detection_result = aws_emotion_detection.aws_main(im_binary)

    return jsonify({"emotion":detection_result})



if __name__ == "__main__":
    app.run(debug=True, host='192.168.0.4', port=8080)


