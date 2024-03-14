from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PokemonType(db.Model):
    __tablename__ = "pokemon_types"
    
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    
    pokemons = db.relationship('Pokemon', back_populates='type')