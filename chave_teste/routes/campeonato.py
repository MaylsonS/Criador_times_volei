from flask import Blueprint, render_template, request, redirect, url_for, session
from database.grupos import DUPLA, TRIO, SEIS

campeonato_route = Blueprint("campeonato_route", __name__)

@campeonato_route.route("/", methods=["GET", "POST"])
def home():
    return "aaa"