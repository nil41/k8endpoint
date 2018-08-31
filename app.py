from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/city")
def city():
    citydata = {"name": "pune", "pincode": 416011 }
    return jsonify(citydata)


@app.route("/employee")
def empolyee():
    result = {"id": 1, "name": "Prince"}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
