# Problem Statement
## 0-1 Knapsack problem
#### We have given a set of items, each with a weight (Wi) and a value (Vi), determine the number of each item included in a collection so that the total weight is less than or equal to a given limit of knapsack and the total value is as large as possible.
&nbsp;
# Possible Approaches to Solve the Problem
We can solve the 0-1 Knapsack problem with the help of given methods:
1. Genetic Algorithm (GA)
2. Dynamic Programming (DP)

## Genetic Algorithm (GA)
source file: src/Knapsack_GA.py
In this approach, we have to perform various steps to generate a good solution for the problem. The steps are:
### 1. Create Initial Population
The initial population is random such that we do not have any bias in the population. The initial populations’ genes have allele values 0 and 1. 0 represents that the item is not selected, while 1 represents a selection of that item. The population size is determined by the number of items we have. We have several possible solutions initially, we minimize and randomize those solutions and thus our initial population is created.
In the source file, the function '__init__' is defined to create initial population based on given weights and values.

### 2. Measure Fitness of the Population
This step involves measuring of fitness of the population we have. This step is essential for the selection process (step 3).
In the source file, the function 'cal_fitness' is defined to calculate the fitness of the population.
The formula to measure the fitness is: 

![Fitness Function](https://miro.medium.com/max/465/1*fenR6vIzGliZ6IfnR83stw.gif)

### 3. Select Proper Population (parents) for Creation of Next Population
Here we select the fittest individuals so that they can undergo crossover. We select the parents based on their fitness. The required fittest population is selected as parents.
In the source file, the function 'selection' is defined to create initial population based on given weights and values.

### 4. Perform Crossover between Selected Population (parents)
In a crossover, we combine 2 parents and generate the new population (offspring). We perform a one-point crossover between 2 parents. Here we decide a common point for both individuals and their offsprings about which for the first offspring, we take all left genes of first parent and all right genes of the second parent and vice-versa for the second offspring.
In the source file, the function 'crossover' is defined to create initial population based on given weights and values.

### 5. Perform Mutation in Created Population
We perform mutation to diversify the population. In mutation, we flip (toggle) the allele of the gene. If the allele is 0, after mutation it becomes 1 and vice-versa.
In the source file, the function 'mutation' is defined to create initial population based on given weights and values.

#### We repeat these steps until our solution constraints are reached.
&nbsp;

## Dynamic Programming (DP)
In this approach, we consider all the possible weights from 1 to W (knapsack capacity) as the columns and given weights of items as the rows. If we consider ‘wi’ (weight in ‘ith’ row) we can fill it in all columns which have ‘weight values > wi’. Now two possibilities can take place:
#### 1. Fill ‘wi’ in the given column.
#### 2. Do not fill ‘wi’ in the given column.
Now we have to take a maximum of these two possibilities, formally if we do not fill ‘ith’ weight in ‘jth’ column then DP[i][j] state will be same as DP[i-1][j] but if we fill the weight, DP[i][j] will be equal to the value of ‘wi’+ value of the column weighing ‘j-wi’ in the previous row. So we take the maximum of these two possibilities to fill the current state.
After performing all the operations, the value of the last row and the last column will be our required answer.
&nbsp;
