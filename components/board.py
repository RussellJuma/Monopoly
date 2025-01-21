from common import List, dataclass
from pieces import Piece
from dataclasses import dataclass


@dataclass
class Property:
    color_group: object
    price: int
    rent: int
    buildable: bool = False
    house_price: int = 0
    hotel_price: int = 0
    mortgaged_value: int = False
    mortgaged: bool = False
    houses: int = 0
    hotels: int = 0
    owner: Piece = None

    def __post_init__(self):
        self.mortgaged_value = self.price // 2

    def buy_house(self, houses: int = 1) -> None:
        if self.houses + houses <= 4:
            self.houses += houses
            self.owner.balance -= houses * self.house_price

    def sell_house(self, houses: int = 1) -> None:
        if self.houses - houses >= 0:
            self.houses -= houses
            self.owner.balance += houses * self.house_price // 2

    def buy_hotel(self) -> None:
        if self.houses == 4 and self.hotels == 0:
            self.houses = 0
            self.hotels += 1
            self.owner.balance -= self.hotel_price

    def sell_hotel(self) -> None:
        if self.hotels == 1:
            self.hotels -= 1
            self.owner.balance += self.hotel_price // 2

    def landed_on(self, player: Piece) -> None:
        player.print_name_location()
        if self.owner is None:
            self._purchase()
        elif self not in player.properties:
            self._rent()

    def _purchase(self) -> None:

    def _rent(self) -> None:
        print()


class Board:
    def __init__(self):
        self.Utility = self.Utility()

    class Utility:
        def __init__(self):
            self.ElectricCompany = self.ElectricCompany(self)
            self.WaterWorks = self.WaterWorks(self)

        class Utility(Property):
            def __init__(self, group_color: object) -> None:
                super().__init__(group_color, 150)

            def rent(self):
                input('Roll the Dice.')
                if self.owner

        class ElectricCompany(Utility):
            pass

        class WaterWorks(Utility):
            pass

    class Railroads:
        def __init__(self):
            self.ReadingRailroad = self.ReadingRailroad(self)
            self.PennsylvaniaRailroad = self.PennsylvaniaRailroad(self)
            self.BORailroad = self.BORailroad(self)
            self.ShortLine = self.ShortLine(self)

        class ReadingRailroad(Property):
            def __init__(self, group_color: object) -> None:
                super().__init__(group_color, 200)

        class PennsylvaniaRailroad(Property):
            def __init__(self, group_color: object) -> None:
                super().__init__(group_color, 200)

        class BORailroad(Property):
            def __init__(self, group_color: object) -> None:
                super().__init__(group_color, 200)

        class ShortLine(Property):
            def __init__(self, group_color: object) -> None:
                super().__init__(group_color, 200)

    class Other:
        class Jail(Property):
            pass

        class IncomeTax(Property):
            pass

        class Jail(Property):
            pass

        class JustVisiting(Property):
            pass

        class GoToJail(Property):
            pass

        class CommunityChest(Property):
            pass

        class FreeParking(Property):
            pass

        class Chance(Property):
            pass

    class Brown:
        class MediterraneanAvenue(Property):
            pass

        class BalticAvenue(Property):
            pass

    class Teal:
        class OrientalAvenue(Property):
            pass

        class VermontAvenue(Property):
            pass

        class ConnecticutAvenue(Property):
            pass

    class Pink:
        class StCharlesPlace(Property):
            pass

        class StatesAvenue(Property):
            pass

        class VirginiaAvenue(Property):
            pass

    class Orange:
        class StJamesPlace(Property):
            pass

        class TennesseeAvenue(Property):
            pass

        class NewYorkAvenue(Property):
            pass

    class Red:
        class KentuckyAvenue(Property):
            pass

        class IndianaAvenue(Property):
            pass

        class IllinoisAvenue(Property):
            pass

    class Yellow:
        class AtlanticAvenue(Property):
            pass

        class VentnorAvenue(Property):
            pass

        class MarvinGardens(Property):
            pass

    class Green:
        class PacificAvenue(Property):
            pass

        class NorthCarolinaAvenue(Property):
            pass

        class PennsylvaniaAvenue(Property):
            pass

    class Blue:
        class ParkPlace(Property):
            pass

        class Boardwalk(Property):
            pass
