import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pandas.read_csv("temperature.csv")
temperature = temperature.set_index("Day")

#print(temperature.head(5))
temperature["13. listopadu 2017"]