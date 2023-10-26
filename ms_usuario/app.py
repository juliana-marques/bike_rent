from flask import Blueprint, request, Response, abort

app_usuario = Blueprint('app_usuario', __name__)

@app_usuario.route("/teste", methods=['GET'])
def ciclista():
    return "Teste"
