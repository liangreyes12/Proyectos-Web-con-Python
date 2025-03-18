from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Tarea

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "clave_secreta"

db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        titulo = request.form["titulo"]
        descripcion = request.form["descripcion"]
        nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion, realizada=False)
        db.session.add(nueva_tarea)
        db.session.commit()
        return redirect(url_for("index"))

    tareas = Tarea.query.all()
    return render_template("index.html", tareas=tareas)

@app.route("/realizar/<int:tarea_id>")
def marcar_realizada(tarea_id):
    tarea = Tarea.query.get_or_404(tarea_id)
    tarea.realizada = not tarea.realizada
    db.session.commit()
    return jsonify({"realizada": tarea.realizada})  # Devuelve JSON para actualizar UI sin recargar

@app.route("/eliminar/<int:tarea_id>")
def eliminar_tarea(tarea_id):
    tarea = Tarea.query.get_or_404(tarea_id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
