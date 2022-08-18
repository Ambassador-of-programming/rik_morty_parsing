import requests


def get_list_characters() -> list:
    url = 'https://rickandmortyapi.com/api/character/'
    data = requests.get(url).json()
    data = data['results']
    return data


def get_character_names() -> list:
    return [i['name'] for i in get_list_characters()]


def _get_character_data(name: str) -> dict:
    characters = {i['name']: i['id'] for i in get_list_characters()}
    char_id = characters[name]
    url = f"https://rickandmortyapi.com/api/character/{char_id}"
    data = requests.get(url).json()
    return data


def get_character_text(name: str) -> str:
    try:
        data = _get_character_data(name)
        text = f"""\
        \nImage: {data['image']}
        \nИдентификатор персонажа: {data['id']}\
        \nИмя персонажа: {data['name']}\
        \nСтатус персонажа: {data['status']}\
        \nВид персонажа: {data['species']}\
        \nТип или подвид персонажа: {data['type']}\
        \nПол персонажа: {data['gender']}\
        \nПроисхождение: {data['location']['name']}\
        \nМестоположение: {data['location']['name']}
        """
        return text
    except Exception:
        return 'Персонажа с токим именем не существует'
