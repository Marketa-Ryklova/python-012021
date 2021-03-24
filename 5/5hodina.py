import pandas
import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
nakupy = pandas.read_csv("nakupy.csv")
#print(nakupy.iloc[8:])
pozdrav = "Ahoj Andreo"
print(nakupy.tail())
