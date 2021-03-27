import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pandas.read_csv("temperature.csv", index_col=0)

print(temperature.head(5))
teplota_13 = temperature[temperature["Day"] == 13]
print(teplota_13)
#dotaz nařádky z 13.listopadu 2017

teplota_v_us = temperature[(temperature["Day"] == 13) & (temperature["Country"] == "US")]
print(teplota_v_us)
#teploty 13.listopadu v US

mesta = teplota_v_us[teplota_v_us["City"].isin(["Washington", "Philadephia"])]
print(mesta)


