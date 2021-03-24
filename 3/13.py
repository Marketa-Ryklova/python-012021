class Car:
  def __init__(self, spz, type, km, dostupnost ):
    self.spz = spz
    self.type = type
    self.km = km
    self.dostupnost = dostupnost

peugeot = Car("4A2 3020", "Peugeot 403 Cabrio", "47534", True)
škoda = Car("1P3 4747", "Škoda Octavia", "41253", True)

auta = {
    "peugeot": peugeot,
    "škoda": škoda,
  }
peugeot = auta["peugeot"]
škoda = auta["škoda"]

vypujcka = input("Jakou značku auta si přejete půjčit? (peugeot/škoda) ")

  def getInfo(self):
    for vypujcka in auta:
      return f"Auto s SPZ {self.spz} typu {self.type}"

    #print(getInfo(peugeot))

  def pujc_auto(self):
    if self.dostupnost:
      self.dostupnost = False
      return f"Potvrzuji zapůjčené vozidla"
    if not self.dostupnost:
      return f"Vozidlo není k dispozici"

  def vrat_auto(self, pocet_km, pocet_dni):
    self.pocet_km = self.pocet_km + pocet_km
    self.pocet_dni = pocet_dni
    if pocet_dni < 7:
      price = 400 * pocet_dni
    else:
      price = 300 * pocet_dni
    return f"Cena za vypůjčení auta je {price} Kč."
    #print(vrat_auto())

pocet_dni = input("Kolik dní jste měli auto půjčené?")
pocet_km = input("Kolik km jste ujeli?")

#peugeot = Car("4A2 3020", "Peugeot 403 Cabrio", "47534", True)
#škoda = Car("1P3 4747", "Škoda Octavia", "41253", True)

#auta = {
    #"peugeot": peugeot,
    #"škoda": škoda,
#  }
#peugeot = auta["peugeot"]
#škoda = auta["škoda"]

#vypujcka = input("Jakou značku auta si přejete půjčit? (peugeot/škoda) ")

 # def getInfo(self):
  #  for vypujcka in auta:
   #   return f"Auto s SPZ {self.spz} typu {self.type}"

#print(getInfo(peugeot))

#pocet:dni = input("Kolik dní jste měli auto půjčené?")
#pocet_km = input("Kolik km jste ujeli?")