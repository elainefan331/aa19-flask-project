from faker import Faker
from ..models import Pokemon
from ..models import PokemonType

import random

faker = Faker()

def random100():
    return random.randint(1,100)

def randomImage():
    images= [
    "/images/pokemon_berry.svg",
    "/images/pokemon_egg.svg",
    "/images/pokemon_potion.svg",
    "/images/pokemon_super_potion.svg",
    ];
    index = random.randint(0, len(images)-1)
    return images[index]

def generateItems():
    for i in range(3):
        yield {
            "name": faker.productName(),
            "price": random100(),
            "happiness": random100(),
            "imageUrl": randomImage(),
        }


async def create(details):
    details["items"] = list(generateItems())
    pokemon = await Pokemon.create(details, include=["items"])
    return pokemon.id


async def update(details):
    id = details["id"]
    del details["id"]
    await Pokemon.update(
        details,
        where = {"id" : id},
        returning = True,
        plain = True
    )
    return id;

async def typeList():
    return await PokemonType.findAll();

async def list():
    return await Pokemon.findAll();


async def one(id):
    return await Pokemon.scope("detailed").findByPk(id)


async def random():
    pokemon = await Pokemon.scope(["random","opponent"].findAll())
    weightedSum = pokemon.reduce(lambda sum, i: sum + i.encounterRate,pokemon,0 )
    randomSum = random.random() * weightedSum
    chosenId = None
    for i in pokemon:
        if randomSum < i.encounterRate :
            chosenId = i
