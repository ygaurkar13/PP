import random

def display(grid,size):
    print("--"*size+"-") 
    for row in grid:
        st="|{}"*size+'|'
        print(st.format(*row),sep="")
        print("--"*size+"-")
        



def initialize():
	print("welcome to sudoku game")
	grid_size =int(input("Enter the size of the game-->"))
	level=int(input("Give the level you want 1/2/3 :\n1-easy\n2-medium\n3-hard-->"))
	game_state=[list(" "*grid_size) for _ in range(grid_size)]
	for i in range(grid_size):
	 game_state[i][i]=i+1
	game_state=fill_sudoku(grid_size)
	game_state=hide_space(game_state,level)
	game_state=start_game(game_state,grid_size)
	
def fill_sudoku(grid_size):
        possible={i for i in range(1,grid_size+1)}
        game_state=[list(" "*grid_size) for _ in range(grid_size)]
        for row in range(grid_size):
                for col in range(grid_size):
                        available=set(game_state[row]+ [tr[col] for tr in game_state])
                        c=list(possible-available)
                        if c:
                                game_state[row][col]=c.pop(random.randint(0,len(c)-1))
                        else:
                             return fill_sudoku(grid_size)    
        return game_state            


def hide_space(game_state,level):
        
        grid_size = len(game_state)
        cells_to_hide = {1: grid_size, 2: grid_size+grid_size, 3: grid_size*(grid_size-1)}  
        cells_to_hide_count = cells_to_hide.get(level, grid_size)
    
        for _ in range(cells_to_hide_count):
                row, col = random.randint(0, grid_size-1), random.randint(0, grid_size-1)
                while game_state[row][col] == "X":
                        row, col = random.randint(0, grid_size-1), random.randint(0, grid_size-1)
                game_state[row][col] = "X"
        return game_state

def start_game(game_state,grid_size):
        print("you can start the game:")
        while True:
                display(game_state,grid_size)
                row,col,value=int(input(f"enter the row from 0-{grid_size-1}")),int(input(f"enter the col from 0-{grid_size-1}")),int(input(f"enter the value you want to put from 1-{grid_size}"))
                if game_state[row][col] == "X":
                         if 1 <= value <= grid_size and not violates_sudoku_rules(game_state, row, col, value):
                                  game_state[row][col] = value
                         else:
                                  print("Incorrect value! It violates Sudoku rules.")
                else:
                        print("This cell is already filled. Please choose a different cell.")
        
                if check_complete(game_state):
                        end_game()
                        break
        
def violates_sudoku_rules(game_state, row, col, value):
    grid_size = len(game_state)
    
    if value in game_state[row]:
        return True
    
    for r in range(grid_size):
        if game_state[r][col] == value:
            return True
    
    sub_grid_size = int(grid_size ** 0.5)
    start_row, start_col = (row // sub_grid_size) * sub_grid_size, (col // sub_grid_size) * sub_grid_size
    
    for r in range(start_row, start_row + sub_grid_size):
        for c in range(start_col, start_col + sub_grid_size):
            if game_state[r][c] == value:
                return True
    
    return False

def check_complete(game_state):
    grid_size = len(game_state)
    
    for i in range(grid_size):
        row_set = set(game_state[i])
        col_set = set([game_state[r][i] for r in range(grid_size)])
        
        if len(row_set) != grid_size or "X" in row_set:
            return False  
        if len(col_set) != grid_size or "X" in col_set:
            return False  
    return True        
	             	
def end_game():
         print("Congratulations! You've successfully completed the Sudoku.")	       
         

def sudoku():
	initialize()
	
sudoku()





