import pandas as pd
import numpy as np
import statistics as stats
from matplotlib import pyplot as plt
from math import log

class DataExtraction:

    def __init__(self, number_of_csv_files, number_of_simulations):
        self.number_of_csv_files = number_of_csv_files
        self.number_of_simulations = number_of_simulations
        pass

    def get_required_data(self, path_name, prefix):

        df_solution_lengths_1 = pd.DataFrame()
        #df_number_of_solutions = pd.DataFrame()
        df_operation_types = pd.DataFrame()

     

        df_number_of_operation_types = pd.DataFrame()

        num_of_solutions = []
        #list containing a tuple for each csv file consisting of (ave number of solutions per solution set, standard deviation)

        genolve_time = []
        #list containing a tuple for each csv file consisting of (average time genolve took, standard deviation)

        percentage_true_solution_present = []

        # BOXPLOTS
        boxplot_time = []
        box_plot_num_sol =[]


        #list containing a percentage value for how often the 'true solution' was present in the set of solutions
        for i in range(1,self.number_of_csv_files+1):

            filename = path_name+prefix+'_'+str(i)+'.csv'
            column_name = prefix + '_'+str(i)

            df = pd.read_csv(filename, converters={'Operation_sequences':eval, 'Solution_sequence':eval})

            #BOXPLOTS
            boxplot_time.append(df['Genolve_time'])


            #time Genolve took
            genolve_time_mean = (stats.mean(df['Genolve_time']))
            #new_means = [log(x,10) for x in df['Genolve_time']] ##############
            #genolve_time_std = stats.stdev(new_means)
            genolve_time_std = stats.stdev(df['Genolve_time'])
            genolve_time_min = (df['Genolve_time'].min())

            genolve_time.append((genolve_time_mean,genolve_time_std))

            # Percentage time true solution was in solution set:
            num_times_true_sol_found = df['True_solution_found'].sum()

            percentage_true_solution_present.append(num_times_true_sol_found/self.number_of_simulations*100)

            operation_sequences = df['Operation_sequences']

            # Number of operations per solution
            solution_lenghts = []

            # Number of solutions
            number_of_solutions = []


            for run in operation_sequences:
                # Number of solutions
                number_of_solutions.append(len(run))

                # Number of operations per solution
                lengths = [len(solution) for solution in run]

                ave = stats.mean(lengths)
                if len(lengths) < 3:
                    solution_lenghts.append((ave, 0))
                else:
                    std = stats.stdev(lengths)
                    solution_lenghts.append((ave, std))


            #Boxplot data
            box_plot_num_sol.append(number_of_solutions)


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

            df_operation_types[column_name] = operation_sequences
            #print(df_operation_types[column_name][0])

            # The resulting dataframe contains one column per csv file for an experiment. Each row per column contains a list of integers
            # representing the number of each type of operations in the following order:
            # [inversions, transpositions, balanced translocations, unbalanced translocations, fissions ,fusions, transpositions2 (block-interchanges)
            # Thus the total number of rows will be equivalent to the number of runs.

            #df_number_of_operation_types[column_name] = operation_types_op_sequence
            # The resulting dataframe contains one column per csv file for an experiment. Each row per column contains a list of percentages
            # representing what percentage of the operations in the solution was of a certain type of rearrangement in the following order
            # [inv, trp, b_trl, u_trl, fis, fus, trp2]
            # The total number of rows will thus be equivalent ot the number of runs



        return df_solution_lengths_1, num_of_solutions, df_operation_types, genolve_time , percentage_true_solution_present, boxplot_time, box_plot_num_sol #, df_inversions, df_transpositions, df_balanced_translocations, df_unbalanced_translocations, df_fissions, df_fusions, df_transpositions2





