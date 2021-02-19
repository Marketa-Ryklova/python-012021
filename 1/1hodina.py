["Čajová konvička s hrnky", 899, True]
item = {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True}
key = "price"
item[key] = 929
print("Vybraný předmět je " + item['title'] + " a cena je " + str(item['price']) +".")
print("Vybraný předmět je ", item["title"], ".")
print(f"Vybraný předmět je {item['title']} a cena je {item['price']}.")

item["weight"] = 0.6
if "weight" in item:
  print(f"Hmotnost předmětu je: {item['weight']}")
else:
  print("Hmotnost není zadána")

sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}
print(len(sausages))
sausages["Jirka"] = 0
print(len(sausages))
sausages.pop("Jirka")
print(len(sausages))

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
number = input("Zadej číslo lístku: ")
number = int(number)
if number in tombola:
  print("Vyhráváš: " + tombola [number])
else:
  print("Nevyhráváš nic")
