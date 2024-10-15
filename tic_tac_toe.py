import random


def print_grid(grid):
    size = len(grid)
    for row in grid:
        print(" | ".join(row))
        if row != grid[-1]:
            print("-" * (size * 4 - 1))


def check_winner(grid, size, symbol):
    
    for i in range(size):
        if all([grid[i][j] == symbol for j in range(size)]) or all([grid[j][i] == symbol for j in range(size)]):
            return True
    
    if all([grid[i][i] == symbol for i in range(size)]) or all([grid[i][size-i-1] == symbol for i in range(size)]):
        return True
    return False


def is_full(grid):
    return all(cell in ['X', 'O'] for row in grid for cell in row)


def tic_tac_toe():
    
    size = int(input("Enter the size of the grid: "))
    
    
    grid = [[str(size * i + j + 1) for j in range(size)] for i in range(size)]
    
    print("Here is the grid:")
    print_grid(grid)
    
    
    player1 = input("Enter the name of Player 1: ")
    player2 = input("Enter the name of Player 2: ")
    players = {0: player1, 1: player2}
    symbols = {0: 'X', 1: 'O'}
    
   
    current_player = random.randint(0, 1)
    print(f"{players[current_player]} goes first!")
    
    
    while True:
        print(f"{players[current_player]}'s turn. Enter a number from the grid:")
        
        
        print_grid(grid)
        
        
        move = input(f"{players[current_player]}, choose a number: ")
        
        
        valid_move = False
        for i in range(size):
            for j in range(size):
                if grid[i][j] == move:
                    grid[i][j] = symbols[current_player]
                    valid_move = True
                    break
            if valid_move:
                break
        
        if not valid_move:
            print("Invalid move, try again!")
            continue
        
   
        if check_winner(grid, size, symbols[current_player]):
            print_grid(grid)
            print(f"Congratulations, {players[current_player]} wins!")
            break
        
        
        if is_full(grid):
            print_grid(grid)
            print("It's a draw!")
            break
        
        
        current_player = 1 - current_player


tic_tac_toe()

