'''
Author: Celine Podgornik
Date: February 25th, 2017

Description:
This program builds a dice game called Pig where two players alternate turns rolling a dice.
During their turn, the sum of the rolls is added to the players score until they decide to 
stop or they roll a 1. If the player rolls a 1, then their turn ends and they lose all the 
accumulated points from that turn. The first player who scores 50 points wins the game. 
'''

import random

def print_scores(player1, score1, player2, score2):
    '''
    This function prints the total scores for both players. 
    
    Parameters:
    player1: a string that holds the name of the first player.
    score1: an integer that holds the score of first player.
    player2: a string that holds the name of the second player.
    score2: an integer that holds the score of the second player. 
    
    Returns: None
    '''
    
    print()
    print("--- SCORES\t" + player1 + ":", str(score1) + "\t" + player2 + ":", score2, "---")
    return None
    
def check_for_winner(name, score):
    '''
    This function checks to see if a player has scored 50 points, and if so prints out who the winner is. 
    
    Parameters:
    name: a string that represents the name of the player who the function is checking to see if won. 
    score: an integer that represents the score of the player being checked by the function. 
    
    Returns: True if the players score is 50 or greater, False if the players score is less than 50. 
    '''
    
    if score >= 50:
        print("THE WINNER IS:", name + "!!!!!")
        return True
    else:
        return False
    
def roll_again(name):
    '''
    This function determines whether the player wants to roll the dice again or end their turn. 
    
    Parameters:
    name: a string that represents the name of the player whose turn it is. 
    
    Returns: True if the player wants to roll again, False if the player does not want to roll again. 
    '''
    
    while True:
        play_again = input("Roll again, " + str(name) + "? (Y/N) ")
        if play_again == "Y" or play_again == "y" or play_again == "N" or play_again == "n":
            break
        else:
            print("I don't understand: \"" + play_again + '". Please enter either "Y" or "N".')
    if play_again == "Y" or play_again == "y":
        return True
    elif play_again == "N" or play_again == "n":
        return False
       
def play_turn(name):
    '''
    This function prints out the name of the player whose turn it is and then "rolls a dice" by choosing a
    random number between 1 and 6 (inclusive) and prints out what number was "rolled". If the random number 
    is ever a 1 during the turn, the players loses all of their points for that turn and the function prints 
    out a statement saying the player rolled a pig and their turn is over. If the player does not "roll a 1" 
    then they can continue to roll the dice, and add the rolls to their total score, until they roll a 1 or 
    decide to end their turn.  
    
    Parameters:
    name: a string that represents the name of the player whose turn it is. 
    
    Returns: the number of points accumulated by the player during their turn. 
    '''
    
    print("-"*10, name + "'s turn", "-"*10)
    points = 0
    while True:
        roll = random.randint(1,6)
        print("\t<<<", name, "rolls a", roll, ">>>")
        if roll == 1:
            print("\t!!! PIG! No points earned, sorry", name, "!!!")
            points = 0
            input('(enter to continue)')
            break
        else:
            points += roll
            print("\tPoints:", points)
            if not roll_again(name):
                break
    return points
#==========================================================
def main():
    '''
    When this file is run, first the program gets a seed value from the user and passes 
    the given value to random.seed. Then two blank lines are printed followed by the title of the game.
    Next, the program asks for the names of player 1 and player 2 and prints out a message to greet the
    players. The players' scores are then initialized to 0 and printed out using the print_scores function.
    A while loop is then entered which repeats the steps:
        Call the play_turn function for player 1
        Print the players' scores by calling print_scores
        Check if player 1 won the game by calling check_for_winner
        If player 1 didn't win the game, call the play_turn function for player 2
        Print the players scores by calling print_scores
        Check whether player 2 won the game by calling check_for_winner
    When someone wins the game, the while loop is exited. 
    '''
    
    seed = int(input("Enter seed value: "))
    random.seed(seed)
    print()
    print()
    print("Pig Dice")
    player1 = input("Enter name for player 1: ")
    player2 = input("Enter name for player 2: ")
    print("\tHello", player1, "and", player2 + ", welcome to Pig Dice!")
    score1 = 0
    score2 = 0
    print_scores(player1, score1, player2, score2)
    while True:
        score1 += play_turn(player1)
        print_scores(player1, score1, player2, score2)
        if not check_for_winner (player1, score1):
            score2 += play_turn(player2)
            print_scores(player1, score1, player2, score2)
            check_for_winner(player2, score2)
        else:
            break
        if check_for_winner(player2, score2):
            break
    
if __name__ == '__main__':
    main()
