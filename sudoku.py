import random

def print_grid(grid):
    for row in grid:
        print(" ".join(str(x) if x != 0 else "." for x in row))

def is_valid_move(grid, row, col, num):
    
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def generate_sudoku():
    grid = [[0] * 9 for _ in range(9)]
    for _ in range(17):  
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid_move(grid, row, col, num):
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        grid[row][col] = num
    solve_sudoku(grid)
    return grid

def hide_cells(grid, difficulty):
    grid_copy = [row[:] for row in grid]
    total_cells = 81
    if difficulty == 'easy':
        cells_to_hide = int(0.25 * total_cells)
    elif difficulty == 'medium':
        cells_to_hide = int(0.60 * total_cells)
    else:  # hard
        cells_to_hide = int(0.90 * total_cells)
    
    while cells_to_hide > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if grid_copy[row][col] != 0:
            grid_copy[row][col] = 0
            cells_to_hide -= 1
    
    return grid_copy

def get_user_input(puzzle_grid):
    print("\nEnter your numbers to complete the Sudoku. Use row and column coordinates (0-8) and the number (1-9).")
    print("Enter 'done' when you finish.")

    while True:
        user_input = input("Enter row, col, number (format: row col num): ").lower()
        if user_input == "done":
            break
        try:
            row, col, num = map(int, user_input.split())
            if 0 <= row <= 8 and 0 <= col <= 8 and 1 <= num <= 9:
                if puzzle_grid[row][col] == 0:  
                    puzzle_grid[row][col] = num
                else:
                    print(f"Cell ({row}, {col}) is already filled. Try another cell.")
            else:
                print("Invalid input. Ensure row, col are between 0-8 and num is between 1-9.")
        except ValueError:
            print("Invalid input format. Please use the format 'row col num'.")
    
    return puzzle_grid

def check_solution(puzzle_grid, solved_grid):
    return puzzle_grid == solved_grid

def sudoku_game():
    grid = generate_sudoku()
    
    difficulty = input("Enter difficulty level (easy, medium, hard): ").lower()
    while difficulty not in ['easy', 'medium', 'hard']:
        difficulty = input("Invalid choice. Please enter 'easy', 'medium', or 'hard': ").lower()
    
    puzzle_grid = hide_cells(grid, difficulty)
    print("\nHere's your Sudoku puzzle:")
    print_grid(puzzle_grid)
    
    
    filled_grid = get_user_input(puzzle_grid)
    
   
    if check_solution(filled_grid, grid):
        print("\nCongratulations! You've solved the Sudoku correctly!")
    else:
        print("\nOops! Your solution is not correct. Better luck next time!")
    

sudoku_game()

