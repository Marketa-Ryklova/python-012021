import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
vaccination = pandas.read_csv("country_vaccinations.csv")
vaccination = vaccination.set_index("date")

#vaccination.info()
#print(vaccination.loc["2021-03-10", "country" : "total_vaccinations"])
#print(vaccination[vaccination["total_vaccinations"] > 1000000])
#vakcinace = vaccination[vaccination["total_vaccinations"] > 1000000]
#print(vakcinace[["country"]])
#print(vaccination.loc["2021-03-10", "total_vaccinations"] > 1_000_000)
vakcinace = vaccination[vaccination.loc["2021-03-10", "total_vaccinations"] > 1_000_000]
print(vakcinace)
