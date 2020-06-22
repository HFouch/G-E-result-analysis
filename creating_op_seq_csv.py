import pandas as pd
import sys
import os
import csv

filename = 'e2_6.csv'
new_filename = 'm_data.csv'
df = pd.read_csv(filename, converters={'Operation_sequences': eval, 'Solution_sequence': eval})
operation_sequences = df['Operation_sequences']


all_operation_sequences = []
for solution_set in operation_sequences:
    x = 0
    while x < len(solution_set):
        print(solution_set[x])
        all_operation_sequences.append(solution_set[x])
        x+=1

print()

for solution in all_operation_sequences:
    with open(new_filename, 'a') as fd:

        str_solution = ''
        print('solution: ', solution)
        print('len: ', len(solution))
        i=0
        while i < len(solution):
            operation = solution[i]
            print('op + idx ', operation, solution.index(operation))
            #str_solution+=str(operation)
            if operation == 6.1:
                if i == len(solution)-2:
                    str_solution += '6'

                else:
                    str_solution+='6'
                    str_solution += ','
            elif operation == 6.2:
                pass
            else:

                if i==len(solution)-1:
                    str_solution += str(operation)

                else:
                    str_solution += str(operation)
                    str_solution += ','
            i+=1

        str_solution+='\n'

        print(str_solution)
        print()
        fd.write(str_solution)
