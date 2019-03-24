p1Symbol = None
p2Symbol = None

def check_valid_choice(choice, board):
    if choice != None and choice.isdigit():
        choice = int(choice)
        if isinstance(choice, int) and choice >= 1 and choice <= 9:   #checks if user choice is a valid input and a free slot
            if isinstance(board[choice], int):
                return 0
    return 1

def finished_with_draw(board):
    print("\nWelp, looks like there was no winner this time\n")           #game drawn, asks for newgame
    print("This is the final state of the board: \n")
    print("     ||    ||      ")
    print("  {}  ||  {} ||  {}  ".format(board[7], board[8], board[9]))
    print("     ||    ||      ")
    print("-------------------")
    print("-------------------")
    print("     ||    ||      ")
    print("  {}  ||  {} ||  {}  ".format(board[4], board[5], board[6]))
    print("     ||    ||      ")
    print("-------------------")
    print("-------------------")
    print("     ||    ||      ")
    print("  {}  ||  {} ||  {}  ".format(board[1], board[2], board[3]))
    print("     ||    ||      ")
    answer = None
    while answer != 'y' and answer != 'n':
        print("\nWant to play again? y/n")
        answer = input()
        if answer == 'y':
            return 0
        elif answer == 'n':
            return 1

def finished_game(winner, board):
    answer = None
    print("\nWell played!")
    print("Player 1 ", end='') if winner == p1Symbol else print("Player 2 ", end='')  #announces winner and asks if players want another game
    print("was the winner !\n\n")
    print("This is the final state of the board: \n")
    print("     ||    ||      ")
    print("  {}  ||  {} ||  {}  ".format(board[7], board[8], board[9]))
    print("     ||    ||      ")
    print("-------------------")
    print("-------------------")
    print("     ||    ||      ")
    print("  {}  ||  {} ||  {}  ".format(board[4], board[5], board[6]))
    print("     ||    ||      ")
    print("-------------------")
    print("-------------------")
    print("     ||    ||      ")
    print("  {}  ||  {} ||  {}  ".format(board[1], board[2], board[3]))
    print("     ||    ||      ")
    while answer != 'y' and answer != 'n':
        print("\nWant to play again? y/n")
        answer = input()
        if answer == 'y':
            return 0
        elif answer == 'n':
            return 1
        

def print_board_state(turnsCount, board):
    print("This is turn number {}\n".format(turnsCount))
    print("State of the board: \n")
    print("     ||    ||      ")
    print("  {}  ||  {} ||  {}  ".format(board[7], board[8], board[9]))        #prints current table
    print("     ||    ||      ")
    print("-------------------")
    print("-------------------")
    print("     ||    ||      ")
    print("  {}  ||  {} ||  {}  ".format(board[4], board[5], board[6]))
    print("     ||    ||      ")
    print("-------------------")
    print("-------------------")
    print("     ||    ||      ")
    print("  {}  ||  {} ||  {}  ".format(board[1], board[2], board[3]))
    print("     ||    ||      ")


def add_to_board(turnsCount, choice, board):
    choice = int(choice)
    board[choice] = p1Symbol if turnsCount % 2 else p2Symbol           # adds current choice from corresponding player to corresponding table slot
    return board

def check_if_winner(board):
    listhold = []
    i = 1
    while i < 10:
        listhold.append(board[i])
        i += 1
    
    i = 0
    while i < 9:                                            #check if there's a winner each turn
        if isinstance(listhold[i], int):
            i += 1
            continue
        else:
            if i >= 0 and i <= 2:                                                         #vertical top check 
                if listhold[i] == listhold[i + 3] == listhold[i + 6]:
                    return listhold[i]
            if i >= 6 and i <= 8:                                                             #vertical bottom check
                if listhold[i] == listhold[i - 3] == listhold[i - 6]:
                    return listhold[i]
            if i == 0 or i == 3 or i == 6:                                                  #horizontal right check
                if listhold[i] == listhold[i + 1] == listhold[i + 2]:
                    return listhold[i]
            if i == 2 or i == 5 or i == 8:                                                  #horizontal left check
                if listhold[i] == listhold[i - 1] == listhold[i - 2]:
                    return listhold[i]
            if i == 0:                                                                        #diagonal top right check
                if listhold[i] == listhold[i + 4] == listhold[i + 8]:
                    return listhold[i]
            if i == 2:                                                                  #diagonal top left check
                if listhold[i] == listhold[i + 2] == listhold[i + 4]:
                    return listhold[i]
            if i == 6:                                                                   #diagonal bottom right  check
                if listhold[i] == listhold[i - 2] == listhold[i - 4]:
                    return listhold[i]
            if i == 8:                                                  #horizontal right check
                if listhold[i] == listhold[i - 4] == listhold[i - 8]:
                    return listhold[i]
        i += 1


    return None

def start_board_loop():
    board = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
    winner = None                                                                            #creates the table and goes through the player's choices
    turnsCount = 1
    print("#####################################################################################")
    print("#####################################################################################")
    print("\nSTARTING A NEW GAME: ")
    while turnsCount < 10:                                                              #prints the board each turn and asks for user input depending on the turn
        print_board_state(turnsCount, board)
        print("\nIt's player\'s 1 turn, choose a slot in the board out of the remaining ones: \n") if turnsCount % 2 else print("\nIt's player\'s 2 turn, choose a slot in the board out of the remaining ones: \n")
        print("Remaining free slots: ", end='')
        for slot in board:
            if isinstance(board[slot], int):
                print(slot, end='')
                print(" ", end='')
        print("\n")
        print("Player 1 choice: ", end='') if turnsCount % 2 else print("Player 2 choice: ", end='')
        choice = None
        while choice != 'exit' and check_valid_choice(choice, board):
            if choice != None:
                print("Wrong choice, either the slot already belongs to a player, or it's not a valid choice\n")
                print("Player 1 choice: ", end='') if turnsCount % 2 else print("Player 2 choice: ", end='')
            choice = input()
        if choice == 'exit':
            return 1
        elif check_valid_choice(choice, board) == 0:
            board = add_to_board(turnsCount, choice, board)                                                   #adds valid user input to board


        winner = check_if_winner(board)
        if winner != None:
            return finished_game(winner, board)
        turnsCount += 1
    
    
    return finished_with_draw(board)


def main():
    global p1Symbol
    global p2Symbol
    print("WELCOME TO TIC-TAC-TOE!!!\n")
    while p1Symbol != 'X' and p1Symbol != '0':
        if p1Symbol != None:
            print("{} is not a valid symbol, try again:\n".format(p1Symbol))               #players choose symbol
        print("Player 1, choose your symbol. Either \"X\" or \"0\".")
        p1Symbol = input()
    p2Symbol = 'X' if p1Symbol == '0' else '0'
    print("\nAlright, so here\'s the deal, player 1 will be the \'{}\'s and player 2 will be the \'{}\'s!".format(p1Symbol, p2Symbol))
    print("You can exit the game anytime by writing \'exit\'\n")
    while start_board_loop() == 0:
        print("\nSo you wanna play again? Let me clear the screen for you!\n\n\n\n")
    print("\nIt was fun playing with you guys! Until the next time <3")

if __name__ == '__main__':
    main()
