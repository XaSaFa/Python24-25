# Bucles

Els bucles serveixen per repetir blocs de codi més d'una vegada.

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/b572db59-a11a-4114-a02a-56c58938bf54)

## While

La comanda while serveix per repetir codi **MENTRE ES COMPLEIXI UNA CONDICIÓ**.

Exemple: Aquest programa imprimirà els números del 1 al 10.

```
a = 0
while a <10:
  a += 1
  print (a)
```

La condició de sortida s'avalua abans d'executar el codi dins el bucle.

El codi que es fiqui fora del bucle while s'executarà quan termini el bucle:

```
a = 0
while a <10:
  a += 1
  print (a)
print("s'ha acabat el bucle")
```

### continue

la comanda continue trenca la iteració del bucle i torna a iniciar el bucle a la següent iteració.

```
a = 0
while a <10:
  a += 1
  if a == 5:
    continue
  print (a)
```

Aquest codi fa que la iteració en la que a val 5 salti del continue al següent while.

### break

La comanda break trenca definitivament un bucle:

```
a = 0
while a <10:
  a += 1
  if a == 5:
    break
  print (a)
```

Aquest programa s'acaba quan a val 5.


## Activitat

Feu un programa que pregunti un número a l'usuari i retorni el valor factorial d'aquell número.

Per exemple, el factorial de 5 és: ```5*4*3*2*1```

Feu el mateix programa utilitzant un break dins el bucle.


