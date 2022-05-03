'''
Requirements:

1. You need to create a simple text-based BlackJack game
2. The game needs to have one player versus an automated dealer.
3. The player can stand or hit.
4. The player must be able to pick their betting amount.
5. You need to keep track of the player's total money.
6. You need to alert the player of wins, losses, or busts, etc...

Important:
You must use OOP and classes in some portion of your game. You can not just use functions in your game. 
Use classes to help you define the Deck and the Player's hand.
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') 
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') 
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank


    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self) -> None:
        self.deck = []

        for suit in suits:
            for rank in ranks:
                createdCard = Card(suit, rank)

                self.deck.append(createdCard)
    

    def __str__(self) -> str:
        for card in self.deck:
            print(f'{card}')
        return 'All cards shown'

    def shuffle(self) -> None:
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self) -> None:
        pass
