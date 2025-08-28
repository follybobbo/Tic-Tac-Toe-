import math
from random import Random

#Dictionary containing the values of each position on the table.

rand = Random()
position_list = [" " for times in range(0, 9)]


#list containing the all possible positional combinations that can lead to winning the game.
solution_groups = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

#List containing all possible choices a player can make while playing the game.
available_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#list that will contain all choices player will make while playing the game.
player_1_selections = []
player_2_selections = []
player_selections_tracker = []


#Function below loops through all possible solutions combination that can be achieved while playing the game and checks
#for a hit.


def check_winner(board):
    for solution in solution_groups:
        index_1 = solution[0]
        index_2 = solution[1]
        index_3 = solution[2]
        group = {board[index_1], board[index_2], board[index_3]}

        if len(group) == 1 and " " not in group:
            for item in group:
                return item
    if " " not in board:
        return "Tie"
    else:
        return None


#Table For gameplay

def show_table():
    print(
        f"""
      {available_positions[0]} | {available_positions[1]} | {available_positions[2]}
    ---+---+---
      {available_positions[3]} | {available_positions[4]} | {available_positions[5]}
    ---+---+---
      {available_positions[6]} | {available_positions[7]} | {available_positions[8]}
    """
    )


#Recursive Function that simulates the gameplay and helps AI select its next move

def minimax(board, depth, is_maximizing):
    #Check winner
    winner_result = check_winner(board)

    #TERMINAL STATES OF THE GAME

        #Player wins
    if winner_result == "O":
        return -1
        #AI wins
    elif winner_result == "X":
        return 1
        #Draw
    elif winner_result == "Tie":
        return 0

    #Maximizes the Score of AI, Returns either -1, 1, or 0 as best score (results of terminal state block.)
    if is_maximizing:
        best_score = -math.inf
        for index, value in enumerate(board):
            if board[index] == " ":
                board[index] = "X"
                score = minimax(board, depth + 1, False)
                board[index] = " "
                best_score = max(score, best_score)

        return best_score
    #Minimizes the score of Player, Returns same as above
    else:
        best_score = math.inf
        for index, value in enumerate(board):
            if board[index] == " ":
                board[index] = "O"
                score = minimax(board, depth + 1, True)
                board[index] = " "
                best_score = min(score, best_score)

        return best_score

#Here the descision of the simulation is decided, in the score > best_score line, it is ensured that at the end of the day
#a move which leads to 1 being selected as the best_score is chosen (that is Computer wins).
def ai_move():
    best_score = -math.inf
    move = None

    for position, value in enumerate(position_list):
        if position_list[position] == " ":
            position_list[position] = "X"
            score = minimax(position_list, 0, False)
            position_list[position] = " "

            if score > best_score:
                best_score = score
                move = position + 1
    # position_dict[move] = "X"
    return move

#Easy AI difficulty, chooses available position on table at Random
def ai_easy(board_state):
    length = len(board_state)
    position_gotten = False
    while not position_gotten:
        position = rand.choice(board_state)
        if position != "X" and position != "O":
            position_gotten = True
            print(position)
            return position






#Contains Logic For gameplay.
def tic_tac_toe():
    print("Welcome tp the Tic-Tac, Player 1 is X and Player 2 is O")
    difficulty = input("Please Choose Difficulty: Easy or Hard: ").capitalize()


    #Runs the code below 9 times since there are only 9 slots in the game.
    for times in range(1, 10):
        show_table()

        #If and Else Block Assigns player one to odd no and player two to even no
        if times % 2 != 0:
            player = "Player 1"

            #Validates Player Response
            validated_response = False
            while not validated_response:
                player_position = input(f"Hello Player 1, what position do you wan to fill {available_positions}: ")
                if player_position.isdigit():
                    player_position = int(player_position)
                    if player_position in available_positions:
                        validated_response = True
                    else:
                        print("Please Input Valid Position")
                else:
                    print("please input digit not string")

            player_selection = "O"
            player_1_selections.append(player_position)
        else:
            #Put AI Function here, it returns selection of AI and position
            player = "Player 2"
            if difficulty == "Easy":
                player_position = ai_easy(available_positions)
            elif difficulty == "Hard":
                player_position = ai_move()

            # player_position = int(input(f"Hello Player 2, what position do you wan to fill {available_positions}: "))
            player_selection = "X"
            player_2_selections.append(player_position)



        # gets index of player input, and remove player selection from available input.
        index_position = player_position - 1
        position_list[index_position] = player_selection
        available_positions[index_position] = player_selection
        # print(position_list)
        win = check_winner(position_list)

        if win == "X" or win == "O":
            print(f"Player {player} wins {win}")
            show_table()
            break



tic_tac_toe()



"""TO DO: CREATE A BRANCH IN GIT CALLED AI, THEN CREATE SMART AI THAT WILL ENUMERATE THE AVAILABLE POSITION AND CHOOSE THE BEST POSITION."""











































