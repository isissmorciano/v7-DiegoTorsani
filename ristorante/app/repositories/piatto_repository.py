from app.db import get_db


# TODO: Implementa le funzioni richieste dall'esercizio 1 e 2
def get_all_piatti():
    """
    Recupera tutti i canali.
    """
    db = get_db()
    query = """
        SELECT *
        FROM piatti
    """
    channels = db.execute(query).fetchall()
    return [dict(channel) for channel in channels]

def get_piatti_by_category(category_id):
    """Recupera un singolo canale per ID."""
    db = get_db()
    query = """
        SELECT c.id, c.nome, c.numero_iscritti, p.nome AS categoria
        FROM category c
        JOIN piatti p ON p.categoria_id = c.id
        WHERE c.id = ?
    """
    category = db.execute(query, (category_id,)).fetchone()
    if category:
        return dict(category)
    return None

def get_piatto_by_id(piatto_id):
    """Recupera un singolo canale per ID."""
    db = get_db()
    query = """
        SELECT *
        FROM piatto p
        WHERE p.id = ?
    """
    piatto = db.execute(query, (piatto_id,)).fetchone()
    if piatto:
        return dict(piatto)
    return None

def create_piatto(category_id, nome, prezzo):
    """Crea un nuovo canale."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO canali (category_id, nome, prezzo) VALUES (?, ?, ?)", (category_id, nome, prezzo)
    )
    db.commit()
    return cursor.lastrowid