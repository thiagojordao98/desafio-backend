from flask import Blueprint, request
from ..controllers.pessoa_controller import create_pessoa, update_pessoa, delete_pessoa, get_all_pessoas, get_pessoa

pessoa_bp = Blueprint('pessoa_bp', __name__)

@pessoa_bp.route('/pessoas', methods=['POST'])
def create():
    data = request.json
    return create_pessoa(data)

@pessoa_bp.route('/pessoas/<int:idPessoa>', methods=['PUT'])
def update(idPessoa):
    data = request.json
    return update_pessoa(idPessoa, data)

@pessoa_bp.route('/pessoas/<int:idPessoa>', methods=['DELETE'])
def delete(idPessoa):
    return delete_pessoa(idPessoa)

@pessoa_bp.route('/pessoas', methods=['GET'])
def get_all():
    return get_all_pessoas()

@pessoa_bp.route('/pessoas/<int:idPessoa>', methods=['GET'])
def get(idPessoa):
    return get_pessoa(idPessoa)
