import os
try:
    val1 = int(input("Saisir votre chiffre"))
except ValueError :
    print('Merci de saisir un chiffre')
try:    
    val2 = str(input("Saisir le signe de votre calcul"))
except ValueError :
    print('Merci de saisir le signe de votre calcul')
try:    
    val3 = int(input("Saisir votre chiffre"))
except ValueError :
    print('Merci de saisir un chiffre')
if val2 == "+":
    val4 = val1 + val3
    print('val4 ', val4)
if val2 == "-":
    val4 = val1 - val3
    print(val4)
if val2 == "*":
    val4 = val1 * val3
    print(val4)
if val2 == "/":
    val4 = val1 / val3
    print(val4)
    
os.system("pause")

