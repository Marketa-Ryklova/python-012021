#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
import pandas

zam_praha = pandas.read_csv("zam_praha.csv", index_col=0)
zam_plzeň = pandas.read_csv("zam_plzeň.csv", index_col=0)
zam_liberec = pandas.read_csv("zam_liberec.csv", index_col=0)
zam_praha["mesto"] = "Praha"
zam_plzeň["mesto"] = "Plzeň"
zam_liberec["mesto"] = "Liberec"
#prridani sloupce mesto
zamestnanci = pandas.concat([zam_praha, zam_plzeň, zam_liberec], ignore_index=True)
print(zamestnanci.shape)
#vytvoření tabulky zamestnanci
platy = pandas.read_csv("platy_2021_02.csv")
print(platy.shape)
zamestnanci_platy = pandas.merge(zamestnanci, platy)
print(zamestnanci_platy)
print(zamestnanci_platy.shape)

prumer_plat = zamestnanci_platy.groupby ('mesto')['plat'].mean()
print(prumer_plat)
#prumerny plat dle kancelari
