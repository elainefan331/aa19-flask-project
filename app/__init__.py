from flask import Flask
from .config import Configuration
from flask_migrate import Migrate
from .models.pokemons import db, PokemonType, Pokemon, Item
import os

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf



# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response