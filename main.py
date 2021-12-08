import pandas as pd

a = pd.DataFrame({'num_legs': [1, 4], 'num_wings': [2, 0]},index=['falcon', 'dog'])
b = a.isin([2])
c = a.isin({'num_wings': [0, 3]})
d = a.isin({'num_legs': [4]})

other = pd.DataFrame({'num_legs': [8, 2], 'num_wings': [0, 2]},index=['dog', 'cat'])
print(a)
'''print(b)
print(c)
print(d)'''
print(other)

e = a.isin(other)
print(e)