from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user inputs from the form
        gender = 0 if request.form['gender'] == 'male' else 1
        age = float(request.form['age'])
        urea = float(request.form['urea'])
        cr = float(request.form['cr'])
        hba1c = float(request.form['hba1c'])
        chol = float(request.form['chol'])
        tg = float(request.form['tg'])
        hdl = float(request.form['hdl'])
        ldl = float(request.form['ldl'])
        vldl = float(request.form['vldl'])
        bmi = float(request.form['bmi'])

        # Convert gender to numerical values
        # gender = 0 if gender == 'male' else 1

        # Make a prediction using the model
        input_data = np.array([[gender, age, urea, cr, hba1c, chol, tg, hdl, ldl, vldl, bmi]])
        prediction = model.predict(input_data)

        # Get the index of the class with the highest probability
        predicted_class = np.argmax(prediction)
        # Map the prediction to the corresponding result
        if predicted_class == 0:
            result = 'No'
        elif predicted_class == 1:
            result = 'Possibility'
        else:
            result = 'Yes'

        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
