#importing numpy library as npy
import numpy as npy

#creating row of 8 and column of 8 with zeros
Chessboard = npy.zeros((8, 8), dtype=int)

# printing the chessboard
print(Chessboard)

# requesting user input
User_solution = input("Do you want an open solution or closed solution? (Enter 'Open' or 'Closed'): ")

# printing user input
print("You have selected " + User_solution + " solution.")

# requesting user input
User_approach = input("Which approach do you want to use? (Enter 'Backtracking' or 'Las Vegas': ")

# printing user input
print("You have selected " + User_approach + " approach.")

# if statement for user selecting an approach
if User_approach == 'Las Vegas':
    print("Las Vegas approach (makes the move randomly): the end conditions are that the tour is completed (successful) or the knight steps in an already-visited square (unsuccessful).")
else:
    print("Backtracking approach: when it reaches a dead end, it undoes the moves and tries a different path.")
