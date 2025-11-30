from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bora Orneles Customer Area Server is running!"

if __name__ == "__main__":
    app.run(debug=True)