from flask import Flask, render_template, request, jsonify, send_from_directory

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

if __name__ == '__main__':
    app.run()