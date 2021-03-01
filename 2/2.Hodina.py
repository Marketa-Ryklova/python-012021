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


