#Autore: "Eduard Sascau"
#Data: "04/02/2025"
#Titolo: "Si abbia in input un numero N. Stampare i dieci numeri pari successivi al numero N."


n = int(input("Dammi un numero: "))
s = int(input(" quanti numeri pari dopo n vuoi ")) 


if n % 2 == 0:
    n += 2
else:
    n += 1


for _ in range(s):
    print(n)
    n += 2  


