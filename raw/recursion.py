import time

# Check if there's a queen in the same column
def is_safe(board, row, col, n):
    # Loop thru each row
    for i in range(row):
        # If a queen is in the same column
        # board[i] represents as the column in the row being looped
        if (board[i] == col or 
            # If both are -1, then there is a queen (diagonally)
            board[i] - i == col - row or # Checks left-to-right
            # If both are the same value, then there is a queen
            board[i] + i == col + row): # Checks right-to-left
            return False
    # If it doesn't pass the conditions, then we can place the queen
    return True

def solve_n_queens(board, row, n, solutions):
    # If the row is now equal to the n (the size of board), we add the solution
    if row == n:
        # Save the current state of board so it won't be modified in backtracking
        solutions.append(board[:])
        return
    
    # Try placing queens in all columns for the current row
    for col in range(n):
        # For each column, we'll check if it's safe to place the queen
        if is_safe(board, row, col, n):
            board[row] = col  # Place the queen
            solve_n_queens(board, row + 1, n, solutions)  # Recur for the next row
            board[row] = -1  # Backtrack, remove the queen

def print_solution(board):
    # Loop thru each row, checking if we place the queen or not
    # Row in here represents the position of each queen in each row
    # Not technically the row in what'd you think in a 2d array
    # So it's a single-dimension array 
    for row in board:
        # Check each column in the board (the queens' positions)
        # If there is a queen print Q if not then print a dot
        # We use len(board) instead of explicitly passing n for adaptability
        # If there ever is a case that n wasn't passed around correctly
        # Or if the recursion modified the board
        line = ['Q' if col == row else '.' for col in range(len(board))]
        print(" ".join(line))
    print("-" * len(board) * 2)

# Initializer method
def n_queens(n):    
    solutions = [] # Initialize array of solutions
    board = [-1] * n  # Initialize the board with -1 (no queens placed)
    
    solve_n_queens(board, 0, n, solutions) # Base
    
    # After the many many recursions, we then (only) print all the valid solutions
    print(f"Found {len(solutions)} solutions for {n}-Queens:")
    for solution in solutions:
        print_solution(solution)

# The size of the board
n = 6

start_time = time.perf_counter()
n_queens(n)
end_time = time.perf_counter()

print(f"Completed in {end_time - start_time:.6f} seconds")