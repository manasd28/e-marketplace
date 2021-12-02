import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict-laptop',methods=['GET', 'POST'])
def predict_laptop():
    '''
    For rendering results on HTML GUI
    '''
    model = pickle.load(open('mobile-model.pkl', 'rb'))
    int_features = [x for x in request.form.values()][:3]
    final_features = np.expand_dims(np.array(int_features), axis = 0)
    print(final_features.shape)
    prediction = model.predict(final_features)

    output = round(prediction[0], 0)

    return render_template('index.html', prediction_text='Laptop Price Should be ₹ {}'.format(output))

if __name__ == "__main__":
    app.run(port=8002,debug=True)
