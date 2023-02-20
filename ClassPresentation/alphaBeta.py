# All credit for this program goes to geeksforgeeks 
# Python3 program to demonstrate working of Alpha-Beta Pruning

# Initialize MAX and MIN values for alpha-beta pruning
MAX, MIN = 1000, -1000

# Returns optimal value for current player using alpha-beta pruning
# depth - current depth in the tree
# nodeIndex - index of the current node in the tree
# maximizingPlayer - boolean indicating whether the current player is maximizing or not
# values - list of values assigned to tree nodes
# alpha - best value for maximizing player found so far
# beta - best value for minimizing player found so far
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
  
    # Terminating condition - leaf node is reached
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        # Initialize best value as minimum possible value
        best = MIN
        # Recur for left and right children
        for i in range(0, 2):
             
            # Evaluate value for child node
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
 
            # Update best value for maximizing player
            best = max(best, val)
 
            # Update alpha value
            alpha = max(alpha, best)
 
            # Alpha Beta Pruning - if beta is smaller than or equal to alpha, break the loop
            if beta <= alpha:
                break

        return best
    else:
        # Initialize best value as maximum possible value
        best = MAX
 
        # Recur for left and right children
        for i in range(0, 2):
          
            # Evaluate value for child node
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
 
            # Update best value for minimizing player
            best = min(best, val)
 
            # Update beta value
            beta = min(beta, best)
 
            # Alpha Beta Pruning - if beta is smaller than or equal to alpha, break the loop
            if beta <= alpha:
                break
          
        return best
      
# Driver Code
if __name__ == "__main__":
  
    # Test values for tree nodes
    values = [3, 5, 6, 9, 1, 2, 0, -1] 

    # Print the optimal value using alpha-beta pruning
    print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))
     