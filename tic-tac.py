# from asyncore import loop
# from dataclasses import replace

# map = " 1 | 2 | 3 \n ---------\n 4 | 5 | 6 \n ---------\n 7 | 8 | 9 "
# map_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# map_list = 0
# player_piece = 0
# def check_move():
#     user_move = int(input("Enter the number for your next move: "))
#     if user_move in map_numbers:
#         map_numbers.remove(user_move)
#         odd_even = player_piece % 2
#         if odd_even != 0:
#             map_list.replace(user_move, "X")
#         elif odd_even == 0:
#             map_list.replace(user_move, "O")
#         print(map)
#     else:
#         print("That is not a valid move, try again!")
#         return

# while map_numbers != []:
#     check_move()
#     if map_numbers == []:
#         print("Game over, try again!")
#         break
def main():
    player = second_player("")
    board = create_board()
    while not (winner(board) or is_draw(board)):
        make_board(board)
        make_move(player, board)
        player = second_player(player)
    make_board(board)
    print("Thanks for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def make_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-----')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-----')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def is_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player} choose a square (1-9): "))
    board[square - 1] = player

def second_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()