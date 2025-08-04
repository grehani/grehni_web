from flask import Flask, render_template, request, jsonify
from grehni_core import process_input

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    reply = process_input(user_input)
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {user_input}\nGrehni: {reply}\n")
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))