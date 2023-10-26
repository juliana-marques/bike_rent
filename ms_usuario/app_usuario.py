from flask import Blueprint, request, Response, abort

app_usuario = Blueprint('app_usuario', __name__)

@app_usuario.route("/ciclista/dados", methods=['GET'])
def ciclista():
    return "Dados do ciclista\n\nNome: Fulano\nIdade: Ciclano", 200
