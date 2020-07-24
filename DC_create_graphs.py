from getting_the_data import DataExtraction
from matplotlib import pyplot as plt
from class_graphs import Graphs

number_of_simulations = 100000
number_of_csv_files = 6
path_to_data = 'Results3/'
path_to_results = 'Results4_graphs/'
file_prefix = 'ex_'
my_data = DataExtraction(number_of_csv_files, number_of_simulations)
create_graph = Graphs(path_to_results,file_prefix, number_of_csv_files, number_of_simulations)


data_e1 = my_data.get_required_data(path_to_data, file_prefix+'1')

df_solution_lengths_e1 = data_e1[0]
number_of_solutions_e1 = data_e1[1]
df_operation_types_e1 = data_e1[2]
genolve_time_e1 = data_e1[3]
percentage_true_solution_present_e1 = data_e1[4]
genolve_time_e1_boxplot = data_e1[5]
number_of_solutions_e1_boxplot = data_e1[6]


data_e2 = my_data.get_required_data(path_to_data, file_prefix+'2')

df_solution_lengths_e2 = data_e2[0]
number_of_solutions_e2 = data_e2[1]
df_operation_types_e2 = data_e2[2]
genolve_time_e2 = data_e2[3]
percentage_true_solution_present_e2 = data_e2[4]
genolve_time_e2_boxplot = data_e2[5]
number_of_solutions_e2_boxplot = data_e1[6]


data_e3 = my_data.get_required_data(path_to_data, file_prefix+'3')

df_solution_lengths_e3 = data_e3[0]
number_of_solutions_e3 = data_e3[1]
df_operation_types_e3 = data_e3[2]
genolve_time_e3 = data_e3[3]
percentage_true_solution_present_e3 = data_e3[4]
genolve_time_e3_boxplot = data_e3[5]
number_of_solutions_e3_boxplot = data_e1[6]


create_graph.box_plot_spread(genolve_time_e1_boxplot, genolve_time_e2_boxplot, genolve_time_e3_boxplot, 'time',  None)
create_graph.box_plot_spread(number_of_solutions_e1_boxplot, number_of_solutions_e2_boxplot, number_of_solutions_e3_boxplot, 'number_of_solutions', None)

#Time Genolve took
#create_graph.time_genolve_took_graphs(genolve_time_e1, genolve_time_e2, genolve_time_e3)
# Number of solutions per solution set
#create_graph.ave_num_solutions_graph(number_of_solutions_e1, number_of_solutions_e2, number_of_solutions_e3)

# Number of operations per solution size
#create_graph.ave_num_of_operations_graphs(df_solution_lengths_e1, df_solution_lengths_e2, df_solution_lengths_e3)

# Number of operations per solution size
#create_graph.ave_num_of_operations_graphs(df_solution_lengths_e1, df_solution_lengths_e2, df_solution_lengths_e3)

'''

# Percentage true solution present
create_graph.percentage_true_sol_present_graph(percentage_true_solution_present_e1, percentage_true_solution_present_e2, percentage_true_solution_present_e3)

#Time Genolve took
create_graph.time_genolve_took_graphs(genolve_time_e1, genolve_time_e2, genolve_time_e3)

# Number of solutions per solution set
create_graph.ave_num_solutions_graph(number_of_solutions_e1, number_of_solutions_e2, number_of_solutions_e3)

# Number of operations per solution size
create_graph.ave_num_of_operations_graphs(df_solution_lengths_e1, df_solution_lengths_e2, df_solution_lengths_e3)

# Number of each operation
# Experiment 1
create_graph.ave_num_type_of_operations(1, df_num_inversions_e1, df_num_transpositions_e1, df_num_balanced_translocations_e1, df_num_unbalanced_translocations_e1, df_num_fissions_e1, df_num_fusions_e1, df_num_transpositions2_e1)
# Experiment 2
create_graph.ave_num_type_of_operations(2, df_num_inversions_e2, df_num_transpositions_e2, df_num_balanced_translocations_e2, df_num_unbalanced_translocations_e2, df_num_fissions_e2, df_num_fusions_e2, df_num_transpositions2_e2)
# Experiment 3
create_graph.ave_num_type_of_operations(3, df_num_inversions_e3, df_num_transpositions_e3, df_num_balanced_translocations_e3, df_num_unbalanced_translocations_e3, df_num_fissions_e3, df_num_fusions_e3, df_num_transpositions2_e3)


'''
