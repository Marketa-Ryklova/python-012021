import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
twlo = pandas.read_csv("twlo.csv")

twlo.info()
print(twlo.loc[301])
print(twlo.iloc[:6])
print(twlo.head(6))
print(twlo.tail(11))