from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from app.repositories import categoria_repository, piatto_repository

bp = Blueprint("main", __name__)


# TODO: Implementa le route richieste dall'esercizio 1 e 2
@bp.route("/")
def index():


    # 1. Prendiamo i canali dal database
    categorie: list[dict] = categoria_repository.get_all_categories()

    # 2. Passiamo la variabile 'channels' al template
    return render_template("index.html", categorie=categorie)

@bp.route("/category/<int:id>")
def category_detail(id):
    # 1. Prendiamo il canale
    category = categoria_repository.get_category_by_id(id)
    if category is None:
        abort(404, "categoria non trovata.")

    # 2. Prendiamo i video del canale
    piatti = piatto_repository.get_piatti_by_category(id)

    # 3. Passiamo al template
    return render_template("categoria_detail.html", category=category, piatto=piatti)


@bp.route("/crea_categoria")
def crea_categoria(id):
    pass

@bp.route("/crea_piatto")
def crea_piatto(id):
    pass

@bp.route("/ricerca")
def ricerca(id):
    pass