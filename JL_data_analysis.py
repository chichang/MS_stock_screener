import csv
import numpy as np
filepath = '/USERS/jackiel/Downloads/AAPL_Income_Statement.csv'
with open(filepath,'r') as fr:
    data_iter = csv.reader(fr,delimiter = ",", quotechar = '"')
    data = [data for data in data_iter]
data_array = np.asarray(data)
print data_array

for s in range(2,len(data_array)):      
    avg = (np.sum([float(i) for i in data_array[s][1:] if i != ''])/(len(data_array[s][1:])))
    print data_array[s][0] + ": " + str(avg)