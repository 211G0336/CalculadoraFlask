from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]
            if operacion == "sumar":
                resultado = num1 + num2
            elif operacion == "restar":
                resultado = num1 - num2
            elif operacion == "multiplicar":
                resultado = num1 * num2
            elif operacion == "dividir":
                resultado = num1 / num2 if num2 != 0 else "Error: división por cero"
        except ValueError:
            error = "Por favor ingresa números válidos."
    return render_template("index.html", resultado=resultado, error=error)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
