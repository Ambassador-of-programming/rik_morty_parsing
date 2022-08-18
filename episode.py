import requests

def get_list_episode() -> list:
    url = "https://rickandmortyapi.com/api/episode"
    r = requests.get(url)
    data = r.json()['results']
    return data



def get_episode_id(name: str) -> dict:
    locations = {i['name']: i['id'] for i in get_list_episode()}
    loc_id = locations[name]
    url = f"https://rickandmortyapi.com/api/episode/{loc_id}"
    data = requests.get(url).json()
    return data


def get_episode_air_data() -> list:
    return [i['air_date'] for i in get_list_episode()]



def get_episode_name() -> list:
    return [i['name'] for i in get_list_episode()]


def parse_vse(name: str) -> str:
    data = get_episode_id(name)
    characters = data['characters']
    names = []
    for url in characters:
        r =  requests.get(url).json()
        name = r['name']
        names.append(name)
    text = f"""
id: {data['id']}
name: {data['name']}
dair_date: {data['air_date']}
episode: {data['episode']}
res: {names}
"""
    return text

