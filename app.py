from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/add')
def add():
    num1 = int(request.args.get('num1'));
    num2 = int(request.args.get('num2'));

    return f"{num1} + {num2} = {num1 + num2}"

if __name__ == "__main__":
    #app.run(debug=True);
    app.run(host="0.0.0.0", port=int("1234"), debug=True)
