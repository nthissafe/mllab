import csv
import numpy as np
with open('Enjoy-sport.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
print(data[-1][-1])
d = np.array(data)[:,:-1]
print("The Attributes are: \n",d)

h = ['0', '0', '0', '0', '0', '0','0']
for row in data:
    if row[-1] == 'yes':
        j=0
        for col in row:
            if col != h[j]:
                if h[j] == '0':
                    h[j] = col
                elif h[j] != '0':
                    h[j] = '?'
            j = j+1


print('Maximally Specific Hypothesis: \n', h[slice(5)])