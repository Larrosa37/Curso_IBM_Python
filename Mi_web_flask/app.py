from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    tareas =["Estudiar python","hacer pequeños proyectos para practicar","Leer sobre python","Practicar y aprender inglés"]
    compras = ["Leche","Huevos","Pan","Agua","Monster verde"]
    return render_template("index.html", tareas=tareas , compras=compras)

if __name__ == "__main__":
    app.run(debug=True)