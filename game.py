from server import Server
from assets import Assets
from game_settings import GameSettings


class Game:

    def __init__(self, server: Server, assets: Assets, game_settings: GameSettings):
        self.server: Server = server
        self.assets: Assets = assets
        self.game_settings = game_settings
        self.players: list = []
        self.round_num: int = 0
        self.stop: bool = False

    def run(self):
        while not self.stop:
            pass
