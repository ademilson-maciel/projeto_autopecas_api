from flask import request, redirect, url_for, flash
from app.models import Peca
from app.database import db

def criar_peca():
    if request.method == 'POST':
        id_codigo = request.form['codigo'].upper()
        descricao = request.form['descricao'].upper()
        fabricante = request.form['fabricante'].upper()
        aplicacao = request.form['aplicacao'].upper()

        # Verificar duplicidade
        if Peca.query.get(id_codigo):
            flash("CÓDIGO JÁ CADASTRADO!", "error")
            return redirect(url_for('nova'))

        nova = Peca(id_codigo=id_codigo, descricao=descricao,
                    fabricante=fabricante, aplicacao=aplicacao)
        db.session.add(nova)
        db.session.commit()

        flash("ITEM CADASTRADO COM SUCESSO!", "success")
        return redirect(url_for('index'))