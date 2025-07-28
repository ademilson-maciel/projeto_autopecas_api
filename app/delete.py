from flask import redirect, url_for, flash
from app.models import Peca
from app.database import db

def deletar_peca(id_codigo):
    peca = Peca.query.get(id_codigo)
    db.session.delete(peca)
    db.session.commit()
    flash("ITEM EXCLUÍDO COM SUCESSO!", "success")
    return redirect(url_for('index'))