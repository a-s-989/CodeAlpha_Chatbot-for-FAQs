from flask import Flask, render_template, request
from gemini_api import fetch_answer_gemini

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get("msg")
    response = fetch_answer_gemini(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)