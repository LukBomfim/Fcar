from flask import Blueprint, render_template

oleo_bp = Blueprint('oleo', __name__)

@oleo_bp.route('/oleo')
def oleo():
    return render_template('/paginas-oleo/oleo.html')