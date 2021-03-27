import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
vaccination = pandas.read_csv("country_vaccinations.csv")
vaccination = vaccination.set_index("date")

vaccination.info()
print(vaccination.loc["2021-03-10","country" : "total_vaccinations"])
#dotaz na počty očkovaných

vakcinace =  vaccination[(vaccination["total_vaccinations"] > 1_000_000)]
print(vakcinace.loc["2021-03-10"])
#2021-03-10 naočkovano vic než 1 mil osob

extremni_hodnoty = vaccination[(vaccination["total_vaccinations"] > 100_000) | (vaccination["total_vaccinations"] < 100)]
print(extremni_hodnoty.loc["2021-03-10"])
#dotaz na extrémní hodnoy


