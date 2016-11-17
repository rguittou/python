#!/usr/bin/python3
# CECI N'EST QUE POUR POUVOIR EXECUTER DANS LE SHELL

########################################################################################################################################
#                                                      Import
#######################################################################################################################################
import sys, datetime

print(sys.version_info)
print(sys.version)
print(sys.platform)
print("je suis le module:", __name__)  # affiche le nom du module principal


########################################################################################################################################
#                                                       Definition de fonction
#######################################################################################################################################

# param:str string
# print the string passed in parameter
def firstFunction(str):
    print(str)
    return


# param:name string
# param:age int
# print user info passed in parameter
def printInfo(age, name):
    print("name:", name)
    print("age:", age)
    print(len(name))  # Affiche la longeur de chaine
    return


a = 259
b = 259
print(id(a), id(b))
# param:file
# print the file






########################################################################################################################################
#                                                       Appel de fonction
#######################################################################################################################################
firstFunction(str="c'est bon");
printInfo(29, "toto");

##exercice sur les list

alist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print(str(alist[:4]))
print(alist[4:])
print(alist[3:-3])

##exercice affichage
i = 5.596
mykey = "temps"
fois = 20
# "formatage chaine de caractere pour affichage de varaible"

print('la valeur %2.2f et le mot %s apparaissent %d fois.' % (i, mykey, fois))
print('la valeur {} et le mot {} apparaissent {} fois.'.format(i, mykey, fois))

# clause if
valeur = "toto"
valeur2 = "titi"

if valeur == "ok":
    print("ok")
elif valeur == "dog":
    print("dog")
else:
    print("inconnu")

if (valeur == "toto" and valeur2 == "titi"):
    print("ok")

# for
seq = [1, 2, 3, 4]
#
a, b, c, d = seq
print(b)

for letter in "Spam":
    print("current letter:", letter)

# parcour d'une sequence
for a in seq:
    print(a)

# boucle avec range

for i in range(1, 15):
    print("étape :", i)
    if (i == 12):
        print("break, out of the for statement")
        break

var = 10

# while statement
while True:
    var -= 1
    print("étape:{}".format(var))
    if (var == 6):
        continue
        print(var)
    if (var == 0):
        print("var a zero|end loop:break")
        break

# list comprehension
a = [1, 4, 2, 7, 1, 9, 0, 3, 4, 6, 6, 6, 8, 3]

# on filtre la liste en gardant les valeurs supp à 5 qu'on met dans b
b = []
for x in a:
    if x > 5:
        b.append(x)
    print("b", b)

# l'ordre à une importance, d'abord le resultat, ensuite les operation
c = [x for x in a if x > 5]
print("c:", c)

#####17/11/2016 exercice

# calcul vitesse
temps = 6.896
distance = 19.7

vitesse = distance / temps
print("la vitesse necessaire pour parcourir la distance d={}m en un temps t={}s est de v={:.2f} m/s".format(distance,
                                                                                                            temps,
                                                                                                            vitesse))

# entier de 0 a 3 avec range

for i in range(4):
    print(i)
print("fin entier de 0 à 3")

# entier de 4 à 7 avec range mais en utilisant des itérateurs avec la fonction iter()
l = range(4, 8)
generateur = iter(l)
for i in l:
    print(next(generateur))
print("fin des entiers de 4 à 7")
# affiché caractere suivant à l'aide d'1 bcle
msg = "c'est la formation devops"
for s in msg:
    print(s)
print("fin boucle affichage caractere chaine msg")
# soit la liste suivante:trier la liste
liste = [17, 38, 10, 25, 72]

print(sorted(liste))
# ajout l'element 12
liste.append(12)
print(liste)
# indice de l'element 17
print("index de l'element 17 est {}".format(liste.index(17)))
# enlever 38 est afficher la liste
liste.remove(38)
print(liste)
# afficher sous liste 3eme element jusqu'q la afin
print("sous liste:", liste[2:])

print(
    "                                                      ######################### Fin du Main ######################")
