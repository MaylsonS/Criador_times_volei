from flask import Blueprint, render_template, request
from database.grupos import DUPLA, TRIO, SEIS

amistoso_route = Blueprint("amistoso_route", __name__)

@amistoso_route.route("/")
def formacao():
    return render_template("formacao.html")


# mostrar tela de formação
# Formação de Duplas, Trios e Seis
# Listar amistoso

