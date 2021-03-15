class Polozka :
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr
  def getInfo(self):
    return f" {self.nazev}, {self.zanr},"

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka
  def getInfo(self):
    super().getInfo()
    return f"{super().getInfo()} film je dlouhý {self.delka} minut. "

movie = Film("I dva jsou rodina", "komedie", 118)
print(movie.getInfo())

class Serial(Polozka):
  def __init__(self, nazev, zanr,  pocet_epizod, delka_epizody):
    super().__init__(nazev, zanr)
    self.pocet_epizod = pocet_epizod
    self.delka_epizody = delka_epizody
  def getInfo(self):
    super().getInfo()
    return f"{super().getInfo()} seriál má {self.pocet_epizod} epizod a každá trvá {self.delka_epizody} minut."

seros = Serial("Mindhunter", "drama", 15, 55)
print(seros.getInfo())