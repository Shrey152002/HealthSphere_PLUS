# app.py
from flask import Flask, render_template, request
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
app = Flask(__name__)

def get_llama_response(age, gender, weight, disease, diet_preference):
    llm = CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})

    template = """
        Generate a customized 200-250 words diet plan for a {age}-year-old {gender} weighing {weight} kg who has{disease} disease and follows a {diet_preference} diet.
    """

    prompt = PromptTemplate(input_variables=['age', 'gender', 'weight', 'disease', 'diet_preference'],
                            template=template)

    response = llm(prompt.format(age=age, gender=gender, weight=weight, disease=disease, diet_preference=diet_preference))
    print(response)
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    age = int(request.form['age'])
    gender = request.form['gender']
    weight = float(request.form['weight'])
    disease = request.form['disease']
    diet_preference = request.form['diet_preference']

    response = get_llama_response(age, gender, weight, disease, diet_preference)
    return render_template('result.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
