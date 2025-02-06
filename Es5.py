#Autore: "Eduard Sascau"
#Data: "04/02/2025"
#Titolo: " Dati N numeri contare quanti sono positivi, negativi e uguali a zero "


n = int(input("Quanti numeri vuoi inserire? "))


positivi = 0
negativi = 0
zero = 0


for _ in range(n):
    num = int(input("Inserisci un numero: "))  
    if num > 0:
        positivi += 1
    elif num < 0:
        negativi += 1
    else:
        zero += 1


print(f"Positivi: {positivi}")
print(f"Negativi: {negativi}")
print(f"Uguali a zero: {zero}")