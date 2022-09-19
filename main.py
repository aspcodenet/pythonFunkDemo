# IDAG = ni får en funktion som ni kan använda i bankomat
# som matar in "failsafe"

print("Hej hej")

def GetIntMenuInput(prompt, minValue, maxValue):
    while True:
        sel = int(input(prompt))
        if sel < minValue or sel > maxValue:
            print(f"Mata in ett tal mellan {minValue} och {maxValue} tack")
        else:
            break
    return sel

def PrintMeny(languageCode):
    if languageCode == "SV":
        print("1. Skapa spelare")
        print("2. Lista spelare")
        print("3. Avsluta")
        print("4. Välj språk")
    elif languageCode == "EN":
        print("1. Create player")
        print("2. List all players")
        print("3. Exit")
        print("4. Select language")


# TVÅ STÄLLEN I RAMMINNET DÄR VARIABLER LAGRAS
# stack
# heap
def addTo(x):
    ee = 12
    x = x + 1
    print(x)

x = 12
y=13
r = 13

addTo(x) 
print(x)

def addToList(lista):
    lista.append(14)

lista = [12,13]
print(lista)
addToList(lista)
print(lista)


print("Programmet börjar")
lang = input("Vilket språk vill du köra på - SV/EN?")
while True:
    PrintMeny(lang)
    sel = GetIntMenuInput("Ange val:",1,4)
    if sel == 4:
        lang = input("Vilket språk vill du köra på - SV/EN?")
    if sel == 1:
        print("1. Skapa en bra spelare")
        print("2. Skapa en dålig spelare")
        sel = GetIntMenuInput("Ange spelartyp:", 1,2)

print("Programmet slutar")




def CalculateVat(pris, product):
    if product == "BOK":
        return pris * 0.06
    if product == "MAT":
        return pris * 0.12
    return pris * 0.25

