from flask import render_template, Blueprint, jsonify, request

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/contato', methods=['GET','POST'])
def contato():
    if request.method == 'POST':
        dados = request.get_json()
        nome = dados.get('nome')

        print(f'Mensagem recebida de: {nome}')
        return jsonify({'status': 'success', 'message': f'Mensagem recebida de: {nome}'})

    return render_template('contato.html')

@routes.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')