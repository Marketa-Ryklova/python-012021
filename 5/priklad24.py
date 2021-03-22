import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pandas.read_csv("temperature.csv")
temperature = temperature.set_index("City")
#temperature.info()
#print(temperature.loc["Prague"])
#print(temperature[temperature["AvgTemperature"] > 80])
regiony = temperature[(temperature["AvgTemperature"] > 60) & (temperature["Region"] == "Europe")]
#print(regiony)
extremni_hodnoty = temperature[(temperature["AvgTemperature"] > 80) | (temperature["AvgTemperature"] < -20)]
print(extremni_hodnoty)