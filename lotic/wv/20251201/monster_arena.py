'''
Monster Arena
Author: Timo Roehle
Description: Funny little game
'''

import random
import sys

villains = [
    {'name': 'Kobold', 'hp': {'current': 30, 'max': 30}, 'atk': 5, 'crit': 15, 'dodge': 20, 'block': 10, 'reward': 10},
    {'name': 'Goblin', 'hp': {'current': 40, 'max': 40}, 'atk': 7, 'crit': 10, 'dodge': 20, 'block': 10, 'reward': 15},
    {'name': 'Orc', 'hp': {'current': 70, 'max': 70}, 'atk': 12, 'crit': 20, 'dodge': 20, 'block': 10, 'reward': 20},
]

class Fight_Round:
    def __init__(self, hero, villain):
        self._hero = hero
        self._villain = villain
        self._summary = {
            'hero_action': '',
            'villain_action': '',
            'hero_dead': False,
            'villain_dead': False,
        }
    def start_round(self):
        print('[1] Angreifen')
        print('[2] Wegrennen')
        valid_choice = False
        while valid_choice == False:
            user_input = input('Deine Wahl? ')
            if user_input == '1':
                valid_choice = True
                self.calc_round(user_input)
                self.info()
                return self._summary
            if user_input == '2':
                valid_choice = True
                self._summary['hero_action'] = 'run'
                return self._summary
    def calc_round(self, user_action):
        #For now Heros Action allways comes first
        if user_action == '1':
            self._summary['hero_action'] = 'attack'
            hero_attack = self._hero.attack()
            self._summary['hero_attack'] = hero_attack
            villain_defend = self._villain.defend(hero_attack)
            self._summary['villain_defend'] = villain_defend
            if self._villain.check_death():
                self._summary['villain_dead'] = True
                return self._summary
            self._summary['villain_action'] = 'attack'
            villain_attack = self._villain.attack()
            self._summary['villain_attack'] = villain_attack
            hero_defend = self._hero.defend(villain_attack)
            self._summary['hero_defend'] = hero_defend
            self._summary['hero_dead'] = self._hero.check_death()
    def info(self):
        #print(self._summary)
        if self._summary['hero_action'] == 'attack':
            print(f'{self._hero.get_name()} greift an!')
            if self._summary['villain_defend']['dodge']:
                print(f'{self._villain.get_name()} weicht dem Angriff aus.')
            if self._summary['villain_defend']['block']:
                print(f'{self._villain.get_name()} blockt den Angriff.')
            print(f'{self._villain.get_name()} erleidet {self._summary['villain_defend']['dmg']} Schaden')
        if self._summary['villain_action'] == 'attack':
            print(f'{self._villain.get_name()} greift an!')
            if self._summary['hero_defend']['dodge']:
                print(f'{self._hero.get_name()} weicht dem Angriff aus.')
            if self._summary['hero_defend']['block']:
                print(f'{self._hero.get_name()} blockt den Angriff.')
            print(f'{self._hero.get_name()} erleidet {self._summary['hero_defend']['dmg']} Schaden')
        if self._summary['villain_dead']:
            print(f'{self._villain.get_name()} geht zu Boden und kann nicht mehr weiterkämpfen')
        if self._summary['hero_dead']:
            print(f'{self._hero.get_name()} geht zu Boden und kann nicht mehr weiterkämpfen')
        print(f'{self._hero.get_name()} HP: {self._hero.get_hp_string()}')
        print(f'{self._villain.get_name()} HP: {self._villain.get_hp_string()}')


class Fight:
    def __init__(self, hero, villain):
        self._hero = hero
        self._villain = villain
        self._rounds = [] # coming soon
        self._round_counter = 0
    def start_round(self):
        fight_ended = False
        while fight_ended == False:
            round = Fight_Round(self._hero, self._villain)
            round_summary = round.start_round()
            if round_summary['hero_action'] == 'run':
                fight_ended = True
            elif round_summary['hero_dead'] or round_summary['villain_dead']:
                fight_ended = True
    def check_end_of_fight(self):
        if self._hero.check_death() or self._villain.check_death():
            return True
        return False
    def check_winner(self):
        if self._hero.check_death():
            return self._villain.get_name()
        if self._villain.check_death():
            return self._hero.get_name()
        return 'Fight is still ongoing'
    def info(self):
        print(f'Runde: {self._round_counter}: {self._hero.get_name()} {self._hero.get_hp_string()} gegen {self._villain.get_name()} {self._villain.get_hp_string()}')
    def conclusion(self):
        print(f'Winner: {self.check_winner()}')

class Arena:
    def __init__(self, hero):
        self._name = 'Monsterarena'
        self._hero = hero
        self._history = []
    def spawn_random_villain(self):
        index = random.randint(0, len(villains)-1)
        villain = Villain(
            villains[index]['name'],
            villains[index]['hp'],
            villains[index]['atk'],
            villains[index]['dodge'],
            villains[index]['block'],
        )
        return villain
    def fight_random(self):
        villain = self.spawn_random_villain()
        self.start_fight(villain)
    def start_fight(self, villain):
        fight = Fight(self._hero, villain)
        fight.info()
        fight.start_round()

class Hero:
    def __init__(self, name):
        self._name = name
        self._hp = {'current': 100, 'max': 100}
        self._atk = 10
        self._block = 10
        self._dodge = 10
    def get_name(self):
        return self._name
    def defend(self, atk):
        defend_summary = {
            'dodge': random.randint(1, 100) < self._dodge,
            'block': random.randint(1, 100) < self._block,
            'dmg': 0
        }
        if defend_summary['dodge']:
            defend_summary['dmg'] = 0
        elif defend_summary['block']:
            defend_summary['dmg'] = atk['value'] * 0.5
        else:
            defend_summary['dmg'] = atk['value']
        self.take_dmg(defend_summary['dmg'])
        return defend_summary
    def attack(self):
        attack_summary = {
            'strength': 'normal',
            'value': 0
        }
        dice = random.randint(1, 100)
        if dice > 70:
            attack_summary['strength'] = 'awsome'
            attack_summary['value'] = self.get_atk() * 2
            return attack_summary
        if dice < 30:
            attack_summary['strength'] = 'pathetic'
            attack_summary['value'] = self.get_atk() * 0.5
            return attack_summary
        attack_summary['value'] = self.get_atk()
        return attack_summary
    def get_atk(self):
        # TODO check villain defense here
        return self._atk
    def get_hp(self):
        return self._hp
    def take_dmg(self, atk):
        self._hp['current'] -= atk
    def get_hp_string(self):
        return f'{round(self._hp['current'])}/{self._hp['max']}'
    def check_death(self):
        if self._hp['current'] <= 0:
            return True
        return False
    
class Villain:
    def __init__(self, name, hp, atk, block, dodge):
        self._name = name
        self._hp = hp
        self._atk = atk
        self._block = block 
        self._dodge = dodge
    def defend(self, atk):
        defend_summary = {
            'dodge': random.randint(1, 100) < self._dodge,
            'block': random.randint(1, 100) < self._block,
            'dmg': 0
        }
        if defend_summary['dodge']:
            defend_summary['dmg'] = 0
        elif defend_summary['block']:
            defend_summary['dmg'] = atk['value'] * 0.5
        else:
            defend_summary['dmg'] = atk['value']
        self.take_dmg(defend_summary['dmg'])
        return defend_summary
    def get_name(self):
        return self._name
    def get_atk(self):
        return self._atk
    def get_hp(self):
        return self._hp
    def get_hp_string(self):
        return f'{round(self._hp['current'])}/{self._hp['max']}'
    def take_dmg(self, atk):
        self._hp['current'] -= atk
        return self._hp
    def check_death(self):
        if self._hp['current'] <= 0:
            return True
        return False
    def attack(self):
        attack_summary = {
            'strength': 'normal',
            'value': 0
        }
        dice = random.randint(1, 100)
        if dice > 70:
            attack_summary['strength'] = 'awesome'
            attack_summary['value'] = self.get_atk() * 2
            return attack_summary
        if dice < 30:
            attack_summary['strength'] = 'pathetic'
            attack_summary['value'] = self.get_atk() * 0.5 
            return attack_summary
        attack_summary['value'] = self.get_atk()
        return attack_summary

def eval_greeting_input():
    valid_choice = False
    while valid_choice == False:
        user_choice = input('Deine Wahl? ')
        if user_choice == '1':
            valid_choice = True
            user_name = read_user_name()
            start_game(user_name)
        if user_choice == '2':
            valid_choice = True
            sys.exit(0)

def read_user_name():
    print('Gib bitte deinen Namen ein, damit wir wissen, was wir auf deinen Grabstein schreiben sollen')
    player_name = input('Name: ')
    return player_name

def greeting():
    print('Willkommen zu Lotics Monster Arena')
    print('Besiege Monster, werde stärker, gewinne Preise')
    print('Bist du bereit dein Können unter Beweis zu stellen?')
    print('[1] Hey Ho Lets go!')
    print('[2] Ich hab vergessen meine braune Hose anzuziehen :(')

def start_game(name):
    hero = Hero(name)
    arena = Arena(hero)
    arena.fight_random()

greeting()
eval_greeting_input()
