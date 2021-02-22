volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

hodina = input("Zadejte hodinu kdy chcete zamluvit meeting room: ")
hodina = int(hodina)

if hodina in volnePokoje:
  print(len(volnePokoje[hodina]))
