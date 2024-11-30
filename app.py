from flask import Flask, render_template, request, jsonify, send_from_directory
import json

app = Flask(__name__)

@app.route('/static/images')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# Load chatbot.json data
with open('chatbot.json', 'r', encoding='utf-8') as f:
    chatbot_data = json.load(f)

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.json.get("message", "").lower()
    response = "Maaf, saya tidak menemukan jawaban untuk pertanyaan Anda."

    # Pisahkan pesan pengguna menjadi daftar kata
    words = user_message.split()

    # Cek setiap kata dalam urutan hingga menemukan kecocokan
    for word in words:
        for key, value in chatbot_data.items():
            if key.lower() == word:
                response = value if isinstance(value, str) else " ".join(value)
                return jsonify({"response": response})  # Kembalikan respons segera setelah ditemukan

    return jsonify({"response": response})

@app.route("/detection")
def detection():
    return render_template("detection-1.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()