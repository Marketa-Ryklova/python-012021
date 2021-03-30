import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

import pandas
vykazy = pandas.read_csv("vykazy.csv", index_col = 0)
print(vykazy.head())
hodiny_projekty = vykazy.groupby('project')['hours'].sum()
print(hodiny_projekty)