from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import categoria_repository, piatto_repository

bp = Blueprint("main", __name__)


# TODO: Implementa le route richieste dall'esercizio 1 e 2
@bp.route("/")
def index():


    # 1. Prendiamo i canali dal database
    categoria: list[dict] = categoria_repository.get_all_categories()

    # 2. Passiamo la variabile 'channels' al template
    return render_template("base.html", categoria=categoria)
