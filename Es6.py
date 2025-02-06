#Autore: "Eduard Sascau"
#Data: "04/02/2025"
#" Dati N numeri calcolare la media aritmetica dei valori pari e quella dei valori dispari"

n =int(input("quanti numeri "))

sp = 0 
sd = 0
cnp = 0 
cnd=0


for i in range(n):
  
  num=int(input("inserisci numero "))

  if num %2 == 0 :

    sp= sp+num 
    cnp =+ 1

  else:

    sd= sd+num 
    cnd =+1



  
if cnp > 0:
    sp = sp / cnp
    print("Media numeri pari è:", sp)
else:
    print("Non ci sono numeri pari.")

if cnd > 0:
    sd = sd / cnd
    print("Media numeri dispari è:", sd)
else:
    print("Non ci sono numeri dispari.")



