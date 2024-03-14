from flask import Blueprint, Flask, redirect
import json
from db.pokemonrepository import PokemonRepository

from db.itemsrepository import ItemsRepository
from .utils import randomItemImage

app = Blueprint ('pokemonRoutes', __name__)

@app.route('/')
def getAllPokemon():
    pokemon = PokemonRepository.list()
    return pokemon

@app.route('/', methods=['POST'])
def createPokemon():
    id = PokemonRepository.create(app.json)
    return redirect ({"id": id}), 

@app.route('/:id', methods=['PUT'])
def update_pokemon(id):
    PokemonRepository.update(id, app.json)
    pokemon = PokemonRepository.one(id)
    return pokemon

@app.route('/types')
def get_pokemon_types():
    pokemonType = PokemonRepository.pokemonType()
    return pokemonType

@app.route('/random')
def get_random_pokemon():
    pokemon = PokemonRepository.random()
    return pokemon

@app.route('/battle')
def pokemon_battle():
    allyId = app.args.get('allyId')
    opponentId = app.args.get('opponentId')
    pokemon = PokemonRepository.battle(allyId, opponentId)
    return pokemon

@app.route('/:id')
def get_single_pokemon(id):
    pokemon = PokemonRepository.one(id)
    return pokemon

@app.route('/:id/items')
def getById(id):
    items = ItemsRepository.itemsByPokemonId(id)
    return items

@app.route('/:id/items', methods=['POST'])
def addItem(id):
    if 'imageUrl' not in app.json:
        app.json['imageUrl'] = randomItemImage()
    item = ItemsRepository.add_item(app.json, id)
    return item
