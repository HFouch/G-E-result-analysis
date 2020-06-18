from matplotlib import pyplot as plt
import pandas as pd

class Graphs:
    def __init__(self, path_to_results, file_prefix, number_of_csv_files, number_of_simulations):
        self.path_to_results = path_to_results
        self.file_prefix = file_prefix
        self.number_of_csv_files = number_of_csv_files
        self.number_of_simulations = number_of_simulations
        pass

 
    def percentage_true_sol_present_graph(self ,percentage_true_solution_present_e1, percentage_true_solution_present_e2, percentage_true_solution_present_e3 ):
        # Percentage true solution present
        x = list(range(4, self.number_of_csv_files+4))
        plt.figure(figsize=(10, 10))
        plt.plot(x, percentage_true_solution_present_e1, color='red', marker='o')
        plt.plot(x, percentage_true_solution_present_e2, color='blue', marker='o')
        plt.plot(x, percentage_true_solution_present_e3, color='green', marker='o')
        plt.legend(['one to one ratio', 'same as solution ratio', 'random ratio'], loc=1)
        plt.title(
            "Comparison of the percentage time the 'true scenario' was present in a solution set \n across genomes increasing in complexity for the three weight ratios")
        plt.xlabel('Genomic Complexity')
        plt.ylabel("Percentage time the 'true scenario' was present")
        plt.savefig(self.path_to_results + 'percentages.png')
        plt.close()
        
        
    def time_genolve_took_graphs(self, genolve_time_e1,genolve_time_e2,genolve_time_e3 ):
        # Time Genolve took
        x = list(range(4, self.number_of_csv_files + 4))
        colors = ['red', 'blue', 'green']
        time_means_e1 = [x[0] for x in genolve_time_e1]
        time_std_e1 = [x[1] for x in genolve_time_e1]
        time_means_e2 = [x[0] for x in genolve_time_e2]
        time_std_e2 = [x[1] for x in genolve_time_e2]
        time_means_e3 = [x[0] for x in genolve_time_e3]
        time_std_e3 = [x[1] for x in genolve_time_e3]
        plt.figure(figsize=(10, 10))
        plt.errorbar(x, time_means_e1, color=colors[0], marker='o', yerr=time_std_e1, ecolor=colors[0])
        plt.errorbar(x, time_means_e2, color=colors[1], marker='o', yerr=time_std_e2, ecolor=colors[1])
        plt.errorbar(x, time_means_e3, color=colors[2], marker='o', yerr=time_std_e3, ecolor=colors[2])
        plt.legend(['one to one ratio', 'same as solution ratio', 'random ratio'], loc=2)
        plt.title('Comparison of the time Genolve takes to run with increasing genome complexity')
        plt.xlabel('Measure of genome complexity')
        plt.ylabel('Time taken by Genolve (seconds)')
        plt.savefig(self.path_to_results + 'genolve_time.png')
        plt.close()

    def ave_num_solutions_graph(self, number_of_solutions_e1, number_of_solutions_e2, number_of_solutions_e3):
        # Number of solutions per solution set
        x = list(range(4, self.number_of_csv_files + 4))
        colors = ['red', 'blue', 'green']
        num_sol_means_e1 = [x[0] for x in number_of_solutions_e1]
        num_sol_std_e1 = [x[1] for x in number_of_solutions_e1]
        num_sol_means_e2 = [x[0] for x in number_of_solutions_e2]
        num_sol_std_e2 = [x[1] for x in number_of_solutions_e2]
        num_sol_means_e3 = [x[0] for x in number_of_solutions_e3]
        num_sol_std_e3 = [x[1] for x in number_of_solutions_e3]
        plt.figure(figsize=(10, 10))
        plt.errorbar(x, num_sol_means_e1, color=colors[0], marker='o', yerr=num_sol_std_e1, ecolor=colors[0])
        plt.errorbar(x, num_sol_means_e2, color=colors[1], marker='o', yerr=num_sol_std_e2, ecolor=colors[1])
        plt.errorbar(x, num_sol_means_e3, color=colors[2], marker='o', yerr=num_sol_std_e3, ecolor=colors[2])
        plt.legend(['one to one ratio', 'same as solution ratio', 'random ratio'], loc=2)
        plt.title('Comparison of the average number of solutions per solution set with increasing genome complexity')
        plt.xlabel('Measure of genome complexity')
        plt.ylabel('Average number of solutions per solution set across 100 000 runs')
        plt.savefig(self.path_to_results + 'number_of_solutions.png')
        plt.close()
    
    def ave_num_of_operations_graphs(self, df_solution_lengths_e1, df_solution_lengths_e2, df_solution_lengths_e3 ):
        # Number of operations per solution size
        x = list(range(1, self.number_of_simulations+1))
        for i in range(1, self.number_of_csv_files + 1):
            colors = ['red', 'blue', 'green']
            fig_name = self.path_to_results + 'ave_num_of_ops_per_solset_' + str(i) + '.png'
            plt.figure(figsize=(28, 10))

            # e1 values
            e1_column_name = self.file_prefix + '1_' + str(i)
            mean_e1 = [x[0] for x in df_solution_lengths_e1[e1_column_name]]
            std_e1 = [x[1] for x in df_solution_lengths_e1[e1_column_name]]

            # e2 values
            e2_column_name = self.file_prefix + '2_' + str(i)
            mean_e2 = [x[0] for x in df_solution_lengths_e2[e2_column_name]]
            std_e2 = [x[1] for x in df_solution_lengths_e2[e2_column_name]]

            # e3 values
            e3_column_name = self.file_prefix + '3_' + str(i)
            mean_e3 = [x[0] for x in df_solution_lengths_e3[e3_column_name]]
            std_e3 = [x[1] for x in df_solution_lengths_e3[e3_column_name]]

            plt.subplot(1, 3, 1)
            plt.plot(x, mean_e1, color=colors[0], marker='o', markersize=1, linewidth=0)
            plt.errorbar(x, mean_e1, color=colors[0], yerr=std_e1, capsize=5, linestyle="None")
            plt.title('One to one ratios')
            plt.xlabel('Run number')
            plt.ylabel('Average number of operations per solution set')

            plt.subplot(1, 3, 2)
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

    def ave_num_type_of_operations(self, experiment_number, df_num_inversions,df_num_transpositions, df_num_balanced_translocations,df_num_unbalanced_translocations,  df_num_fissions,  df_num_fusions, df_num_transpositions2):
        # Number of each operation
        x = list(range(1, self.number_of_simulations + 1))
        for i in range(1, self.number_of_csv_files + 1):

            if experiment_number == 1:
                fig_name =  self.path_to_results + 'e1_ave_num_of_ops_types_per_solset_' + str(i) + '.png'
                title = 'One to one ratios'
            elif experiment_number == 2:
                fig_name = self.path_to_results + 'e2_ave_num_of_ops_types_per_solset_' + str(i) + '.png'
                title = 'Same as solution ratios'
            elif experiment_number ==3:
                fig_name = self.path_to_results + 'e3_ave_num_of_ops_types_per_solset_' + str(i) + '.png'
                title = 'Randomized ratios'

            
            colors = ['darkred', 'orange', 'forestgreen', 'deepskyblue', 'mediumorchid', 'lightpink', 'slategray']

            #  values
            column_name = self.file_prefix + str(experiment_number)+'_' + str(i)
            inv_mean = [x[0] for x in df_num_inversions[column_name]]
            inv_std = [x[1] for x in df_num_inversions[column_name]]
            trp_mean = [x[0] for x in df_num_transpositions[column_name]]
            trp_std = [x[1] for x in df_num_transpositions[column_name]]
            b_trl_mean = [x[0] for x in df_num_balanced_translocations[column_name]]
            b_trl_std = [x[1] for x in df_num_balanced_translocations[column_name]]
            u_trl_mean = [x[0] for x in df_num_unbalanced_translocations[column_name]]
            u_trl_std = [x[1] for x in df_num_unbalanced_translocations[column_name]]
            fis_mean = [x[0] for x in df_num_fissions[column_name]]
            fis_std = [x[1] for x in df_num_fissions[column_name]]
            fus_mean = [x[0] for x in df_num_fusions[column_name]]
            fus_std = [x[1] for x in df_num_fusions[column_name]]
            trp2_mean = [x[0] for x in df_num_transpositions2[column_name]]
            trp2_std = [x[1] for x in df_num_transpositions2[column_name]]
           
            #plots
            plt.figure(figsize=(28, 28))
            plt.plot(x, inv_mean, color=colors[0], marker='o', markersize=5, linewidth=0)
            # plt.errorbar(x, inv_mean, color=colors[0], yerr=inv_std, capsize=5, linestyle="None")
            plt.plot(x, trp_mean, color=colors[1], marker='o', markersize=5, linewidth=0)
            # plt.errorbar(x, trp_mean, color=colors[1], yerr=trp_std, capsize=5, linestyle="None")
            plt.plot(x, b_trl_mean, color=colors[2], marker='o', markersize=5, linewidth=0)
            # plt.errorbar(x, b_trl_mean, color=colors[2], yerr=b_trl_std, capsize=5, linestyle="None")
            plt.plot(x, u_trl_mean, color=colors[3], marker='o', markersize=5, linewidth=0)
            # plt.errorbar(x, u_trl_mean, color=colors[3], yerr=u_trl_std, capsize=5, linestyle="None")
            plt.plot(x, fis_mean, color=colors[4], marker='o', markersize=5, linewidth=0)
            # plt.errorbar(x, fis_mean, color=colors[4], yerr=fis_std, capsize=5, linestyle="None")
            plt.plot(x, fus_mean, color=colors[5], marker='o', markersize=5, linewidth=0)
            # plt.errorbar(x, fus_mean, color=colors[5], yerr=fus_std, capsize=5, linestyle="None")
            plt.plot(x, trp2_mean, color=colors[6], marker='o', markersize=5, linewidth=0)
            # plt.errorbar(x, trp2_mean, color=colors[6], yerr=trp2_std, capsize=5, linestyle="None")

            plt.title(title)
            plt.xlabel('Run number')
            plt.ylabel('Average number of operations per solution set')
            plt.legend(
                ['inversions', 'transpositions', 'balanced translocations', 'unbalanced translocations', 'fissions',
                 'fusions',
                 'block-interchanges'])

            plt.savefig(fig_name)
            plt.close()



        
