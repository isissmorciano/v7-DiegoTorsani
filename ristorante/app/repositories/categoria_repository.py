from app.db import get_db


# TODO: Implementa le funzioni richieste dall'esercizio 1 e 2
def get_all_categories():
    """
    Recupera tutte le categorie.
    """
    db = get_db()
    query = """
        SELECT * FROM categoria ORDER BY nome
    """
    categories = db.execute(query).fetchall()
    return [dict(category) for category in categories]

def get_category_by_id(category_id):
    """Recupera un singolo canale per ID."""
    db = get_db()
    query = """
        SELECT *
        FROM category c
        WHERE c.id = ?
    """
    category = db.execute(query, (category_id,)).fetchone()
    if category:
        return dict(category)
    return None

def create_category(nome):
    """Crea un nuovo canale."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO category (nome) VALUES (?)", (nome)
    )
    db.commit()
    return cursor.lastrowid