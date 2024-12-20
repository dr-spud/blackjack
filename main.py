import random
import time

def main():
    game = DeckOfCards()

    game.shuffle_deck()

    game.deal_cards()



    print(f"\nDealer's hand: {game.dealer_hand[0]}, Hidden")
    # print(f"Dealer's value: {game.calculate_hand_value(game.dealer_hand)}")

    if game.player_turn() == True:
        #if player didn't bust
        print("\nDealer's turn: ")
        
        game.dealer_turn()

        print(f"\nFinal results:")
        print(f"Player value: {game.calculate_hand_value(game.player_hand)}")
        print(f"Dealer value: {game.calculate_hand_value(game.dealer_hand)}")

        dealer_value = game.calculate_hand_value(game.dealer_hand)
        player_value = game.calculate_hand_value(game.player_hand)

        if dealer_value > 21:
            print("\nDealer bust! You win!")
        elif dealer_value > player_value:
            print("\nDealer is closer to 21! You lose!")
        elif player_value > dealer_value:
            print("\nYou are closer to 21! You win")
        elif player_value == dealer_value:
            print("\nIt's a draw!")





class DeckOfCards:
    SUITS = [
        'Hearts',
        'Diamonds',
        'Clubs',
        'Spades'
    ]

    RANKS = [
        'Ace',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'Jack',
        'Queen',
        'King',
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck() 
        self.dealer_hand = []
        self.player_hand = []

    def create_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.__cards.append((rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.__cards)
    
    def get_cards(self):
        return self.__cards
    
    def deal_cards(self):
        if len(self.__cards) < 4:
            return None
        
        for i in range(2):
            self.player_hand.append(self.__cards.pop())
            self.dealer_hand.append(self.__cards.pop())
        
    def calculate_hand_value(self, hand):
        value = 0
        aces = 0
        for card in hand:
            #grabbing rank for each card tuple
            rank = card[0]
            if rank in ['Jack', 'Queen', 'King']:
                value += 10
            elif rank in ["Ace"]:
                aces += 1
            else:
                value += int(rank)
        
        #to handle aces

        for i in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        return value
    
    def player_turn(self):
        while True:
            hand_value = self.calculate_hand_value(self.player_hand)

            print(f"\nYour hand: {self.player_hand}")
            print(f"Your value: {hand_value}")

            if hand_value > 21:
                print("Bust! You went over 21, Dealer wins.")
                return False

            choice = input("\nDo you want to (H)it, or (S)tand?: ").upper()

            if choice == "H":
                self.player_hand.append(self.__cards.pop())
                

            elif choice =="S":
                return True
        
            else:
                print("\nNot a valid choice!")

        
            
    def dealer_turn(self):
        hand_value = self.calculate_hand_value(self.dealer_hand)

        

        if hand_value > 16:
            return False
        
        self.dealer_hand.append(self.__cards.pop())
        print(f"\nDealer's hand: {self.dealer_hand}")
        print(f"Dealer's value: {self.calculate_hand_value(self.dealer_hand)}")

        time.sleep(1)

        self.dealer_turn()

         


if __name__ == "__main__":
    main()




