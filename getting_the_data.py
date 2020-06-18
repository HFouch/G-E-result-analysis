import pandas as pd
import numpy as np
import statistics as stats
from matplotlib import pyplot as plt


class DataExtraction:

    def __init__(self, number_of_csv_files, number_of_simulations):
        self.number_of_csv_files = number_of_csv_files
        self.number_of_simulations = number_of_simulations
        pass

    def get_required_data(self, path_name, prefix):

        df_solution_lengths_1 = pd.DataFrame()
        #df_number_of_solutions = pd.DataFrame()
        df_operation_types = pd.DataFrame()

        df_inversions = pd.DataFrame()
        df_transpositions = pd.DataFrame()
        df_balanced_translocations = pd.DataFrame()
        df_unbalanced_translocations = pd.DataFrame()
        df_fissions = pd.DataFrame()
        df_fusions = pd.DataFrame()
        df_transpositions2 = pd.DataFrame()


        df_number_of_operation_types = pd.DataFrame()

        num_of_solutions = []
        #list containing a tuple for each csv file consisting of (ave number of solutions per solution set, standard deviation)

        genolve_time = []
        #list containing a tuple for each csv file consisting of (average time genolve took, standard deviation)

        percentage_true_solution_present = []
        #list containing a percentage value for how often the 'true solution' was present in the set of solutions
        for i in range(1,self.number_of_csv_files+1):

            filename = path_name+prefix+'_'+str(i)+'.csv'
            column_name = prefix + '_'+str(i)

            df = pd.read_csv(filename, converters={'Operation_sequences':eval, 'Solution_sequence':eval})

            #time Genolve took
            genolve_time_mean = (df['Genolve_time'].mean())
            genolve_time_std = (df['Genolve_time'].std())
            genolve_time.append((genolve_time_mean,genolve_time_std))

            # Percentage time true solution was in solution set:
            num_times_true_sol_found = df['True_solution_found'].sum()

            percentage_true_solution_present.append(num_times_true_sol_found/self.number_of_simulations*100)

            operation_sequences = df['Operation_sequences']

            # Number of operations per solution
            solution_lenghts = []

            # Number of solutions
            number_of_solutions = []

            #Operation types
            #operation_types_op_sequence =[]
            #operation_tytpe = [num_inv, num_trp, num_b_trl, num_u_trl, num_fis, num_fus, num_trp2]

            inversions =[]
            transpositions = []
            balanced_translocations = []
            unbalanced_transloctions = []
            fissions = []
            fusions =[]
            transpositions2 = []
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
                operation_types_solution_set =[]
                for solution in run:
                    sol_length = len(solution)
                    sol_operation_types = [(solution.count(0)/sol_length)*100,(solution.count(1)/sol_length)*100 ,(solution.count(2)/sol_length)*100,(solution.count(3)/sol_length)*100, (solution.count(4)/sol_length)*100,(solution.count(5)/sol_length)*100,((solution.count(6.1)+solution.count(6.2))/sol_length)*100]
                    operation_types_solution_set.append((sol_operation_types))

                #op_type_stats_solution_set = []
                inv_percentages=[]
                trp_percentages=[]
                b_trl_percentages=[]
                u_trl_percentages=[]
                fis_percentages=[]
                fus_percentages=[]
                trp2_percentages=[]
                for op_type_percentages in operation_types_solution_set:
                    inv_percentages.append(op_type_percentages[0])
                    trp_percentages.append(op_type_percentages[1])
                    b_trl_percentages.append(op_type_percentages[2])
                    u_trl_percentages.append(op_type_percentages[3])
                    fis_percentages.append(op_type_percentages[4])
                    fus_percentages.append(op_type_percentages[5])
                    trp2_percentages.append(op_type_percentages[6])

                inv_percentages_mean = stats.mean(inv_percentages)
                if len(inv_percentages) < 3:
                    inv_percentages_std = 0
                else:
                    inv_percentages_std = stats.stdev(inv_percentages)
                #op_type_stats_solution_set.append((inv_percentages_mean, inv_percentages_std))
                inversions.append((inv_percentages_mean, inv_percentages_std))


                trp_percentages_mean = stats.mean(trp_percentages)
                if len(trp_percentages) < 3:
                    trp_percentages_std = 0
                else:
                    trp_percentages_std = stats.stdev(trp_percentages)
                #op_type_stats_solution_set.append((trp_percentages_mean, trp_percentages_std))
                transpositions.append((inv_percentages_mean,inv_percentages_std))

                b_trl_percentages_mean = stats.mean(b_trl_percentages)
                if len(b_trl_percentages) < 3:
                    b_trl_percentages_std = 0
                else:
                    b_trl_percentages_std = stats.stdev(b_trl_percentages)
                #op_type_stats_solution_set.append((b_trl_percentages_mean, b_trl_percentages_std))
                balanced_translocations.append((b_trl_percentages_mean,b_trl_percentages_std))

                u_trl_percentages_mean = stats.mean(u_trl_percentages)
                if len(u_trl_percentages) < 3:
                    u_trl_percentages_std = 0
                else:
                    u_trl_percentages_std = stats.stdev(u_trl_percentages)
                #op_type_stats_solution_set.append((u_trl_percentages_mean, u_trl_percentages_std))
                unbalanced_transloctions.append((u_trl_percentages_mean,u_trl_percentages_std))

                fis_percentages_mean = stats.mean(fis_percentages)
                if len(fis_percentages) < 3:
                    fis_percentages_std=0
                else:
                    fis_percentages_std = stats.stdev(fis_percentages)
                #op_type_stats_solution_set.append((fis_percentages_mean, fis_percentages_std))
                fissions.append((fis_percentages_mean, fis_percentages_std))

                fus_percentages_mean = stats.mean(fus_percentages)
                if len(fus_percentages) < 3:
                    fus_percentages_std = 0
                else:
                    fus_percentages_std = stats.stdev(fus_percentages)
                #op_type_stats_solution_set.append((fus_percentages_mean, fus_percentages_std))
                fusions.append((fus_percentages_mean,fus_percentages_std))


                trp2_percentages_mean = stats.mean(trp2_percentages)
                if len(trp_percentages) < 3:
                    trp2_percentages_std = 0
                else:
                    trp2_percentages_std = stats.stdev(trp2_percentages)
                #op_type_stats_solution_set.append((trp2_percentages_mean, trp2_percentages_std))
                transpositions2.append((trp2_percentages_mean, trp2_percentages_std))

                #operation_types_op_sequence.append(op_type_stats_solution_set)




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

            df_inversions[column_name] = inversions
            df_transpositions[column_name] = transpositions
            df_balanced_translocations[column_name] = balanced_translocations
            df_unbalanced_translocations[column_name] = unbalanced_transloctions
            df_fissions[column_name] = fissions
            df_fusions[column_name] = fusions
            df_transpositions2[column_name] = transpositions2
        return df_solution_lengths_1, num_of_solutions, df_operation_types, genolve_time , percentage_true_solution_present, df_inversions, df_transpositions, df_balanced_translocations, df_unbalanced_translocations, df_fissions, df_fusions, df_transpositions2





