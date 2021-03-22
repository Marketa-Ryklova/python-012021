import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")
import pandas
character = pandas.read_csv("character-deaths.csv")
character = character.set_index("Name")
print(character.index)
print(character.iloc[0:])
print(character.loc["Hali"])
print(character.loc["Gevin Harlaw": "Gillam"])
print(character.loc["Gevin Harlaw": "Gillam", "Death Year"])
print(character.loc["Gevin Harlaw": "Gillam", "GoT": "DwD"])
