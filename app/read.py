from app.models import Peca

def listar_pecas(filtro=None):
    if filtro:
        filtro = filtro.upper()
        return Peca.query.filter(
            (Peca.id_codigo.contains(filtro)) | (Peca.descricao.contains(filtro))
        ).all()
    return Peca.query.all()