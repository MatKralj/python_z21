import numpy as np

def testirajSamoortogonalnost(matrica):
    maxVal = np.amax(matrica)
    minVal = np.amin(matrica)
    if 0<=maxVal<=1 and 0<=minVal<=1:
        if produktOdgovara(matrica):
            return True
    return False

def produktOdgovara(matrica):
    for i in range (0, np.size(matrica, 0)):
        for j in range (i, np.size(matrica, 0)):
            a = np.dot(matrica[i], matrica[j])
            if a%2!=0:
                return False
    return True


def dajMatricuOdKorisnika():
    matrica = np.empty((3,4), int)
    print("\nUnesite matricu dimenzija 3x4 (3 retka i 4 stupca)\n ")
    for i in range (0, 3):
        print("Unos %i. retka:\n"% (i+1))
        for j in range (0, 4):
            element = int(input("\tUnesite element %i : "%(j+1)))
            matrica[i][j] = element
    return matrica


A = np.array([[1,1,0],[0,0,1],[1,0,0],[0,0,1]])
B = np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
C = np.array([[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
D = np.array([[1,0,0],[0,1,1],[0,0,0],[0,0,0]])

samoortogonalna = testirajSamoortogonalnost(A)
print ("Matrica A:\n", A)
print ("\tje samootrogonalna modulo 2: %r" % samoortogonalna)


samoortogonalna = testirajSamoortogonalnost(B)
print ("Matrica B:\n", B)
print ("\tje samootrogonalna modulo 2: %r" % samoortogonalna)

samoortogonalna = testirajSamoortogonalnost(C)
print ("Matrica C:\n", C)
print ("\tje samootrogonalna modulo 2: %r" % samoortogonalna)

samoortogonalna = testirajSamoortogonalnost(D)
print ("Matrica D:\n", D)
print ("\tje samootrogonalna modulo 2: %r" % samoortogonalna)

korisnikova = dajMatricuOdKorisnika()
samoortogonalna = testirajSamoortogonalnost(korisnikova)
print ("Matrica korisnikova:\n", korisnikova)
print ("\tje samootrogonalna modulo 2: %r" % samoortogonalna)