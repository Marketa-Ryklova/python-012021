from datetime import datetime, timedelta
performance_start = input("Zadejte datum představení: ")
start = datetime.strptime(performance_start, "%d. %m. %Y")
people = int(input("Zadej počet osob: "))

prvni_datum = datetime(2021, 7, 1)
druhe_datum = datetime(2021, 8, 10)
treti_datum = datetime(2021, 8, 11)
ctvrte_datum = datetime(2021, 8, 31)

vstupenka1 = 250
vstupenka2 = 180

cena_vstupenky1 = people * vstupenka1
cena_vstupenky2 = people * vstupenka2

cena1 = (start <= druhe_datum)
cena2 = (start >= treti_datum)


if start < prvni_datum:
  print("Letní kino je v tomto termínu uzavřené")
elif cena1:
  print(f"Cena vstupenky je {cena_vstupenky1}")
elif start > ctvrte_datum:
  print("Letní kino je v tomto termínu uzavřené")
elif cena2:
  print(f"Cena vstupenky je {cena_vstupenky2} ")





