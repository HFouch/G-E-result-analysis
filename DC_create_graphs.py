from getting_the_data import DataExtraction
from matplotlib import pyplot as plt
from class_graphs import Graphs

number_of_simulations = 1000
number_of_csv_files = 5
path_to_data = 'Results2/'
path_to_results = 'Results2_graphs2/'
file_prefix = 'ex_'
my_data = DataExtraction()
create_graph = Graphs(path_to_results,file_prefix, number_of_csv_files)
x = [4,5,6,7,8,9]

data_e1 = my_data.get_required_data(path_to_data, file_prefix+'1')

df_solution_lengths_e1 = data_e1[0]
number_of_solutions_e1 = data_e1[1]
df_operation_types_e1 = data_e1[2]
genolve_time_e1 = data_e1[3]
percentage_true_solution_present_e1 = data_e1[4]
df_num_inversions_e1 = data_e1[5]
df_num_transpositions_e1 = data_e1[6]
df_num_balanced_translocations_e1 = data_e1[7]
df_num_unbalanced_translocations_e1 = data_e1[8]
df_num_fissions_e1 = data_e1[9]
df_num_fusions_e1 = data_e1[10]
df_num_transpositions2_e1 = data_e1[11]


data_e2 = my_data.get_required_data(path_to_data, file_prefix+'2')

df_solution_lengths_e2 = data_e2[0]
number_of_solutions_e2 = data_e2[1]
df_operation_types_e2 = data_e2[2]
genolve_time_e2 = data_e2[3]
percentage_true_solution_present_e2 = data_e2[4]
df_num_inversions_e2 = data_e2[5]
df_num_transpositions_e2 = data_e2[6]
df_num_balanced_translocations_e2 = data_e2[7]
df_num_unbalanced_translocations_e2 = data_e2[8]
df_num_fissions_e2 = data_e2[9]
df_num_fusions_e2 = data_e2[10]
df_num_transpositions2_e2 = data_e2[11]


data_e3 = my_data.get_required_data(path_to_data, file_prefix+'3')

df_solution_lengths_e3 = data_e3[0]
number_of_solutions_e3 = data_e3[1]
df_operation_types_e3 = data_e3[2]
genolve_time_e3 = data_e3[3]
percentage_true_solution_present_e3 = data_e3[4]
df_num_inversions_e3 = data_e3[5]
df_num_transpositions_e3 = data_e3[6]
df_num_balanced_translocations_e3 = data_e3[7]
df_num_unbalanced_translocations_e3 = data_e3[8]
df_num_fissions_e3 = data_e3[9]
df_num_fusions_e3 = data_e3[10]
df_num_transpositions2_e3 = data_e3[11]

# Percentage true solution present
create_graph.percentage_true_sol_present_graph(x, percentage_true_solution_present_e1, percentage_true_solution_present_e2, percentage_true_solution_present_e3)

# Time Genolve took
create_graph.time_genolve_took_graphs(x, genolve_time_e1, genolve_time_e2, genolve_time_e3)

# Number of solutions per solution set
create_graph.ave_num_solutions_graph(x, number_of_solutions_e1, number_of_solutions_e2, number_of_solutions_e3)

x = list(range(0,number_of_simulations))
# Number of operations per solution size
create_graph.ave_num_of_operations_graphs(x, df_solution_lengths_e1, df_solution_lengths_e2, df_solution_lengths_e3)

# Number of each operation
# Experiment 1
create_graph.ave_num_type_of_operations(1, x, df_num_inversions_e1, df_num_transpositions_e1, df_num_balanced_translocations_e1, df_num_unbalanced_translocations_e1, df_num_fissions_e1, df_num_fusions_e1, df_num_transpositions2_e1)
# Experiment 2
create_graph.ave_num_type_of_operations(2, x, df_num_inversions_e2, df_num_transpositions_e2, df_num_balanced_translocations_e2, df_num_unbalanced_translocations_e2, df_num_fissions_e2, df_num_fusions_e2, df_num_transpositions2_e2)
# Experiment 3
create_graph.ave_num_type_of_operations(3, x, df_num_inversions_e3, df_num_transpositions_e3, df_num_balanced_translocations_e3, df_num_unbalanced_translocations_e3, df_num_fissions_e3, df_num_fusions_e3, df_num_transpositions2_e3)

