import pandas as pd
import numpy as np
import statistics as stats
from matplotlib import pyplot as plt

number_of_simulations = 1000

class DataExtraction:

    def __init__(self):
        pass

    def get_required_data(self, path_name, prefix):

        df_solution_lengths_1 = pd.DataFrame()
        #df_number_of_solutions = pd.DataFrame()
        df_operation_types = pd.DataFrame()

        num_of_solutions = []
        #list containing a tuple for each csv file consisting of (ave number of solutions per solution set, standard deviation)

        genolve_time = []
        #list containing a tuple for each csv file consisting of (average time genolve took, standard deviation)

        percentage_true_solution_present = []
        #list containing a percentage value for how often the 'true solution' was present in the set of solutions
        for i in range(1,6):

            filename = path_name+prefix+'_'+str(i)+'.csv'
            column_name = prefix + '_'+str(i)

            df = pd.read_csv(filename, converters={'Operation_sequences':eval, 'Solution_sequence':eval})

            #time Genolve took
            genolve_time_mean = (df['Genolve_time'].mean())
            genolve_time_std = (df['Genolve_time'].std())
            genolve_time.append((genolve_time_mean,genolve_time_std))

            # Percentage time true solution was in solution set:
            num_times_true_sol_found = df['True_solution_found'].sum()

            percentage_true_solution_present.append(num_times_true_sol_found/number_of_simulations*100)

            operation_sequences = df['Operation_sequences']
            for i in range(0,10):
                print(i, ":  ",operation_sequences[i])
                print()

            # Number of operations per solution
            solution_lenghts = []

            # Number of solutions
            number_of_solutions = []

            #Operation types
            operation_types =[]
            #operation_tytpe = [num_inv, num_trp, num_b_trl, num_u_trl, num_fis, num_fus, num_trp2]

            for run in operation_sequences:

                # Number of operations per solution
                lengths = [len(solution) for solution in run]

                ave = stats.mean(lengths)
                if len(lengths) < 3:
                    solution_lenghts.append((ave, 0))
                else:
                    std = stats.stdev(lengths)
                    solution_lenghts.append((ave, std))

                # Number of solutions
                number_of_solutions.append(len(run))

                # Operation types
                for solution in run:
                    sol_operation_types = [solution.count(0),solution.count(1) ,solution.count(2),solution.count(3), solution.count(4),solution.count(5),solution.count(6)]
                operation_types.append(sol_operation_types)




            num_sol_ave = stats.mean(number_of_solutions)
            num_sol_std = stats.stdev(number_of_solutions)

            num_of_solutions.append((num_sol_ave, num_sol_std))

            df_solution_lengths_1[column_name] = solution_lenghts
            #The resulting dataframe contains one column per csv file for an experiment. Each row per column contains a tuple of
            #the (average, standard deviation) of the number of operations in a solution for a single run. Thus the total number of
            #rows will be equivalent to the number of runs. If there were less than three solutions, the standard deviation cannot
            #be calculated and the tuple is (average, False).
            #With the one-to-one weighting scheme there will only be variance between solution lengths for a single run if some of the
            #solutions used block-interchange operations and others did not.


           # df_number_of_solutions[column_name] = number_of_solutions
            # The resulting dataframe contains one column per csv file for an experiment. Each row per column contains an integer - the
            # number of solutions for a single run. Thus the total number of rows will be equivalent to the number of runs.

            df_operation_types[column_name] = operation_types
            # The resulting dataframe contains one column per csv file for an experiment. Each row per column contains a list of integers
            # representing the number of each type of operations in the following order:
            # [inversions, transpositions, balanced translocations, unbalanced translocations, fissions ,fusions, transpositions2 (block-interchanges)
            # Thus the total number of rows will be equivalent to the number of runs.

        return df_solution_lengths_1, num_of_solutions, df_operation_types, genolve_time , percentage_true_solution_present




