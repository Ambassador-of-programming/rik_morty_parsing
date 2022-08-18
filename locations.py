import requests


def get_list_locations() -> list:
    url = "https://rickandmortyapi.com/api/location"
    r = requests.get(url)
    data = r.json()['results']
    return data

def get_location_names() -> list:
    return [i['name'] for i in get_list_locations()]


def get_location_data(name: str) -> dict:
    locations = {i['name']: i['id'] for i in get_list_locations()}
    loc_id = locations[name]
    url = f"https://rickandmortyapi.com/api/location/{loc_id}"
    data = requests.get(url).json()
    return data

def parse_data(name: str) -> str:
    data = get_location_data(name)
    residenta = data['residents']
    names = []
    for url in residenta:
        r =  requests.get(url).json()
        name = r['name']
        names.append(name)
    text = f"""
id: {data['id']}
name: {data['name']}
type: {data['type']}
dimension: {data['dimension']}
created: {data['created']}
res: {names}
"""
    return text


