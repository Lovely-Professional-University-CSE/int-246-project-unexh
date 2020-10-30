import numpy as np
import pandas as pd
import random as rd
from random import randint
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def to_base64(fig):
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String

class Knapsack_Class_GA:
    maxx_val = 0
    def __init__(self,weight_list,value_list,knapsack_value,gene_count=8,gen_count=50,crossover_rate=0.8,mutation_rate=0.4):
        self.item_number = np.arange(1,len(weight_list)+1)
        self.weight = np.array(weight_list)
        self.value = np.array(value_list)
        self.knapsack_threshold = knapsack_value
        print('\nThe list is as follows:')
        print('Item No.   Weight   Value')
        for i in range(self.item_number.shape[0]):
            print('{0}          {1}         {2}\n'.format(i, self.weight[i], self.value[i]))
        self.solutions_per_pop = gene_count
        self.pop_size = (self.solutions_per_pop, self.item_number.shape[0])
        print('Population size = {}'.format(self.pop_size))
        initial_population = np.random.randint(2, size = self.pop_size)
        self.initial_population = initial_population.astype(int)
        self.num_generations = gen_count
        print('Initial population: \n{}'.format(initial_population))
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

    def cal_fitness(self):
        fitness = np.empty(self.initial_population.shape[0])
        for i in range(self.initial_population.shape[0]):
            S1 = np.sum(self.initial_population[i] * self.value)
            S2 = np.sum(self.initial_population[i] * self.weight)
            if S2 <= self.knapsack_threshold:
                fitness[i] = S1
            else :
                fitness[i] = 0 
        return fitness.astype(int)

    def selection(self,fitness, num_parents):
        fitness = list(fitness)
        parents = np.empty((num_parents, self.initial_population.shape[1]))
        for i in range(num_parents):
            max_fitness_idx = np.where(fitness == np.max(fitness))
            parents[i,:] = self.initial_population[max_fitness_idx[0][0], :]
            fitness[max_fitness_idx[0][0]] = -999999
        return parents

    def crossover(self,parents, num_offsprings):
        offsprings = np.empty((num_offsprings, parents.shape[1]))
        crossover_point = int(parents.shape[1]/2)
        i=0
        while (parents.shape[0] < num_offsprings):
            parent1_index = i%parents.shape[0]
            parent2_index = (i+1)%parents.shape[0]
            x = rd.random()
            if x > self.crossover_rate:
                continue
            parent1_index = i%parents.shape[0]
            parent2_index = (i+1)%parents.shape[0]
            offsprings[i,0:crossover_point] = parents[parent1_index,0:crossover_point]
            offsprings[i,crossover_point:] = parents[parent2_index,crossover_point:]
            i=+1
        return offsprings    

    def mutation(self,offsprings):
        mutants = np.empty((offsprings.shape))
        for i in range(mutants.shape[0]):
            random_value = rd.random()
            mutants[i,:] = offsprings[i,:]
            if random_value > self.mutation_rate:
                continue
            int_random_value = randint(0,offsprings.shape[1]-1)    
            if mutants[i,int_random_value] == 0 :
                mutants[i,int_random_value] = 1
            else :
                mutants[i,int_random_value] = 0
        return mutants   

    def optimize(self):
        parameters, fitness_history = [], []
        num_parents = int(self.pop_size[0]/2)
        num_offsprings = self.pop_size[0] - num_parents 
        for _ in range(self.num_generations):
            fitness = self.cal_fitness()
            fitness_history.append(fitness)
            parents = self.selection(fitness, num_parents)
            offsprings = self.crossover(parents, num_offsprings)
            mutants = self.mutation(offsprings)
            self.initial_population[0:parents.shape[0], :] = parents
            self.initial_population[parents.shape[0]:, :] = mutants
            
        print('Last generation: \n{}\n'.format(self.initial_population)) 
        fitness_last_gen = self.cal_fitness()      
        print('Fitness of the last generation: \n{}\n'.format(fitness_last_gen))
        max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
        parameters.append(self.initial_population[max_fitness[0][0],:])
        return (parameters, fitness_history)

    def get_solution_ga(self):
        parameters, self.fitness_history = self.optimize()
        print('The optimized parameters for the given inputs are: \n{}'.format(parameters))
        selected_items = self.item_number * parameters
        print('\nSelected items that will maximize the knapsack without breaking it:')
        for i in range(selected_items.shape[1]):
            if selected_items[0][i] != 0:
                print('{}\n'.format(selected_items[0][i]))
                
        for i in range(selected_items.shape[1]):
            if selected_items[0][i] != 0:
                self.maxx_val += self.value[i]
                
        print("maxx_val is : ",self.maxx_val)
        return self.maxx_val

    def get_graph(self):
        fitness_history_mean = [np.mean(fitness) for fitness in self.fitness_history]
        fitness_history_max = [np.max(fitness) for fitness in self.fitness_history]
        fig = plt.figure(1)
        plt.plot(list(range(self.num_generations)), fitness_history_mean, label = 'Mean Fitness')
        plt.plot(list(range(self.num_generations)), fitness_history_max, label = 'Max Fitness')
        plt.legend()
        plt.title('Fitness through the generations')
        plt.xlabel('Generations')
        plt.ylabel('Fitness')
        #plt.show()
        print(np.asarray(self.fitness_history).shape)
        return to_base64(fig)


def demo():
    session_knapsack = Knapsack_Class_GA([10,20,30],[60,100,120],50)#,8,50,0.8,0.4)
    session_knapsack.get_solution_ga()
    #session_knapsack.get_graph()
    #will not work now as its returning a base64 string

if __name__ == '__main__':
    demo()