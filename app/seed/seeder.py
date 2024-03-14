from datetime import datetime, timedelta
from random import randint, choice
from ...app import app
from app.models.pokemons import db, Item, Pokemon, PokemonType


images = [
    "/images/pokemon_berry.svg",
    "/images/pokemon_egg.svg",
    "/images/pokemon_potion.svg",
    "/images/pokemon_super_potion.svg"
]


with app.app_context():
    # db.drop_all()
    # print("DROPPED ALL TABLES!!!!!!")
    # db.create_all()
    # print("CREATED ALL TABLES")

    pokemons = [
        {
                "number": 1,
                "imageUrl": '/images/pokemon_snaps/1.svg',
                "name": 'Bulbasaur',
                "attack": 49,
                "defense": 49,
                "type": 'grass',
                "moves": [
                  'tackle',
                  'vine whip'
                ],
                "captured": True
            },
             {
                "number": 2,
                "imageUrl": '/images/pokemon_snaps/2.svg',
                "name": 'Ivysaur',
                "attack": 62,
                "defense": 63,
                "type": 'grass',
                "moves": [
                  'tackle',
                  'vine whip',
                  'razor leaf'
                ],
                "captured": True
              },
              {
                "number": 3,
                "imageUrl": '/images/pokemon_snaps/3.svg',
                "name": 'Venusaur',
                "attack": 82,
                "defense": 83,
                "type": 'grass',
                "moves": [
                  'tackle',
                  'vine whip',
                  'razor leaf'
                ],
                "captured": True
              },
              {
                "number": 4,
                "imageUrl": '/images/pokemon_snaps/4.svg',
                "name": 'Charmander',
                "attack": 52,
                "defense": 43,
                "type": 'fire',
                "moves": [
                  'scratch',
                  'ember',
                  'metal claw'
                ],
                "captured": True
              },
              {
                "number": 5,
                "imageUrl": '/images/pokemon_snaps/5.svg',
                "name": 'Charmeleon',
                "attack": 64,
                "defense": 58,
                "type": 'fire',
                "moves": [
                  'scratch',
                  'ember',
                  'metal claw',
                  'flamethrower'
                ],
                "captured": True
              },
              {
                "number": 6,
                "imageUrl": '/images/pokemon_snaps/6.svg',
                "name": 'Charizard',
                "attack": 84,
                "defense": 78,
                "type": 'fire',
                "moves": [
                  'flamethrower',
                  'wing "attack"',
                  'slash',
                  'metal claw'
                ],
                "captured": True
              },
              {
                "number": 7,
                "imageUrl": '/images/pokemon_snaps/7.svg',
                "name": 'Squirtle',
                "attack": 48,
                "defense": 65,
                "type": 'water',
                "moves": [
                  'tackle',
                  'bubble',
                  'water gun'
                ],
                "captured": True
              },
              {
                "number": 8,
                "imageUrl": '/images/pokemon_snaps/8.svg',
                "name": 'Wartortle',
                "attack": 63,
                "defense": 80,
                "type": 'water',
                "moves": [
                  'tackle',
                  'bubble',
                  'water gun',
                  'bite'
                ],
              },
              {
                "number": 9,
                "imageUrl": '/images/pokemon_snaps/9.svg',
                "name": 'Blastoise',
                "attack": 83,
                "defense": 100,
                "type": 'water',
                "moves": [
                  'hydro pump',
                  'bubble',
                  'water gun',
                  'bite'
                ],
              },
              {
                "number": 10,
                "imageUrl": '/images/pokemon_snaps/10.svg',
                "name": 'Caterpie',
                "attack": 30,
                "defense": 35,
                "type": 'bug',
                "moves": [
                  'tackle'
                ],
              },
              {
                "number": 12,
                "imageUrl": '/images/pokemon_snaps/12.svg',
                "name": 'Butterfree',
                "attack": 45,
                "defense": 50,
                "type": 'bug',
                "moves": [
                  'confusion',
                  'gust',
                  'psybeam',
                  'silver wind'
                ],
              },
              {
                "number": 13,
                "imageUrl": '/images/pokemon_snaps/13.svg',
                "name": 'Weedle',
                "attack": 35,
                "defense": 30,
                "type": 'bug',
                "moves": [
                  'poison sting'
                ],
              },
              {
                "number": 16,
                "imageUrl": '/images/pokemon_snaps/16.svg',
                "name": 'Pidgey',
                "attack": 45,
                "defense": 40,
                "type": 'normal',
                "moves": [
                  'tackle',
                  'gust'
                ],
              },
              {
                "number": 17,
                "imageUrl": '/images/pokemon_snaps/17.svg',
                "name": 'Pidgeotto',
                "attack": 60,
                "defense": 55,
                "type": 'normal',
                "moves": [
                  'tackle',
                  'gust',
                  'wing "attack"'
                ],
              },
              {
                "number": 18,
                "imageUrl": '/images/pokemon_snaps/18.svg',
                "name": 'Pidgeot',
                "attack": 80,
                "defense": 75,
                "type": 'normal',
                "moves": [
                  'tackle',
                  'gust',
                  'wing "attack"'
                ],
              },
              {
                "number": 19,
                "imageUrl": '/images/pokemon_snaps/19.svg',
                "name": 'Rattata',
                "attack": 56,
                "defense": 35,
                "type": 'normal',
                "moves": [
                  'tackle',
                  'hyper fang'
                ],
              },
              {
                "number": 20,
                "imageUrl": '/images/pokemon_snaps/20.svg',
                "name": 'Raticate',
                "attack": 81,
                "defense": 60,
                "type": 'normal',
                "moves": [
                  'tackle',
                  'hyper fang'
                ],
              }
         ]

    # generate items
    for pokemon in pokemons:
        pokemon = Pokemon(**pokemon)
        db.session.add(pokemon)

    db.session.commit()



    # lunas_posts = [
    #         {
    #             "caption": "my best buddy!",
    #             "image": "https://pipstagram.s3.amazonaws.com/15035574_1079682388796264_6184137089534132224_n.jpg",
    #             "created_at": random_date_2023(),
    #         }
    #     ]

    # lokis_posts = [
    #         {
    #             "caption": "allow me to introduce myself",
    #             "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.53.08.jpg",
    #             "created_at": random_date_2023(),
    #         },
    #         {
    #             "caption": "mmmm... dirt!",
    #             "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.53.30.jpg",
    #             "created_at": random_date_2023(),
    #         },
    #         {
    #             "caption": "please sir, i beg of you",
    #             "image": "https://pipstagram.s3.amazonaws.com/2023-07-17+14.57.09.jpg",
    #             "created_at": random_date_2023(),
    #         }
    #     ]

    # users = [
    #         {
    #             "name": "Pip"
    #         },
    #         {
    #             "name": "Luna"
    #         },
    #         {
    #             "name": "Loki"
    #         }
    #         ]

    # for user in users:
    #     current_user = User(**user)
    #     db.session.add(current_user)
    #     # print(f"SEEDED USER {current_user.name}")

    # for post in pip_posts:
    #     current_post = Post(**post)
    #     current_post.author_id = 1
    #     db.session.add(current_post)

    # for post in lunas_posts:
    #     current_post = Post(**post)
    #     current_post.author_id = 2
    #     db.session.add(current_post)

    # for post in lokis_posts:
    #     current_post = Post(**post)
    #     current_post.author_id = 3
    #     db.session.add(current_post)


    # db.session.commit()