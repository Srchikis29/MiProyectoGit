from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de espera (en memoria)
lista_espera = []

@app.route("/", methods=["GET", "POST"])
def index():
    global lista_espera
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        if nombre and apellido:
            lista_espera.append(f"{nombre} {apellido}")
        return redirect(url_for("index"))
    return render_template("index.html", lista=lista_espera)

@app.route("/siguiente")
def siguiente():
    global lista_espera
    if lista_espera:
        lista_espera.pop(0)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)