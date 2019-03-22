from colorama import init

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
whose_turn = 1
game_is_running = True
mark = 0
moves = 0

def show_board():
    print("\t\t\t__________________")
    print("\t\t\t|  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "  |")
    print("\t\t\t------------------")
    print("\t\t\t|  " + board[3] + "  |  " + board[4] + "  |  " + board[5] + "  |")
    print("\t\t\t------------------")
    print("\t\t\t|  " + board[6] + "  |  " + board[7] + "  |  " + board[8] + "  |")
    print("\t\t\t------------------")

def display_game_menu():
    print("What do you want to do?")
    print("1. Play Game")
    print("2. Quit")
    opt = int(input("Enter your choice: "))
    if(opt == 1):
        show_board()
    elif(opt == 2):
        exit()
    else:
        print("\nWrong choice :( \n\n")
        display_game_menu()
    
def check_empty_cell(mark):
    if(board[mark-1] == " "):
        return True
    return False

def check_who_is_winning(moves, whose_turn):
    global game_is_running
    if(moves >= 5):
        if(board[0] == board[1] == board[2]) and (board[0] != " "):
            return whose_turn
        elif(board[3] == board[4] == board[5]) and (board[3] != " "):
            return whose_turn
        elif(board[6] == board[7] == board[8]) and (board[6] != " "):
            return whose_turn
        elif(board[0] == board[3] == board[6]) and (board[0] != " "):
            return whose_turn
        elif(board[1] == board[4] == board[7]) and (board[1] != " "):
            return whose_turn
        elif(board[2] == board[5] == board[8]) and (board[2] != " "):
            return whose_turn
        elif(board[0] == board[4] == board[8]) and (board[0] != " "):
            return whose_turn
        elif(board[2] == board[4] == board[6]) and (board[2] != " "):
            return whose_turn
        elif(board[0] != " " and board[1] != " " and board[2] != " " and 
             board[3] != " " and board[4] != " " and board[5] != " " and 
             board[6] != " " and board[7] != " " and board[8] != " "):
            game_is_running = False
            return print("Match Drawn. Nobody wins or loses.")

def main():
    init()
    global board, moves, whose_turn, game_is_running, mark
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    whose_turn = 1
    game_is_running = True
    mark = 0
    moves = 0
    
    print("\033[92m" + "TIC TAC TOE on console, not PS console)\n" + "\033[0m")
    display_game_menu()
    print("Name your players:")
    player1 = input("Player 1's [X] name: ")
    player2 = input("Player 2's [O] name: ")

    print("\033[92m" + "\nSo it is " + str(player1) + " vs " + str(player2) + "\033[0m")
    print("Let's kickoff :)")

    while(game_is_running):
        if(whose_turn == 1):
            print("It is Player 1: " + "\033[92m" + str(player1) + "'s turn" + "\033[0m")
        else:
            print("It is Player 2: " + "\033[92m" + str(player2) + "'s turn" + "\033[0m") 
        #while(mark <= 0 and mark >9):
        mark = int(input("Enter a number between 1 to 9 for putting a mark in that position:"))

        if(whose_turn == 1):
            while(check_empty_cell(mark) == False):
                print("\033[31m" + "Cell " + str(mark) + " is already filled up. Please give the empty cell no." + "\033[0m")
                mark = int(input("Enter a number between 1 to 9 for putting a mark in that position:"))
            
            board[mark-1] = "X"
            print("Player 1: " + str(player1) + " put 'X' at cell " + str(mark))
            moves = moves + 1
            if(check_who_is_winning(moves, whose_turn) == 1):
                print("\033[92m" + "Player 1: " + player1 + " has won." + "\033[0m")
                game_is_running = False
            whose_turn = 2

        else:
            while(check_empty_cell(mark) == False):
                print("\033[31m" + "Cell " + str(mark) + " is already filled up. Please give the empty cell no." + "\033[0m")
                mark = int(input("Enter a number between 1 to 9 for putting a mark in that position:"))
            
            board[mark-1] = "O"
            print("Player 2: " + str(player2) + " put 'O' at cell " + str(mark)) 
            moves = moves + 1
            if(check_who_is_winning(moves, whose_turn) == 2):
                print("\033[92m" + "Player 2: " + player2 + " has won." + "\033[0m")
                game_is_running = False
            whose_turn = 1
        
        show_board()
    print("\033[92m" + "Nice game. Let's have another round.\n\n" + "\033[0m")
    main()

if __name__ == "__main__":
    main()
        
    
    

