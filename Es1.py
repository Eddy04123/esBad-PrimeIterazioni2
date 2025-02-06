#Autore: "Eduard Sascau"
#Data: "04/02/2025"
#Titolo: "Chiedere in input un numero N. Stampare i numeri pari tra 0 e N.

n = int(input("quanti numeri vuoi "))


for i in range(0,n):
 
 if i%2==0:
  
  print(i)
  i+=1

else:
 
 i+=1
  