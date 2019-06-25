N = [[1,2,0],[3,1,4],[3,0,1]]
A = [[1,2],[1,1]]
C = [1]



def SumDiPar(a):
    resultado = "La matriz", a, "es impar"
    suma=0
    for i in range(len(a)):
        suma = suma + a[i][i] 

    if suma%2==0:
        resultado = "La matriz", a, "es papar"
    return resultado

SumDiPar(N)
SumDiPar(A)
SumDiPar(C)
