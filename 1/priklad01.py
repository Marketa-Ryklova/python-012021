baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
čísloBalíku = input("Zadej číslo balíku: ")



if baliky[čísloBalíku]:
    print(f"Balík byl předán kurýrovi")
else:
    print(f"Balík zatím nebyl předán kurýrovi")