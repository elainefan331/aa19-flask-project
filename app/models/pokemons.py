from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pokemon(db.Model):
    __tablename__= "pokemons"
    
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    moves = db.Column(db.String, nullable=False)
    encounterRate = db.Column(db.Numeric(3, 2))
    catchRate = db.Column(db.Numeric(3, 2))
    captured = db.Column(db.Boolean)
    typeId = db.Column(db.String, db.ForeignKey('pokemon_types.id'))
    
    type = db.relationship("PokemonType", back_populates='pokemons')
    items = db.relationship('Item', back_populates="pokemon")
    
    
class PokemonType(db.Model):
    __tablename__ = "pokemon_types"
    
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    
    pokemons = db.relationship('Pokemon', back_populates='type')
    
    
class Item(db.Model):
    __tablename__ = "items"
    
    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer)
    imageUrl = db.Column(db.String, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemonId = db.Column(db.Integer, db.ForeignKey("pokemons.id"), nullable=False)
    
    pokemon = db.relationship("Pokemon", back_populates="items")
    