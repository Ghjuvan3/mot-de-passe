import random
import string

longueur = 20

caracteres = string.ascii_letters + string.digits + string.punctuation

mot_de_passe = ''.join(random.choice(caracteres) for i in range(longueur))

print("Mot de passe :", mot_de_passe)