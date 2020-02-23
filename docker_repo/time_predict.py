import numpy as np
from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)
dl_model = tf.keras.models.load_model('dl_model')


@app.route('/')
def home():
    return jsonify({"message": 'Predict the sending email time!'})

@app.route('/predict',methods=['POST'])
def predict():
    data = request.json
    arr = np.array([data['features']]).reshape(1,6)
    print(arr)
    hours = int(round(dl_model.predict(arr)[0][0])//60)
    minutes = int(round(dl_model.predict(arr)[0][0])%60)
    return jsonify({'predicted_time': '{0}:{1}'.format(hours, minutes)})



if __name__ == "__main__":
    app.run(host='0.0.0.0')
