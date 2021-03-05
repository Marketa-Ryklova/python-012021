sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

totalSales = 0
for key, value in sales.items():
  print(f"Knihy {key} se prodalo {value} ks.")
  totalSales += value
print( f"Celkem bylo prodáno {totalSales} knih.")

books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
totalRevenue = 0
for item in books:
  if item ["year"] == 2019:
    totalRevenue += item["sold"] * item["price"]
print(f"Utržené tržby celkem {totalRevenue}")

def  greetUser(name):
  print(f"Ahoj {name}")
greetUser("Maky")

def sumTwoNumbers(a, b):
  return a + b
result = sumTwoNumbers(1, 2)
print(result)

def getMark(points, bonus=0):
  if points + bonus <= 60:
    mark = 5
  elif points + bonus <= 70:
    mark = 4
  elif points + bonus <= 80:
    mark = 3
  elif points + bonus <= 90:
    mark = 2
  else:
    mark = 1
  return mark
points = input("Kolik jsi dostal bodů?: ")
points = int(points)
bonus = input("Zadejpočet bonus bodů?: ")
bonus = int(bonus)
mark = getMark(points, bonus)
if mark == 5:
  points = input ("Počet bodů v opravném testu?:")
  points = int(points)
  mark = getMark(points)
print(f"Vysledná znamka je {mark}")




