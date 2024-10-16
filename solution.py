def solve_n_queens(n):
    def is_safe(queens, row, col):
        # Check if the current queen placement is safe
        for r, c in enumerate(queens):
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def solve(queens, row):
        if row == n:
            # If all queens are placed, add the solution to the results
            result.append(queens)
            return
        
        for col in range(n):
            if is_safe(queens, row, col):
                # Try placing a queen at (row, col)
                solve(queens + [col], row + 1)

    result = []
    solve([], 0)
    
    # Generate the board configurations
    def generate_board(queens):
        board = []
        for queen in queens:
            row = ['.'] * n
            row[queen] = 'Q'
            board.append(''.join(row))
        return board
    
    return [generate_board(queens) for queens in result]

# Test case
n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()
