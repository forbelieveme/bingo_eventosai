import numpy as np
import pandas as pd

<<<<<<< HEAD
file = open("C:\\Users\Jimenez Medina\\Desktop\Archivos Backup\\bingo_eventosai\\cartonescomas.csv")
numline = len(file.readlines())
print (numline)
=======

df = pd.read_csv('cartonescomas2.csv')
# print(df.head())
print(len(df))
print(len(df.columns))
b = df.loc[:,['n1b1','n1b2','n1b3','n1b4','n1b5']]

print(len(b))
print(len(b.columns))

print(b[b['n1b1'] > 15])

# file = open("cartonescomas.csv")
# numline = len(file.readlines())
# print (numline)
>>>>>>> refs/remotes/origin/main
