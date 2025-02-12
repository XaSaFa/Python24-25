# Bucles for

for és una paraula reservada per Python per crear bucles iterant una variable.

La variable a iterar pot ser un número, però també un string, una llista, etc...

## Iterar de 0 a un número

Per exemple podem utilitzar for per a fer un programa que imprimeixi els números del 0 al 10, això es faria així.

```
for i in range(11):
  print(i)
```

La funció range genera una llista de números que comença per 0 i acaba en el número introduït menys 1, o sigui 10:  [0,1,2,3,4,5,6,7,8,9,10].

Així el programa anterior és equivalent a:

```
for i in [0,1,2,3,4,5,6,7,8,9,10]:
  print(i)
```

Però ocupa menys i és més entenedor.

## Iterar entre dos números.

Si volem que el programa imprimeixi un rang determinat de números l'indiquem a la funció range. El següent programa imprimeix els números de 1 a 5:

```
for i in range(1,6):
  print(i)
```

## Iterar entre dos números amb increment:

També podem indicar a la funció range que generi una llista de números que s'incrementin amb un valor fixe, per exemple, podríem fer un programa que imprimeixi els números múltiples de 5 entre 1 i 100 així:

```
for i in range(0,101,5):
  print(i)
```

Com veieu afegim un tercer **paràmetre** a la funció range.

## continue i break:

Les instruccions continue i else funcionen exactament igual que als bucles while per als bucles for.

## Bucles anidats:

Utilitzant for podem crear bucles anidats, és a dir, que un bucle estigui dins d'un altre bucle, per exemple:

```
for externa in range(1,4):
  print("iteració externa: ",externa)
  for interna in range(1,3):
    print("iteració interna: ", interna)
```

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Activitat**

1. Fes la funció factorial utilitzant un bucle for.
2. Fes un programa que pregunti un número i et tregui la seva taula de multiplicar.
3. Fes un programa que pregunta dos números a l'usuari i escriu els números des del més baix fins al més alt.
4. Fes un programa que pregunta una paraula a l'usuari i després mostra lletra a lletra.
5. Fes un programa que pregunta coses que has de comprar i cada vegada mostra la llista de la compra (utilitzant una llista).

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎
