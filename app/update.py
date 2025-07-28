from flask import request, redirect, url_for, flash
from app.models import Peca
from app.database import db

def atualizar_peca(id_codigo):
    peca = Peca.query.get(id_codigo)

    if request.method == 'POST':
        peca.id_codigo = request.form['codigo'].upper()
        peca.descricao = request.form['descricao'].upper()
        peca.fabricante = request.form['fabricante'].upper()
        peca.aplicacao = request.form['aplicacao'].upper()
        db.session.commit()

        flash("ITEM ATUALIZADO COM SUCESSO!", "success")
        return redirect(url_for('index'))

    return peca