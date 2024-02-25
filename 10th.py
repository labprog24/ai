def is_safe(board, row, col, n):
    return all(board[i][col] == 0 for i in range(row)) and \
           all(board[i][j] == 0 for i, j in zip(range(row, -1, -1), range(col, -1, -1))) and \
           all(board[i][j] == 0 for i, j in zip(range(row, -1, -1), range(col, n)))

def solve_n_queens(n):
    def solve(board, row):
        if row == n:
            solutions.append([''.join('Q' if cell == 1 else '.' for cell in row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    solutions = []
    solve([[0] * n for _ in range(n)], 0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        print('\n'.join(solution))
        print()

if __name__ == "__main__":
    n = 5
    solutions = solve_n_queens(n)
    print(f'solutions for {n} Queens: ')
    print_solutions(solutions)
