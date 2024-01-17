import flask
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = flask.Flask(__name__)

# Load model and tokenizer locally
model_name = "model\llama-2-7b-chat.ggmlv3.q8_0.bin"  # Replace with your model path
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    age = int(flask.request.form["age"])
    weight = int(flask.request.form["weight"])
    diseases = flask.request.form["diseases"]
    diet_preference = flask.request.form["diet_preference"]

    # Construct prompt using tokenizer
    prompt = tokenizer.encode(
        f"Generate a customized diet plan for a {age}-year-old person weighing {weight} kg who {diseases} and follows a {diet_preference} diet.",
        return_tensors="pt",
    )

    # Generate diet plan using the model
    response = model.generate(prompt, max_length=500, num_return_sequences=1)
    generated_text = tokenizer.decode(response[0], skip_special_tokens=True)

    return flask.render_template("response.html", generated_plan=generated_text)

if __name__ == "__main__":
    app.run(debug=True)
