from flask import Blueprint


bp = Blueprint('bp', __name__, url_prefix='/api/pokemon')

@bp.route('/')
def pokemon():
    pass
