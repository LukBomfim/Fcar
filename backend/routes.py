from flask import render_template, Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/contato')
def contato():
    return render_template('contato.html')

@routes.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')