import asyncio
import random

import aiohttp
import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 400
SIZE = 1000


def get_pokemon_sync(id_: str) -> str:
    url = BASE_URL + id_
    response = requests.get(url)
    return response.json()["name"]


def get_random_id() -> str:
    random_id = random.randint(1, MAX_POKEMON + 1)
    return str(random_id)


def get_random_pokemon() -> str:
    random_id = get_random_id()
    return get_pokemon_sync(random_id)


def get_random_pokemon_url() -> str:
    random_id = get_random_id()
    return BASE_URL + str(random_id)


async def get_rand_pokemon(my_session, get_random_pokemon_url):
    async with my_session.get(get_random_pokemon_url) as response:
        pokemon = await response.json()
        return pokemon["name"]


async def main():
    
    print('Running' + '.' * 30)
    
    async with aiohttp.ClientSession() as my_session:
        
        tasks = []
        for _ in range(SIZE):
            random_pokemon_url = get_random_pokemon_url()
            tasks.append(asyncio.create_task(get_rand_pokemon(my_session, random_pokemon_url)))
        pokemons = await asyncio.gather(*tasks)
    
    print(f"All names of random pokemons: {pokemons}")


asyncio.run(main())
