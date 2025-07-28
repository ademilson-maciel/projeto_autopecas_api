from flask import render_template, request
from app.read import listar_pecas
from app.create import criar_peca
from app.update import atualizar_peca
from app.delete import deletar_peca

def register_routes(app):

    @app.route('/', methods=['GET'])
    def index():
        filtro = request.args.get('buscar')
        pecas = listar_pecas(filtro)
        return render_template('index.html', pecas=pecas, filtro=filtro)

    @app.route('/nova', methods=['GET', 'POST'])
    def nova():
        if request.method == 'POST':
            return criar_peca()
        return render_template('form.html', peca=None)

    @app.route('/editar/<string:id_codigo>', methods=['GET', 'POST'])
    def editar(id_codigo):
        peca = atualizar_peca(id_codigo)
        if request.method == 'POST':
            return peca
        return render_template('form.html', peca=peca)

    @app.route('/deletar/<string:id_codigo>')
    def deletar(id_codigo):
        return deletar_peca(id_codigo)