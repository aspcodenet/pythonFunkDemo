# IDAG = ni får en funktion som ni kan använda i bankomat
# som matar in "failsafe"

# felinmatning
# namngivna parametrar
# default parameter
# LABBA

# REGEL:_ När vi skriver en funktion sp
# är dom enda variablerna vi använder = parametrar + lokala
def addAccount(allAccounts):
    kontonummer = input("Ange kontonummer")
    allAccounts[kontonummer] = 0

def addPlayer(allPlayers):
    namn = input("Ange namn")
    allPlayers.append(namn)

allAccounts =  {}
allPlayers =  []
addAccount(allAccounts)
addPlayer(allPlayers)

def IsMyndig(age):
    if age >= 18:
        return True
    else:
        return False

age = int(input("Din ålder"))    
myndig = IsMyndig(age)
if myndig:
    print("Myndig")
else:
    print("Icke myndig")



while True:
    age = int(input("Ange ålder:"))
    location = input("Ange plats K/S:")
    promille = float(input("Ange din promillehalt:"))






def Hello():
    age = age + 1
age = 12
Hello()
print(age)

def HittaLangstaOrdet(lista):
    longestSoFar = lista[0]
    for one in lista:
        pass
        #if len(lon)
    return longest

lista = ["aaa", "bbb", "Stefan"]
longest = HittaLangstaOrdet(lista)


def Plussa(s1,s2):
    result = s1 + s2
    return result

t = "Morgon"
res = Plussa("God ", t)





print("Hej hej")

def GetIntMenuInput(prompt, minValue, maxValue):
    while True:
        try:
            sel = int(input(prompt))
            if sel < minValue or sel > maxValue:
                print(f"Mata in ett tal mellan {minValue} och {maxValue} tack")
            else:
                break
        except:
            print("Mata in ett tal tack")
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

def theCalculation(a,b,c,d,e,f=2022,g=1,h=2,lang="SV"):
    pass

theCalculation(12,34,667,134556,7,2021)

print("Programmet börjar")
lang = input("Vilket språk vill du köra på - SV/EN?")
while True:
    PrintMeny(lang)
    #sel = GetIntMenuInput(prompt="Ange val:", minValue=1,maxValue=4)
    sel = GetIntMenuInput("Ange val:", 1,maxValue=4)
    if sel == 4:
        lang = input("Vilket språk vill du köra på - SV/EN?")
    if sel == 1:
        print("1. Skapa en bra spelare")
        print("2. Skapa en dålig spelare")
        sel = GetIntMenuInput("Ange spelartyp:", 1,2)

print("Programmet slutar")







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



def CalculateVat(pris, product):
    if product == "BOK":
        return pris * 0.06
    if product == "MAT":
        return pris * 0.12
    return pris * 0.25

