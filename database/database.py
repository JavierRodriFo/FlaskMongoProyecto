from http import client
from pymongo import MongoClient
import json
import certifi

ca= certifi.where()


def loadConfigFile():
    with open ('database/config.json') as f:
        data= json.load(f)
    return data

def dbConnection():
    dataConfig = loadConfigFile()
    try:
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], TlsCAFile=ca)

        #client = MongoClient(dataConfig['MONGO_URI_LOCAL'],dataConfig['LOCAL_PORT])
        db = client["Proyecto_Final_Cicloa1_Grupo37"]
    except:  
        print("Error de conexion en la db") 

    return db             