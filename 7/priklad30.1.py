import pandas
temperature = pandas.read_csv("temperature.csv", index_col=0)

print(temperature.head(5))
teplota_13 = temperature[temperature["Day"] == 13]
print(teplota_13)
#filtrace 13.listopadu 2017

print(teplota_13[teplota_13["AvgTemperature"] == -99])
teplota_13= teplota_13.drop(222)
teplota_13= teplota_13.drop(552)
teplota_13
print(teplota_13[teplota_13["AvgTemperature"] == -99])
#vyřazené záznamy s teplotou -99

razeni = teplota_13.sort_values(by="AvgTemperature", ascending=False)
print(razeni)
#serazeni teploty od nejvyssi po nejnizsi
print(razeni.head())
#5mest s nejvyssi teplotou
print(razeni.tail())
#5 mest s nejnizsi teplotou

