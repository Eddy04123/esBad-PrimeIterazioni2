#Autore: "Eduard Sascau"
#Data: "04/02/2025"
#Titolo: "Si abbiano in input due numeri interi A e N e dati N numeri contare quanti sono i multipli di A.


a = int(input( "sottomultiplo "))
n = int(input(" numeri  ")) 
c = 0

for i in range (1,n+1):
    
   if i % a == 0 :
   
    c += 1


print("i multipli di",a,"in",n,"numeri sono:",c)