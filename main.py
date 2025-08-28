
#Dictionary containing the values of each position on the table.
position_dict = {
    "pos_1": "1",
    "pos_2": "2",
    "pos_3": "3",
    "pos_4": "4",
    "pos_5": "5",
    "pos_6": "6",
    "pos_7": "7",
    "pos_8": "8",
    "pos_9": "9"
}


#Table For gameplay
table = f"""
  {position_dict.get("pos_1")} | {position_dict["pos_2"]} | {position_dict["pos_3"]}
---+---+---
  {position_dict["pos_4"]} | {position_dict["pos_5"]} | {position_dict["pos_6"]}
---+---+---
  {position_dict["pos_7"]} | {position_dict["pos_8"]} | {position_dict["pos_9"]}
"""

#list containing the all possible positional combinations that can lead to winning the game.
solution_groups = [
    ["pos_1", "pos_2", "pos_3"],
    ["pos_4", "pos_5", "pos_6"],
    ["pos_7", "pos_8", "pos_9"],
    ["pos_1", "pos_4", "pos_7"],
    ["pos_2", "pos_5", "pos_8"],
    ["pos_3", "pos_6", "pos_9"],
    ["pos_1", "pos_5", "pos_9"],
    ["pos_3", "pos_5", "pos_7"]
]

#List containing all possible choices a player can make while playing the game.
available_positions = ["pos_1", "pos_2", "pos_3", "pos_4", "pos_5", "pos_6", "pos_7", "pos_8", "pos_9"]

#list that will contain all choices player will make while playing the game.
player_1_selections = []
player_2_selections = []


#Function below loops through all possible solutions combination that can be achieved while playing the game and checks
#for a hit.
def check_winner():

    for group in solution_groups:
        #converts each list to a set, only set which has same value ['o', 'o', 'o'] or ['x', 'x', 'x'] will have content
        #{'o'} or {'x'} which satisfies the condition below.
        winner_set = set(group)
        if len(winner_set) == 1 and "" not in winner_set:
            winning_set = winner_set
            winner = True
            return_list = [winner, winning_set]
            return return_list

    winner = False
    return_list = [winner]
    return return_list


#This function updates the solution_group which by default contains possible solution positions, with the users input in
#those positions.
def update_solution_group(player_position):
    for solution in solution_groups:
        if player_position in solution:
            index = solution.index(player_position)
            solution[index] = position_dict[player_position]

#Shows the table when called.
def show_table():
    print(f"""
              {position_dict.get("pos_1")} | {position_dict["pos_2"]} | {position_dict["pos_3"]}
            ---+---+---
              {position_dict["pos_4"]} | {position_dict["pos_5"]} | {position_dict["pos_6"]}
            ---+---+---
              {position_dict["pos_7"]} | {position_dict["pos_8"]} | {position_dict["pos_9"]}
            """)



#Contains Logic For gameplay.
def tic_tac_toe():
    print("Welcome tp the Tic-Tac, Player 1 is X and Player 2 is O")

    #Runs the code below 9 times since there are only 9 slots in the game.
    for times in range(1, 10):
        show_table()

        #If and Else Block Assigns player one to odd no and player two to even no
        if times % 2 != 0:
            player = "Player 1"
            player_position = input(f"Hello Player 1, what position do you wan to fill {available_positions}: ")
            player_selection = "O"
            player_1_selections.append(player_position)
        else:
            player = "Player 2"
            player_position = input(f"Hello Player 2, what position do you wan to fill {available_positions}: ")
            player_selection = "X"
            player_2_selections.append(player_position)

        #gets index of player input, and remove player selection from available input.
        index_available_position = available_positions.index(player_position)
        available_positions.pop(index_available_position)

        #update position selected by player with the player input which is either O or X in position_dict
        position_dict.update({player_position: player_selection})
        #Updates the solutions_group with the player input so possible winning positions can be tracked.
        update_solution_group(player_position)

        #Block Below contains logic for identifying when winner has been selected or if game is a draw.

        if len(player_1_selections) >= 3 or len(player_2_selections) >= 3:
            result = check_winner()
            winner_gotten = result[0]
            if winner_gotten:
                print(f"winner {player}")
                show_table()
                break
            elif len(player_1_selections) > 4 or len(player_2_selections) > 4 and not winner_gotten:
                show_table()
                print("Draw")




"""TO DO: CREATE A BRANCH IN GIT CALLED AI, THEN CREATE SMART AI THAT WILL ENUMERATE THE AVAILABLE POSITION AND CHOOSE THE BEST POSITION."""


def minimax(board, is_maximizing):























































