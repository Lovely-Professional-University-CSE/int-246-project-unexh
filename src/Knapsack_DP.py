# A naive recursive implementation 
# of 0-1 Knapsack Problem 

# Returns the maximum value that 
# can be put in a knapsack of 
# capacity knapsack_threshold 

class Knapsack_Class_DP:
    def knapSack(self,knapsack_threshold, weight, value, count):
        if count == 0 or knapsack_threshold == 0 : 
            return 0
        if (weight[count-1] > knapsack_threshold): 
            return self.knapSack(knapsack_threshold, weight, value, count-1) 
        else: 
            return max(value[count-1] + self.knapSack( 
                        knapsack_threshold-weight[count-1], weight, value, count-1), 
                        self.knapSack(knapsack_threshold, weight, value, count-1)) 

if __name__ == '__main__':
    value = [60, 100, 120]
    weight = [10, 20, 30] 
    knapsack_threshold = 50
    count = len(value)
    session_knapsack = Knapsack_Class_DP()
    print(session_knapsack.knapSack(knapsack_threshold,weight,value,count))
