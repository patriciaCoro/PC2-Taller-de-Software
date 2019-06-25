import random



n=[]
c= 0
while True:
    a= int(input("Ingrese un número: "))
    if (0<a<11) and (n.count(a)==0):
        n.append(a)
        c=c+1
    else:
        print("Ingrese un número distinto  del 1 al 10")
    if (c==6):
        break
    
Ra=[]
c2=0
while True:
    a1=random.randint(1,10)
    if Ra.count(a1)==0:
        Ra.append(a1)
        c2= c2+1
    if (c2==6):
        break
    

print(n)
print(Ra)
