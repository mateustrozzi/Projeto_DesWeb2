from flask import Blueprint, render_template, request, redirect
from models.evento import Evento
from dao.data import EventoDAO

evento_bp = Blueprint("evento", __name__)

@evento_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vagas = request.form.get("vagas", 0)
        try:
            vagas = int(vagas)
        except (ValueError, TypeError):
            vagas = 0

        evento = Evento(
            nome=request.form["nome"],
            data=request.form["data"],
            local=request.form["local"],
            vagas=vagas
        )
        EventoDAO.salvar_evento(evento)
        return redirect("/")

    eventos = EventoDAO.listar()
    return render_template("index.html", eventos=eventos)
