
import pandas
u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()
u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"

#print(u202.head())
#print(u202[u202["znamka"].isnull()])
maturita = pandas.concat([u202,u203,u302], ignore_index=True)
#print(maturita.head())
#maturita.to_csv("maturita.csv", index=False)
studenti = pandas.read_csv("studenti.csv")
vysledky_se_jmeny = pandas.merge(maturita, studenti, how="left")
#print(vysledky_se_jmeny.head())
#print(maturita.shape)
#print(vysledky_se_jmeny.shape)
#print(maturita.head())
#print(studenti.head())
#print(vysledky_se_jmeny[vysledky_se_jmeny["jmeno"].isnull()])

predsedajici = pandas.read_csv("predsedajici.csv")
predsedajici["den"] = predsedajici["den"].str.strip()
vysledky_se_jmeny_a_predsedajicimi = pandas.merge(vysledky_se_jmeny, predsedajici, on="den")
#print(vysledky_se_jmeny_a_predsedajicimi.shape)
#print(u202.shape)
print(maturita.groupby('predmet')["znamka"].max())