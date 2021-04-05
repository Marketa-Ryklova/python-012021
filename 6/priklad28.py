import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

import pandas
staty = pandas.read_json("staty.json")

#print(staty.head())
staty_v_evrope = staty[staty["region"] == "Europe"]
#print(staty_v_evrope)
#Státy ležící v Evropě

pocet_statu = staty.groupby('subregion')['name'].count()
#print(pocet_statu)
#počet států v jednotlivých subregionech

celkove_obyvatelstvo_subregiony = staty.groupby('subregion')['population'].sum()
#print(celkove_obyvatelstvo_subregiony)
#počet obyvatel v subregionech

#print(staty.head())

gdp = pandas.read_csv("gdp.csv").dropna()
print(gdp.head())
#odstranění státu s chybějícími daty

staty = staty.rename(columns={'alpha3Code': 'Code'})
print(staty.head())
gdp = gdp.rename(columns={'Country Code': 'Code'})
print(gdp.head())

gdp_staty = pandas.merge(staty, gdp, on=['Code'])
print(gdp_staty.head())
gdp_staty.to_csv("gdp_staty.csv")
#zmergované tabulky staty a gdp

hdp_2019 = gdp_staty.groupby('subregion')['2019'].sum()
print(hdp_2019)
#celkovegdp dle subregionu
population_subregiony = gdp_staty.groupby('subregion')['population'].sum()
print(population_subregiony)
#celkova populace v subregionu

gdp_staty["gdp_per_person"] = hdp_2019/population_subregiony
print(gdp_staty)
#gdp per person

