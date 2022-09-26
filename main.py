#Write a program that joins two text files and records the results in a third file. PS:
#first delete the third file if if already exists!

# player ska ha jerseyNumber, namn, Teamname
# player = namn

from dataclasses import dataclass

import jsonpickle


@dataclass
class Player:
    Namn: str
    JerseyNumber: int
    Teamname: str

# p2 = Player("Mats Sundin", 13, "Toronto")
# p2.Teamname
# l = []
# l.append(p1)
# .Teamname = "Tre Kronor"
# print(p1.Namn)
# print(p2.Namn)


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


def CreatePlayer(): # black box - kommer ut ut den så ska vi ha en ny player (namn - string)
    namn = input("Ange namn:")
    team = input("Ange lag:")
    jersey = int(input("Ange jersey:"))
    player = Player(namn,jersey,team) 
    return player
    
def ListPlayers(listOfPlayers): 
    for player in listOfPlayers:
        print(f"{player.JerseyNumber} {player.Namn} {player.Teamname}")

def DeletePlayer(listOfPlayer):
    index = 1
    for playerName in listOfPlayer:
        print(f"{index} {playerName}")
        index = index + 1
    sel = GetIntMenuInput("Ange spelare att ta bort:",1, len(listOfPlayer))
    del listOfPlayer[sel-1]


def ChangePlayer(listOfPlayer):
    while True:
        print(" *** PLAYER MENU *** ")
        print("1. Ändra namn")
        print("2. Ändra jersey")
        print("3. Tillbaka till huvudmenyn")
        sel = GetIntMenuInput("Ange val:", 1, 3)
        if sel == 1:
            index = 1
            for playerName in listOfPlayer:
                print(f"{index} {playerName}")
                index = index + 1
            sel = GetIntMenuInput("Ange spelare att ändra namn på:",1, len(listOfPlayer))

            namn = input("Ange nytt namn")
            listOfPlayer[sel-1] = namn
        elif sel == 2:
            print("To be implemented")
        elif sel == 3:
            return          


def MenuPrint():
    print("1. Skapa spelare")
    print("2. Lista spelare")
    print("3. Ändra spelare")
    print("4. Ta bort spelare")
    print("5. Avsluta")
# ibland så returnerar INTE en funktion nånting


def AddTwoNumbers(tal1:int, tal2:int) -> int:
    return tal1 + tal2

def HuvudMenyInput(lista):        
    a = AddTwoNumbers()
    n = GetIntMenuInput()
    while True:
        MenuPrint()
        sel = GetIntMenuInput("Ange val:", 1, 5)
        if sel == 1:
            player = CreatePlayer()
            lista.append(player)
        if sel == 2:
            ListPlayers(lista)
        if sel == 4:
            DeletePlayer(lista)
        if sel == 3:
            ChangePlayer(lista)
        if sel == 5:
            break


lista = []

with open("spelare-objekt.txt", "r") as filen:
    lista = jsonpickle.decode(filen.read())


# # Läs in alla spelare
# with open("spelare-objekt.txt", "r") as filen:
#     counter = 0
#     for raden in filen:
#         if counter == 0:
#             player = Player("",0,"")
#             lista.append(player)
#             player.Namn = raden.replace("\n", "")
#         if counter == 1:
#             player.JerseyNumber = int(raden.replace("\n", ""))
#         if counter == 2:
#             player.Teamname = raden.replace("\n", "")
#         counter = counter + 1
#         if counter == 3:
#             counter = 0

        # f.write(player.Namn + "\n")
        # f.write(str(player.JerseyNumber) + "\n")
        # f.write(player.Teamname + "\n")





HuvudMenyInput(lista)
# class Player:
#    Namn: str
#    JerseyNumber: int
#    Teamname: str


with open("spelare-objekt.txt", "w") as f:
    f.write(jsonpickle.encode(lista))

# with open("spelare-objekt.txt", "w") as f:
#     for player in lista:
#         f.write(player.Namn + "\n")
#         f.write(str(player.JerseyNumber) + "\n")
#         f.write(player.Teamname + "\n")
        

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
    return age >= 18
    # if age >= 18:
    #     return True
    # else:
    #     return False

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








fil1 = "spelare.txt"
fil2 = "spelare2.txt"
resultFile = "total.txt"

with open(resultFile, "w") as resultFile:
    with open(fil1, "r") as fil1:
        for raden in fil1:
            resultFile.write(  raden.replace("\n", "") + "\n")            
    with open(fil2, "r") as fil2:
        for raden in fil2:
            resultFile.write(raden.replace("\n", "") + "\n")            

print("sdffssd")

# Läs in alla spelare
with open("spelare.txt", "r") as filen:
    isOnOddLine = True
    for raden in filen:
        if isOnOddLine:
            print(raden)
        # isOnOddLine = not isOnOddLine
        if isOnOddLine:
            isOnOddLine = False
        else:
            isOnOddLine = True
        


x = 12
if x > 10:
    print("bla bl223a")
print("234234")    

for x in range(0,5):
    if x > 10:
        print("sdfrsdsdffsd")
    print(x)




# anropa funktion från funktion
# submeny och 4 = tillbaka till huvudmenyn

# FUNKTION ett kodblock som vi ger ett namn
# en funktion kan TA IN PARAMETRAR
# return  

# def calculateSalary(monthly, age):
#     extra = 0
#     if age > 65:
#         extra = 1.1
#     if age < 20:
#         extra = 1.3
#     salary = extra * monthly
#     return salary


# print("Innan")
# lonen = calculateSalary(10000, 68)
# alder = int(input("Ange ålder"))
# lonen2 = calculateSalary(10000,alder )
# print("Klar")
