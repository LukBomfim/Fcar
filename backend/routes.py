from flask import render_template, Blueprint, jsonify, request
from dotenv import load_dotenv
import os
import json

load_dotenv()
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/contato', methods=['GET','POST'])
def contato():
    if request.method == 'POST':
        dados = request.get_json()
        nome = dados.get('nome')

        print(json.dumps(dados, indent=4))
        return jsonify({
            'status': 'sucesso', 
            'message': f'Mensagem recebida de: {nome}'
            })

    return render_template('contato.html')

@routes.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')