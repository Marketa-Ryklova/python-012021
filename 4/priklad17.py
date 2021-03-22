class Polozka :
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr
  def getInfo(self):
    return f" {self.nazev}, {self.zanr},"

class Uzivatel:
  def __init__(self, uzivatelske_jmeno):
    self.uzivatelske_jmeno = uzivatelske_jmeno
    self.delka_sledovani = 0

  def pripocti_zhlednuti(self, delka_sledovani):
    self.delka_sledovani = delka_sledovani
    return self.delka_sledovani

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka
  def get_celkova_delka(self):
    self.delka = self.delka
    return self.delka

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
  def get_celkova_delka(self):
    self.delka_serialu = self.delka_epizody * self.pocet_epizod
    return self.delka_serialu

  #def getInfo(self):
   # super().getInfo()
   # return f"{super().getInfo()} seriál má {self.pocet_epizod} epizod a každá trvá {self.delka_epizody} minut."

film = Film("Nedotknutelní", "Komedie", 112)
serial = Serial("Mindhunter", "drama", 15, 55)
uzivatel = Uzivatel("Marketa")

print(film.get_celkova_delka())
print(serial.get_celkova_delka())
print(uzivatel.pripocti_zhlednuti(serial.get_celkova_delka()+ film.get_celkova_delka()))