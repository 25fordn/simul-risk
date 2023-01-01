from json import load
from os import listdir
from card import Card
import troop

RESOURCE_DIR = '/resources'
RESOURCE_FILE = '/resources.json'
TROOP_DIR = '/troops'
TROOP_STATS_FILE = '/stats.json'
TROOP_CLASS_TABLE = {'ranged': troop.RangedTroop, 'basic': troop.BasicTroop}
TROOP_ICON_FILE = '/icon.png'
TROOP_MODEL_FILE = '/model.png'
CARD_DIR = '/cards'


class Assets:

    def __init__(self, resources: list = None, troops: list = None, cards: list = None):
        if not resources:
            resources = []
        if not troops:
            troops = []
        if not cards:
            cards = []
        self.resources: list[str] = resources
        self.troops: list[type] = troops
        self.cards: list[Card] = cards


def resources_from_json(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:      # throws FileNotFoundError if file_path is invalid
        resources = load(file)              # throws json.decoder.JSONDecodeError if invalid json
        if not isinstance(resources, list):
            raise Exception(f'json in file {file_path} is not correct format for resources.')
        return resources


def load_resources(dir_path: str) -> list[str]:
    return resources_from_json(dir_path + RESOURCE_FILE)


def create_troop_subclass(class_name: str, base_classes: tuple = (troop.Troop,), member_fields=None) -> type:
    return type(class_name, base_classes, member_fields)


def troop_from_json(dir_path: str) -> type:
    with open(dir_path + TROOP_STATS_FILE, 'r') as file:
        stats = load(file)
        base_classes = []
        for k, v in TROOP_CLASS_TABLE.items():
            if k in stats['classes']:
                base_classes.append(v)
        del stats['classes']
        name = stats['name']
        del stats['name']
        return create_troop_subclass(name, tuple(base_classes), stats)


def load_troops(dir_path: str) -> list[type]:
    troops = []
    for troop_path in listdir(dir_path):
        troops.append(troop_from_json(dir_path + '/' + troop_path))
    return troops


def load_cards(dir_path: str) -> list[Card]:
    return []


def load_from_dir(dir_path: str) -> Assets:
    resources = load_resources(dir_path + RESOURCE_DIR)
    troops = load_troops(dir_path + TROOP_DIR)
    cards = load_cards(dir_path + CARD_DIR)
    return Assets(resources, troops, cards)
