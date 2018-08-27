#!/usr/bin/env python3


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

import random
import time
import os

class Player:
    
    def __init__(self):
        self.move_list = []
        self.opponent_move_list = []
        self.rnd_no = 0

    def move(self):
        return random.choice(moves)

    def pick_three(self):
        self.choice_sequence = random.sample(moves,3)
        return self.choice_sequence
    
    def learn_move(self,my_move,opponent_move,round_number):
        self.move_list.append(my_move)
        self.opponent_move_list.append(opponent_move)
        self.rnd_no = round_number

class Rock (Player):

    def move(self):
        return "rock"

class Human (Player):

    def move(self):
        player_move = "xxx"
        while_count = 0

        while player_move not in moves:

            if while_count > 0:
                print(f"I didn't recogtnize your choice {player_move} please pick again")
                print()

            player_move = input(f'What is your move? Type "Rock", "Paper" or "Scissors": ')
            player_move = player_move.lower()
            
            if player_move in moves:
                pass
        
            else:
                for i in moves:

                    if i[0] == player_move[0]:
                        player_move=i
                        print ()
                        print (f'Since your answer began with the letter {i[0]} I am guessing that you intended to select {i}')
                        print ()

            if while_count > 3:
                 print()
                 print (f"I didn't recogtnize your choice {player_move} so I am picking for you!")
                 print()
                 time.sleep(1)
                 player_move = random.choice(moves)
            
            while_count += 1

        return player_move               

class ReflectPlayer (Player):

    def move(self):

        if self.rnd_no == 0:
            return random.choice(moves)

        else:
            return self.opponent_move_list[self.rnd_no-1]
        
class CyclePlayer (Player):

    def move(self):

        if self.rnd_no == 0:
            self.pick_three()
            return self.choice_sequence[0]

        elif self.rnd_no == 1:
            return self.choice_sequence[1]

        elif self.rnd_no == 2:
            return self.choice_sequence[2]

        else:
            return self.move_list[self.rnd_no-3]
       
class RandomPlayer (Player):
    pass

def beats(one, two):

    if ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock')):
        return 1,0

    elif (one == two):
        return 0,0

    else:
        return 0,1

class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.round_number = 0
 
    def play_round(self):
        move1 = "start"
        move2 = "start"
        move_count = 0

        while move1 == move2:

            if move_count > 0:
                time.sleep(1)
                print("It was a tie, please try again")
                print()

            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"Player 1: {move1}  Player 2: {move2}")
            print()
            move_count += 1

            if move_count > 5:
                break

        self.round_number +=1
        records = beats(move1,move2)
        self.p1.learn_move(move1,move2,self.round_number)
        self.p2.learn_move(move2,move1,self.round_number)
        return move1,move2,records[0],records[1]

    def play_game(self):
        print("Let the games begin!")
        p1_move_list = []
        p2_move_list = []
        results_list = []
        p1_record = 0
        p2_record = 0
        p1_record_list = []
        p2_record_list = []
        p1_set_wins = []
        p2_set_wins = []
        p1_total_sets = 0
        p2_total_sets = 0

        for set_num in range(int(sets)):
            p1_record = 0
            p2_record = 0

            for round in range(int(games)):
                print()
                print(f"Set {set_num+1} Round {round+1}:")
                ret_value = self.play_round()
                p1_record = p1_record + ret_value[2]
                p2_record = p2_record + ret_value[3]
                p1_record_list.append(ret_value[2])
                p2_record_list.append(ret_value[3])
                time.sleep(1)
                p1_move_list.append(ret_value[0])
                p2_move_list.append(ret_value[1])

                if ret_value[2]>ret_value[3]:
                    print("Player 1 Wins!")

                elif ret_value[3]>ret_value[2]:
                    print("Player 2 Wins!")

                else:
                    print("Oh great, a tie")

            print()

            if p1_record > p2_record:
                print(f"Player 1 Wins Set {set_num+1}! {p1_record} to {p2_record}")
                results_list.append(f"Player 1 Wins Set {set_num+1}! {p1_record} to {p2_record}")
                p1_set_wins.append(1)
                p1_total_sets += 1
                p2_set_wins.append(0)

            elif p2_record > p1_record:
                print(f"Player 1 Loses Set {set_num+1}! {p1_record} to {p2_record}")
                results_list.append(f"Player 2 Wins Set {set_num+1}! {p2_record} to {p1_record}")
                p1_set_wins.append(0)                
                p2_set_wins.append(1)
                p2_total_sets += 1

            else:
                print(f"Its a tie for Set {set_num+1}! {p1_record} to {p2_record}")
                results_list.append(f"Yuck, a tie {set_num+1}! {p1_record} to {p2_record}")
                p1_set_wins.append(0)                
                p2_set_wins.append(0)

            print()

        round_count = 0

        for set_results in range(int(sets)):
            print(f"Set Number {set_results+1}: {results_list[set_results]}")

            for game_results in range(int(games)):
                margin_adjust = 12-len(p1_move_list[round_count])
                spacing = " "*margin_adjust
                print(f"    Round {game_results+1}   {p1_move_list[round_count]}{spacing}{p2_move_list[round_count]}")
                round_count += 1
            print()

        if p1_total_sets > p2_total_sets:
            win_message = "Player 1 wins the match!"

        elif p1_total_sets < p2_total_sets:
            win_message = "Player 1 loses the match"

        else:
            win_message = "The entire match is a darn tie, I can't call anyone a loser"

        print(f"{win_message} with {p1_total_sets} sets to {p2_total_sets} sets")
        print()
        print()
        print("Game over!")

if __name__ == '__main__':
    
    player_type_list = [Rock(), ReflectPlayer(), CyclePlayer(), RandomPlayer(),Human()]
    number_of_types_list = ["1","2","3","4","5"]
    player_name_list = ["Rock player", "Reflect player", "Cycle player", "Random player", "Human player"]
    selected_player_type_list = []
    os.system('cls')
    time.sleep(1)

    for i in range(2):
        print(f"Please select a type of player for player {i+1}")
        print()
        player_type_choice = input("Pick: 1 for Rock, 2 for Reflect, 3 for Cycle, 4 for Random or 5 for Human: ")
        print()
        
        if player_type_choice in (number_of_types_list):
            choice = int(player_type_choice)-1
            print(f"Player {i+1} is a {player_name_list[choice]}")
            print()

        else:
            print("Sorry, you must pick a number between 1 and 5")
            print()
            player_type_choice = input("Pick: 1 for Rock, 2 for Reflect, 3 for Cycle, or 4 for Random or 5 for Human: ")
            print()
            
            if player_type_choice in (number_of_types_list):
                choice = int(player_type_choice)-1
                print(f"Player {i+1} is a {player_name_list[choice]}")
                print()

            else:
                print("Sorry, you must pick a number between 1 and 5,.. this is your second try so I'll pick for you") 
                print()
                player_type_choice = random.choice(number_of_types_list)
                choice = int(player_type_choice)-1
                print(f"Player {i+1} is a {player_name_list[choice]}")
                print()

        selected_player_type_list.append(player_type_list[int(player_type_choice)-1])
    
    sets = 2
    while_count = 0
    
    while int(sets) % 2 == 0:

        if while_count > 0:
            print()
            print("That number is even please try again")

        sets = input("Please enter an odd number of sets for each match: ")
        while_count += 1
        print()
    
    games = 2
    while_count = 0
    
    while int(games) % 2 == 0:

        if while_count > 0:
            print()
            print("That number is even please try again")

        games = input("Please enter an odd number of rounds in each set ")
        while_count += 1
        print()
  
    game = Game(selected_player_type_list[0], selected_player_type_list[1])
    game.play_game()
