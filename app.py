import json
import os

if os.path.exists(r"C:\Users\espan\Downloads\Proyecto_SGT\registro.json"):
    with open(r"C:\Users\espan\Downloads\Proyecto_SGT\registro.json", "r") as f:
        dict_reg = json.load(f)
else:
    dict_reg = {}

def registro(user, passw):
    dict_reg[user] = passw
    with open("registro.json", "w") as f:
        json.dump(dict_reg, f)
    print("Registro actualizado:", dict_reg)

def ingreso (user, passw):
    if dict_reg.get(user) == passw:
        print ("ingreso exitoso")
    else:
        print ("ingreso fallido")

registro("Juanes", "Juanes1227")
ingreso("Juanes", "Juanes1227")

