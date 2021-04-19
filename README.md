# Sudoku-Solver

Simple sudoku solver, will take a 2-D array as input and output a solution, if it exists. This is done using a
backtracking algorithm where it will check for each valid input in each of the unfilled spaces, all currently
valid entries, if it reaches a number with no possible solutions, it will backtrack, deleting the last number added
and increment that number