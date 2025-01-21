
from common import List, dataclass
from random import shuffle
from board import Board

@dataclass
class Card:
    description: str
    money: int = 0
    move: int = 0
    advance_to_go: bool = False
    get_out_of_jail: bool = False


@dataclass
class Cards:
    cards: List[Card]
    disposed_cards: List[Card]

    def _shuffle(self) -> None:
        shuffle(self.disposed_cards)
        self.cards = self.disposed_cards
        self.disposed_cards.clear()

    def pull_card(self) -> Card:
        if len(self.cards) > 0:
            card = self.cards.pop(0)
            print(card.description)
            return card
        else:
            self._shuffle()
            return self.pull_card()


@dataclass
class CommunityChestCards(Cards):
    cards = [Card('Advance to Go (Collect $200)', advance_to_go=True),
             Card('Bank error in your favor. Collect $200', money=200),
             Card('Doctor’s fee. Pay $50', money=-50),
             Card('From sale of stock you get $50', money=50),
             Card('Get Out of Jail Free', get_out_of_jail=True),
             Card('Go to Jail. Go directly to jail, do not pass Go, do not collect $200'),
             Card('Holiday fund matures. Receive $100', money=100),
             Card('Income tax refund. Collect $20', money=20),
             Card('It is your birthday. Collect $10 from every player'),
             Card('Life insurance matures. Collect $100', money=100),
             Card('Pay hospital fees of $100', money=-100),
             Card('Pay school fees of $50', money=-50),
             Card('Receive $25 consultancy fee', money=25),
             Card('You are assessed for street repair. $40 per house. $115 per hotel'),
             Card('You have won second prize in a beauty contest. Collect $10', money=10),
             Card('You inherit $100', money=100)]


class ChanceCards(Cards):
    cards = [Card('Advance to Boardwalk'),
             Card('Advance to Go (Collect $200)', advance_to_go=True),
             Card('Advance to Illinois Avenue. If you pass Go, collect $200'),
             Card('Advance to St. Charles Place. If you pass Go, collect $200'),
             Card(
                 'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled'),
             Card(
                 'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled'),
             Card(
                 'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.'),
             Card('Bank pays you dividend of $50'),
             Card('Get Out of Jail Free', get_out_of_jail=True),
             Card('Go Back 3 Spaces', move=-3),
             Card('Go to Jail. Go directly to Jail, do not pass Go, do not collect $200', 0),
             Card(
                 'Make general repairs on all your property. For each house pay $25. For each hotel pay $100'),
             Card('Speeding fine $15'),
             Card('Take a trip to Reading Railroad. If you pass Go, collect $200'),
             Card('You have been elected Chairman of the Board. Pay each player $50'),
             Card('Your building loan matures. Collect $150')]
