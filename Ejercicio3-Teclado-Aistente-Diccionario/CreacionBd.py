'''
Created on Apr 4, 2013

@author: jc
'''
from MainZoDb import Manejo_Db
import transaction


# Creacion de la base de datos
db = Manejo_Db('Dataprueba.fs')  # Nombre de la Bd
dbroot = db.dbroot
dbroot['palabras'] = {22288663266833: 'abundante', 26622244666: 'ancho',\
        3338833: 'fue', 2668337777: 'antes', 2777777444222: 'arriba',\
        22225666: 'abajo', 224443366: 'bien', 22883366666: 'bueno',\
        222882663666: 'cuando', 2226666666: 'como', 244444: 'ahi',\
        22225554443366833: 'caliente', 388777266833: 'durante',\
        68822244666: 'mucho', 22244288: 'chau', 7666777: 'por',\
        778833: 'que', 366666333: 'donde', 727772: 'para',\
        4777222244427777: 'gracias', 66666: "no", 7777444: 'si',\
        888666999: 'voy', 442777782: 'hasta', 3377777337772777: 'esperar',\
        446665552: 'hola', 66232: 'nada', 4777266333: "grande",\
        299933777: 'ayer', 25558666: 'alto', 44666999: 'hoy'}
dbroot['codletra'] = {"2": "a", "22": "b", "222": "c", "3": "d", "33": "e",\
        "333": "f", "4": "g", "44": "h", "444": "i", "5": "j", "55": "k",\
        "555": "l", "6": "m", "66": "n", "666": "o", "7": "p", "77": "q",\
        "777": "r", "7777": "s", "8": "t", "88": "u", "888": "v", "9": "w",\
        "99": "x", "999": "y", "9999": "z", '*': "-", '#': " "}
transaction.commit()
db.close()
