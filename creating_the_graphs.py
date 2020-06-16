from getting_the_data import DataExtraction
from matplotlib import pyplot as plt

number_of_simulations = 1000
number_of_csv_files = 5
my_data = DataExtraction()

data_e1 = my_data.get_required_data('Results(trp2_6.1_6.2)/','e1')

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


data_e2 = my_data.get_required_data('Results(trp2_6.1_6.2)/', 'e2')

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


data_e3 = my_data.get_required_data('Results(trp2_6.1_6.2)/' ,'e3')

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

colors = ['red', 'blue', 'green']
x = [4,5,6,7,8]

# Percentage true solution present
plt.figure(figsize=(10,10))
plt.plot(x, percentage_true_solution_present_e1, color='red', marker='o')
plt.plot(x, percentage_true_solution_present_e2, color='blue', marker='o')
plt.plot(x, percentage_true_solution_present_e3, color='green', marker='o')
plt.legend(['one to one ratio', 'same as solution ratio', 'random ratio'], loc=1)
plt.title("Comparison of the percentage time the 'true scenario' was present in a solution set \n across genomes increasing in complexity for the three weight ratios")
plt.xlabel('Genomic Complexity')
plt.ylabel("Percentage time the 'true scenario' was present")
plt.savefig('Results(trp2_6.1_6.2)/percentages.png')
plt.close()


# Time Genolve took
time_means_e1= [x[0] for x in genolve_time_e1]
time_std_e1 = [x[1] for x in genolve_time_e1]
time_means_e2= [x[0] for x in genolve_time_e2]
time_std_e2 = [x[1] for x in genolve_time_e2]
time_means_e3= [x[0] for x in genolve_time_e3]
time_std_e3 = [x[1] for x in genolve_time_e3]
plt.figure(figsize=(10,10))
plt.errorbar(x, time_means_e1, color=colors[0], marker='o', yerr=time_std_e1, ecolor='black')
plt.errorbar(x, time_means_e2, color=colors[1], marker='o', yerr=time_std_e2, ecolor='black')
plt.errorbar(x, time_means_e3, color=colors[2], marker='o', yerr=time_std_e3, ecolor='black')
plt.legend(['one to one ratio', 'same as solution ratio', 'random ratio'], loc=2)
plt.title('Comparison of the time Genolve takes to run with increasing genome complexity')
plt.xlabel('Measure of genome complexity')
plt.ylabel('Time taken by Genolve (seconds)')
plt.savefig('Results(trp2_6.1_6.2)/genolve_time.png')
plt.close()


# Number of solutions per solution set
num_sol_means_e1= [x[0] for x in number_of_solutions_e1]
num_sol_std_e1 = [x[1] for x in number_of_solutions_e1]
num_sol_means_e2= [x[0] for x in number_of_solutions_e2]
num_sol_std_e2 = [x[1] for x in number_of_solutions_e2]
num_sol_means_e3= [x[0] for x in number_of_solutions_e3]
num_sol_std_e3 = [x[1] for x in number_of_solutions_e3]
plt.figure(figsize=(10,10))
plt.errorbar(x, num_sol_means_e1, color=colors[0], marker='o', yerr=num_sol_std_e1, ecolor='black')
plt.errorbar(x, num_sol_means_e2, color=colors[1], marker='o', yerr=num_sol_std_e2, ecolor='black')
plt.errorbar(x, num_sol_means_e3, color=colors[2], marker='o', yerr=num_sol_std_e3, ecolor='black')
plt.legend(['one to one ratio', 'same as solution ratio', 'random ratio'], loc=2)
plt.title('Comparison of the average number of solutions per solution set with increasing genome complexity')
plt.xlabel('Measure of genome complexity')
plt.ylabel('Average number of solutions per solution set across 100 000 runs')
plt.savefig('Results(trp2_6.1_6.2)/number_of_solutions.png')
plt.close()

# Number of operations per solution size
for i in range(1,number_of_csv_files+1):
    fig_name = 'Results(trp2_6.1_6.2)/ave_num_of_ops_per_solset_'+str(i)+'.png'
    plt.figure(figsize=(28,10))

    # e1 values
    e1_column_name = 'e1_'+str(i)
    mean_e1 = [x[0] for x in df_solution_lengths_e1[e1_column_name]]
    std_e1 = [x[1] for x in df_solution_lengths_e1[e1_column_name]]

    # e2 values
    e2_column_name = 'e2_' + str(i)
    mean_e2 = [x[0] for x in df_solution_lengths_e2[e2_column_name]]
    std_e2 = [x[1] for x in df_solution_lengths_e2[e2_column_name]]

    # e3 values
    e3_column_name = 'e3_' + str(i)
    mean_e3 = [x[0] for x in df_solution_lengths_e3[e3_column_name]]
    std_e3 = [x[1] for x in df_solution_lengths_e3[e3_column_name]]

    x = list(range(0, number_of_simulations))

    plt.subplot(1,3,1)
    plt.plot(x, mean_e1, color=colors[0], marker='o', markersize=1, linewidth=0)
    plt.errorbar(x, mean_e1, color=colors[0], yerr=std_e1, capsize=5, linestyle="None")
    plt.title('One to one ratios')
    plt.xlabel('Run number')
    plt.ylabel('Average number of operations per solution set')

    plt.subplot(1,3,2)
    plt.plot(x, mean_e2, color=colors[1], marker=',', markersize=1, linewidth=0)
    plt.errorbar(x, mean_e2, color=colors[1], yerr=std_e2, capsize=5, linestyle="None")
    plt.title('Same as solution ratios')
    plt.xlabel('Run number')
    plt.ylabel('Average number of operations per solution set')

    plt.subplot(1, 3, 3)
    plt.plot(x, mean_e3, color=colors[2], marker=',', markersize=1, linewidth=0)
    plt.errorbar(x, mean_e3, color=colors[2], yerr=std_e3, capsize=5, linestyle="None")
    plt.title('Random ratios')
    plt.xlabel('Run number')
    plt.ylabel('Average number of operations per solution set')


    plt.savefig(fig_name)
    plt.close()



# Number of each operation
for i in range(1,number_of_csv_files+1):
    fig_name = 'Results(trp2_6.1_6.2)/ave_num_of_ops_types_per_solset_'+str(i)+'.png'
    plt.figure(figsize=(28,28))
    
    colors = ['darkred', 'orange', 'forestgreen', 'deepskyblue', 'mediumorchid', 'lightpink','slategray']
    
    # e1 values
    e1_column_name = 'e1_'+str(i)
    inv_mean_e1 = [x[0] for x in df_num_inversions_e1[e1_column_name]]
    inv_std_e1 = [x[1] for x in df_num_inversions_e1[e1_column_name]]
    trp_mean_e1 = [x[0] for x in df_num_transpositions_e1[e1_column_name]]
    trp_std_e1 = [x[1] for x in df_num_transpositions_e1[e1_column_name]]
    b_trl_mean_e1 = [x[0] for x in df_num_balanced_translocations_e1[e1_column_name]]
    b_trl_std_e1 = [x[1] for x in df_num_balanced_translocations_e1[e1_column_name]]
    u_trl_mean_e1 = [x[0] for x in df_num_unbalanced_translocations_e1[e1_column_name]]
    u_trl_std_e1 = [x[1] for x in df_num_unbalanced_translocations_e1[e1_column_name]]
    fis_mean_e1 = [x[0] for x in df_num_fissions_e1[e1_column_name]]
    fis_std_e1 = [x[1] for x in df_num_fissions_e1[e1_column_name]]
    fus_mean_e1 = [x[0] for x in df_num_fusions_e1[e1_column_name]]
    fus_std_e1 = [x[1] for x in df_num_fusions_e1[e1_column_name]]
    trp2_mean_e1 = [x[0] for x in df_num_transpositions2_e1[e1_column_name]]
    trp2_std_e1 = [x[1] for x in df_num_transpositions2_e1[e1_column_name]]


    # e2 values
    e2_column_name = 'e2_' + str(i)
    mean_e2 = [x[0] for x in df_solution_lengths_e2[e2_column_name]]
    std_e2 = [x[1] for x in df_solution_lengths_e2[e2_column_name]]

    # e3 values
    e3_column_name = 'e3_' + str(i)
    mean_e3 = [x[0] for x in df_solution_lengths_e3[e3_column_name]]
    std_e3 = [x[1] for x in df_solution_lengths_e3[e3_column_name]]

    x = list(range(0,number_of_simulations))

    #plt.subplot(1, 3, 1)
    #plt.plot(x, inv_mean_e1, color=colors[0], marker='o', markersize=5, linewidth=0)
    #plt.errorbar(x, inv_mean_e1, color=colors[0], yerr=inv_std_e1, capsize=5, linestyle="None")
    plt.plot(x, trp_mean_e1, color=colors[1], marker='o', markersize=5, linewidth=0)
   # plt.errorbar(x, trp_mean_e1, color=colors[1], yerr=trp_std_e1, capsize=5, linestyle="None")
    plt.plot(x, b_trl_mean_e1, color=colors[2], marker='o', markersize=5, linewidth=0)
   # plt.errorbar(x, b_trl_mean_e1, color=colors[2], yerr=b_trl_std_e1, capsize=5, linestyle="None")
    plt.plot(x, u_trl_mean_e1, color=colors[3], marker='o', markersize=5, linewidth=0)
   # plt.errorbar(x, u_trl_mean_e1, color=colors[3], yerr=u_trl_std_e1, capsize=5, linestyle="None")
    plt.plot(x, fis_mean_e1, color=colors[4], marker='o', markersize=5, linewidth=0)
   # plt.errorbar(x, fis_mean_e1, color=colors[4], yerr=fis_std_e1, capsize=5, linestyle="None")
    plt.plot(x, fus_mean_e1, color=colors[5], marker='o', markersize=5, linewidth=0)
   # plt.errorbar(x, fus_mean_e1, color=colors[5], yerr=fus_std_e1, capsize=5, linestyle="None")
    plt.plot(x, trp2_mean_e1, color=colors[6], marker='o', markersize=5, linewidth=0)
   # plt.errorbar(x, trp2_mean_e1, color=colors[6], yerr=trp2_std_e1, capsize=5, linestyle="None")

    plt.plot(x, inv_mean_e1, color=colors[0], marker='o', markersize=5, linewidth=0)

    plt.title('One to one ratios')
    plt.xlabel('Run number')
    plt.ylabel('Average number of operations per solution set')
    plt.legend(
        ['inversions', 'transpositions', 'balanced translocations', 'unbalanced translocations', 'fissions', 'fusions',
         'block-interchanges'])


    plt.savefig(fig_name)
    plt.close()
