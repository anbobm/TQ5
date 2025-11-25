# Wuerfelspiel. Zweiter Versuch mit Klassen

import random

class GameState():
    def __init__(
        self,
    ) -> None:
        self._rounds = []
        self._total_points = 0
    def add_round(self, round):
        self._rounds.append(round)
    def game_stats(self):
        for round in self._rounds:
            self._total_points += round.get_round_points()
        print('Game Status')
        print(f'Runden: {len(self._rounds)}')
        print(f'Gesammtpunkte: {self._total_points}')

class GameRound():
    def __init__(
        self,
        dices: list,
    ) -> None:
        self._dices = dices 
        self._dice_points = 0
        self._bonus_points = 0
        self._round_points = 0
        self.roll_dices()
    def roll_dices(self):
        for dice in self._dices:
            dice.roll()
    def three_of_a_kind(self):
        if self._dices[0].get_roll()  == self._dices[1].get_roll() and self._dices[1].get_roll() == self._dices[2].get_roll():
            return 6 
        return 0
    def two_of_a_kind(self):
        if(self._dices[0].get_roll() == self._dices[1].get_roll()):
            return 2
        if(self._dices[1].get_roll() == self._dices[2].get_roll()):
            return 2
        if(self._dices[0].get_roll() == self._dices[2].get_roll()):
            return 2
        return 0
    def check_bonus_points(self):
        bonuspoints = self.three_of_a_kind()
        if bonuspoints > 0:
            return bonuspoints
        bonuspoints = self.two_of_a_kind()
        return bonuspoints
    def calc_points(self):
        self._dice_points =  self._dices[0].get_roll() + self._dices[1].get_roll() + self._dices[2].get_roll()
        self._bonus_points = self.check_bonus_points()
        self._round_points = self._dice_points + self._bonus_points
    def get_dice_points(self):
        return self._dice_points
    def get_bonus_points(self):
        return self._bonus_points
    def get_round_points(self):
        return self._round_points
    def round_summary(self):
        print(40 * '*')
        print(f"Deine Würfe: Würfel1: {self._dices[0].get_symbol()}, Würfel2: {self._dices[1].get_symbol()}, Würfel3: {self._dices[2].get_symbol()}")
        print(f"Bonus Punkte: {self._bonus_points}")
        print(f"Punkte in dieser Runde: {self._round_points}")
        

class Dice():
    def __init__(
        self,
    ) -> None:
        self._side_symbols = [
            '⚀', 
            '⚁',
            '⚂',
            '⚃',
            '⚄',
            '⚅',
        ]
        _roll = 0
    def roll(self):
        self._roll = random.randint(1, 6)
        return self._roll
    def get_symbol(self):
        if(self._roll == 0):
           return '❌'
        return self._side_symbols[self._roll-1]
    def get_roll(self):
        return self._roll

def start_round():
    dices = []
    for i in range(0, 3):
        dice = Dice()
        dices.append(dice)

    game_round = GameRound(dices)
    game_round.calc_points()
    game_round.round_summary()
    return game_round

game_state = GameState()

def read_user_input():
    user_input = input('Wuerfeln (y)')
    if user_input == 'y':
        game_round = start_round()
        game_state.add_round(game_round)
        game_state.game_stats()
        read_user_input()

read_user_input()
