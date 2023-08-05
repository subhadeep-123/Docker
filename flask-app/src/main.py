from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_msg():
    return jsonify({"msg": 'Hello world from Python', 'version': '1.0.0'})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)