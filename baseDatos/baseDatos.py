from pymongo.mongo_client import MongoClient#IMPORTAR PARA TRABAJR CON LA BASE DE DATOS 

#CONEXIÓN, DEFINIENDO UNA FUNCION SIENDO MONGO CLIENT DE LA BASE DE DATOS PROPIA
def conexion():
    uri = "mongodb+srv://nataliatovarc0303:1234@cluster0.vsdestk.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    return MongoClient(uri)

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos():
    client = conexion()
    db = client.actividad4.data_real
    data_list = []
    for data_real_bd in db.find():
        data_list.append(data_real_bd)
    return data_list

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""