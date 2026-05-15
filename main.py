from flask import Flask
from backend.routes import routes
from backend.pecas import pecas_bp
from backend.oleo import oleo_bp


app = Flask(__name__, 
            template_folder='frontend/templates', 
            static_folder='frontend/static')

app.register_blueprint(routes)
app.register_blueprint(pecas_bp)
app.register_blueprint(oleo_bp)

if __name__ == '__main__':
    app.run()