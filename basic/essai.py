#!/usr/bin/python3

import sys


#lecture argument parametre
#sys.argv[o]=nom_fichier.py
#sys.argv[>1]: parametre passés dans l'ordre

def info(name, firstname):
    print ("username:",name)
    print ("userfirstname:",firstname)

def equal(a,b):
    if(a != b):
        print("la valeur de a:{} n'est pas égal à la valeur de b:{}".format(a,b))
    else:
        print("la valeur de a:{}== a la valeur de b:{}".format(a,b))

equal (sys.argv[1],sys.argv[2]);