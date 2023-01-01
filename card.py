import random
from typing import Any
from types import FunctionType


class Card:

    def __init__(self, title: str = '', description: str = ''):
        self.title: str = title
        self.description: str = description


class HistoricalCard(Card):

    def __init__(self, func: FunctionType, args: tuple = None, title: str = '', description: str = ''):
        super().__init__(title=title, description=description)
        if not args:
            args = ()
        self.func: FunctionType = func
        self.args: tuple = args

    def play(self, player: Any):
        self.func(player, *self.args)


class Deck:

    def __init__(self):
        self.cards: list[Card] = []
        self.draw_pile: list[Card] = []
        self.discard_pile: list[Card] = []

    def shuffle(self) -> None:
        random.shuffle(self.draw_pile)

    def new_draw_pile(self) -> None:
        self.draw_pile = self.cards.copy()
        self.discard_pile = []
        self.shuffle()

    def draw_from_top(self) -> Card:
        if not self.draw_pile:
            self.new_draw_pile()
        return self.draw_pile.pop(-1) if self.draw_pile else None

    def discard(self, card: Card) -> None:
        self.discard_pile.append(card)

    def __str__(self) -> str:
        return f'Cards: {self.cards}.\nDraw pile: {self.draw_pile}.\nDiscard pile: {self.discard_pile}.'
