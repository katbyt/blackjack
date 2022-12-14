import random


class BlackJack:
    deck_of_cards = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
                     'валет': 10, 'дама': 10, 'король': 10, 'туз': 11}

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer

    def game(self, balance):
        self.player_result = sum([BlackJack.deck_of_cards[i] for i in self.player.hand])
        if self.player_result == 21:
            self.player.result()
        if self.player_result > 21:
            if 'туз' in player.hand:
                self.player_result -= 10
                if self.player_result > 21:
                    print('Перебор!')
                    self.player.result()
            else:
                print('Перебор!')
                bj.result()
        else:
            print('\nУ Вас на руках карты:', player.hand)
            print('Выберите действие: 1 - взять еще одну карту; 2 - остановиться.')
            action = input('Сделайте свой выбор: ')
            if action == '1':
                balance -= {player.give_card()}
                bj.game(balance)
            elif action == '2':
                bj.result()
            else:
                print('Нет такой команды.')
                bj.game(balance)

    def result(self):
        self.dealer_result = sum([BlackJack.deck_of_cards[i] for i in self.dealer.hand])
        if self.player_result > 21 and 'туз' in player.hand:
            self.player_result -= 10
        print(f'\nКарты игрока: {player.hand}, сумма значений: {self.player_result}')
        print(f'Карты дилера: {dealer.hand}, сумма значений: {self.dealer_result}')
        if self.player_result > 21 or self.dealer_result > self.player_result:
            print('Увы, Вы проиграли.')
        elif self.player_result == self.dealer_result:
            print('При своих.')
        else:
            print('Поздравляем! Вы выиграли!')


class Players:

    def __init__(self, hand):
        self.hand = hand

    def give_card(self):
        card = random.choice(list(balance_cards))
        self.hand.append(card)
        return card


player = Players([])
dealer = Players([])
bj = BlackJack(player, dealer)
balance_cards = set(BlackJack.deck_of_cards)

for _ in range(2):
    balance_cards -= {player.give_card()}
    balance_cards -= {dealer.give_card()}

bj.game(balance_cards)

print('\nОставшиеся карты:', balance_cards)
