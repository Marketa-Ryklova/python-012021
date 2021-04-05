import pandas
temperature = pandas.read_csv("temperature.csv", index_col=0)

print(temperature.head(5))
teplota_13 = temperature[temperature["Day"] == 13]
#print(teplota_13)
#filtrace 13.listopadu 2017

#print(teplota_13[teplota_13["AvgTemperature"] == -99])
teplota_13= teplota_13.drop(222)
teplota_13= teplota_13.drop(552)
teplota_13
#print(teplota_13[teplota_13["AvgTemperature"] == -99])
#vyřazené záznamy s teplotou -99

print(teplota_13)
print(teplota_13.groupby('Region').count())
#počet dat za daný den pro jednotlivé regiony

prumerna_teplote_regiony = teplota_13.groupby('Region')['AvgTemperature'].mean()
print(prumerna_teplote_regiony)
#prumerna teplota regiony

min_teplota_region = teplota_13.groupby('Region')['AvgTemperature'].min()
print(min_teplota_region)
#min teplota v regionech

max_teplota_region = teplota_13.groupby('Region')['AvgTemperature'].max()
print(max_teplota_region)
#maximalni teplotav regionech



