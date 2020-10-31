class Knapsack_Class_DP:
    def knapSack(self, knapsack_threshold, weight, value, count):
        K = [[0 for x in range(knapsack_threshold + 1)] for x in range(count + 1)]
        for i in range(count + 1):
            for w in range(knapsack_threshold + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif weight[i-1] <= w:
                    K[i][w] = max(value[i-1]
                                + K[i-1][w-weight[i-1]],  K[i-1][w])
                else:
                    K[i][w] = K[i-1][w]
        return K[count][knapsack_threshold]


if __name__ == '__main__':
    value = [60, 100, 120]
    weight = [10, 20, 30]
    knapsack_threshold = 50
    count = len(value)
    session_knapsack = Knapsack_Class_DP()
    print(session_knapsack.knapSack(knapsack_threshold, weight, value, count))