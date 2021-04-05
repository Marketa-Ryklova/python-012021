import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

import pandas
staty = pandas.read_json("staty.json")

print(staty.head())
staty_v_evrope = staty[staty["region"] == "Europe"]
print(staty_v_evrope)
#Státy ležící v Evropě

pocet_statu = staty.groupby('subregion')['name'].count()
print(pocet_statu)
#počet států v jednotlivých subregionech

celkove_obyvatelstvo_subregiony = staty.groupby('subregion')['population'].sum()
print(celkove_obyvatelstvo_subregiony)
#počet obyvatel v subregionech
