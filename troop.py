from typing import Optional


class Troop:
    default_max_health: int = 1
    default_movement: int = 3
    default_size: float = 1.0
    default_cost: dict[str, int] = {}

    def __init__(self):
        self.max_health: int = self.default_max_health
        self.movement: int = self.default_movement
        self.health: int = self.default_max_health
        self.size: float = self.default_size

        self.container: Optional[TroopContainer] = None
        self.owner: Optional[None] = None

    def remove_container(self):
        if self.container:
            self.container.remove_troop(self)
            self.container = None

    def add_container(self, container: 'TroopContainer'):
        self.remove_container()
        if container:
            self.container = container
            container.add_troop(self)


class BasicTroop(Troop):
    default_power: dict[str, float] = {'skirmish': 0.0, 'attack': 0.0, 'defense': 0.0, 'chase': 0.0, 'retreat': 0.0}

    def __init__(self):
        super().__init__()
        self.power: dict[str, float] = self.default_power.copy()


class RangedTroop(BasicTroop):
    default_range: int = 1
    default_power: dict[str, float] = BasicTroop.default_power.copy().update({'ranged': 0.0}) # TODO fix :'(

    def __init__(self):
        super().__init__()
        self.range = self.default_range


class TroopContainer:

    def __init__(self, max_capacity):
        self.max_capacity: float = max_capacity
        self.capacity: float = 0
        self.troops: set[Troop] = set()

    def can_house(self, troop: Troop) -> bool:
        if not troop:
            return False
        return self.capacity + troop.size <= self.max_capacity

    def remove_troop(self, troop: Troop) -> None:
        if troop and troop in self.troops:
            self.troops.remove(troop)
            self.capacity -= troop.size
            troop.remove_container()

    def add_troop(self, troop) -> None:
        if troop and troop not in self.troops:
            troop.remove_container()
            self.troops.add(troop)
            self.capacity += troop.size
            troop.add_container(self)
