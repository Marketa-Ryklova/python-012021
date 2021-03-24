import pandas
import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")
staty = pandas.read_json("staty.json")
staty = staty.set_index("name")

lidnate_evropske_staty = staty[(staty["population"] > 20_000_000)& (staty["region"] == "Europe")]
print(lidnate_evropske_staty)
vyznamne_staty = staty[(staty["population"] > 1_000_000_000) | (staty["area"] > 3_000_000)]
#print(vyznamne_staty)
zap_vych_evropa = staty[staty["subregion"].isin(["Western Europe", "Eastern Europe"])]
print(zap_vych_evropa)