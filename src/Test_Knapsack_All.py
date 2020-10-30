from Knapsack_GA import Knapsack_Class_GA
from Knapsack_DP import Knapsack_Class_DP

session_obj_GA = Knapsack_Class_GA([10,20,30],[60,100,120],50)
print("solution by GA : ",session_obj_GA.get_solution_ga())

session_obj_DP = Knapsack_Class_DP()
print("solution by Dp : ",session_obj_DP.knapSack(50,[10,20,30],[60,100,120],3))