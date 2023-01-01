from game import Game


class Server:

    def __init__(self, port: int = 1000):
        self.port: int = port
        self.games: set[Game] = set()
        self.request_handler = None

    def run(self):
        # create request handler
        pass


def main():
    Server().run()


if __name__ == '__main__':
    main()
