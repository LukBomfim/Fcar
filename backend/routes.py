from flask import render_template, Blueprint, jsonify, request
from backend.contato import *

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/contato', methods=['GET','POST'])
def contato():
    if request.method == 'POST':
        dados = request.get_json()
        
        enviarEmail(dados)

        return jsonify({
            'status': 'sucesso', 
            })

    return render_template('contato.html')

@routes.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')