from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('heart_disease.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/predict', methods=['POST','GET'])
def index():
    data1 = request.form['age']
    data2 = request.form['sex']
    data3 = request.form['chestPain']
    data4 = request.form['restingBPS']
    data5 = request.form['cholesterol']
    data6 = request.form['fastingBloodSugar']
    data7 = request.form['restingECG']
    data8 = request.form['maxHeartRate']
    data9 = request.form['exerciseAngina']
    data10= request.form['oldPeak']
    data11= request.form['STSlope']
    arr = np.array([[float(data1), float(data2), float(data3),float(data4),float(data5),float(data6),float(data7),float(data8),float(data9),float(data10),float(data11)]])
    
    print("Input Array:", arr)
    pred = model.predict(arr)
    print("Model Prediction:", pred)
   
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)
  