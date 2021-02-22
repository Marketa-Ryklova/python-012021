prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}
prodeje2020['Zkus mě chytit'] = 9828
titul = input("Zadej název knihy: ")
titul = str(titul)

if titul in prodeje2019 and titul in prodeje2020:
  print (prodeje2019[titul] + (prodeje2020[titul]))
elif titul in prodeje2020:
  print(prodeje2020[titul])
else:
  print("Tuto knihu nemáme v databázi")
