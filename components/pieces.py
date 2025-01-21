from common import List, dataclass


class Piece:
    def __init__(self) -> None:
        self.balance: int = 1500
        self.position: int = 0
        self.properties = {}
        self.name: str = ''
        self.computer: bool = True

    def pick(self) -> None:
        self.name = input('Player Name:')
        self.computer = False

    def print_name(self) -> None:
        print(f'{self.name} ({self.__class__.__name__})')

    def print_name_location(self) -> None:
        print(f'{self.name} ({self.__class__.__name__}) landed on ')


class Pieces:
    class BattleShip(Piece):
        pass

    class TopHat(Piece):
        pass

    class Shoe(Piece):
        pass

    class Dog(Piece):
        pass

    class Car(Piece):
        pass

    class WheelBarrel(Piece):
        pass

    class Iron(Piece):
        pass

    class Thimble(Piece):
        pass
