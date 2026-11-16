from flask import Flask,jsonify,request,render_template
from calculator import calculate

app=Flask(__name__)

@app.route("/")
def home() :
    return render_template("index.html")

@app.route("/calculate")
def calculate_route():
    try:
        first_number = float(request.args.get("first"))
        second_number = float(request.args.get("second"))
    except (TypeError, ValueError):
        return jsonify({"error": "Provide two valid numbers"}), 400

    operator = request.args.get("operator")

    if operator not in ("+", "-", "*", "/"):
        return jsonify({"error": "Invalid operator"}), 400

    if operator == "/" and second_number == 0:
        return jsonify({"error": "Can't divide by zero"}), 400

    result = calculate(first_number, second_number, operator)
    return jsonify({"result": result})

if __name__=="__main__":
   app.run()