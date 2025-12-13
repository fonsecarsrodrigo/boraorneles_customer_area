from flask import Flask
from flask import redirect
from flask_openapi3 import OpenAPI, Info


info = Info(title="Bora Orneles Customer Area API", version="1.0.0")
app = OpenAPI(__name__, info=info)

@app.route("/")
def home():
     return redirect('/openapi')

if __name__ == "__main__":
    app.run(debug=True)