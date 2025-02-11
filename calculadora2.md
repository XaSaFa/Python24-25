```
numero1 = input("Digues el primer número: ")
numero1 = float(numero1)
numero2 = input("Digues el segon número: ")
numero2 = float(numero2)
operacio = input("Digues quina operació vols realitzar +,-,* o / ")
resultat = 0

# operació suma
if (operacio == "+"):
    resultat = numero1 + numero2
# operació resta
elif (operacio == "-"):
    resultat = numero1 - numero2
# operació multiplicació
elif (operacio == "*"):
    resultat = numero1 * numero2
# operació divisió
elif (operacio == "/"):
    # controlem error de divisió entre 0
    if(numero2 == 0):
        resultat = "infinit"
    else:
        resultat = numero1 / numero2
else:
    resultat = "entrada incorrecta"

print ("El resultat és ", resultat)
```
