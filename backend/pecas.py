from flask import Blueprint, render_template

pecas_bp = Blueprint('pecas', __name__)

@pecas_bp.route('/pecas')
def pecas():
    return render_template('/paginas-pecas/pecas.html')