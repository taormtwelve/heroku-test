from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def helloDef():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)