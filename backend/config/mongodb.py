from pymongo import MongoClient
from typing import Dict, List, Any
import os
from dotenv import load_dotenv

class MongoDBHandler:
    def __init__(self):
        load_dotenv()  # Carga las variables de entorno desde el archivo .env
        self.usuario = os.getenv('MONGO_USERNAME')
        self.contraseña = os.getenv('MONGO_PASSWORD')
        self.host = os.getenv('MONGO_HOST')
        self.puerto = int(os.getenv('MONGO_PORT', 27017))
        self.nombre_db = os.getenv('MONGO_DB_NAME')
        self.client = None
        self.db = None

    def conectar(self):
        uri = f"mongodb://{self.usuario}:{self.contraseña}@{self.host}:{self.puerto}/?authSource=admin"
        try:
            self.client = MongoClient(uri)
            self.db = self.client[self.nombre_db]
            self.client.admin.command('ismaster')
            print("Conexión a MongoDB establecida correctamente.")
        except Exception as e:
            print(f"Error al conectar a MongoDB: {e}")

    def cerrar_conexion(self):
        if self.client:
            self.client.close()
            print("Conexión cerrada.")

    def crear_coleccion(self, nombre_coleccion: str):
        if self.db:
            coleccion = self.db[nombre_coleccion]
            print(f"Colección '{nombre_coleccion}' creada/accedida con éxito.")
            return coleccion
        else:
            print("Error: No hay conexión a la base de datos.")
            return None

    def insertar_documento(self, coleccion: str, documento: Dict[str, Any]):
        if self.db:
            resultado = self.db[coleccion].insert_one(documento)
            print(f"Documento insertado con id: {resultado.inserted_id}")
            return resultado.inserted_id
        else:
            print("Error: No hay conexión a la base de datos.")
            return None

    def buscar_documentos(self, coleccion: str, filtro: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        if self.db:
            return list(self.db[coleccion].find(filtro))
        else:
            print("Error: No hay conexión a la base de datos.")
            return []

    def actualizar_documento(self, coleccion: str, filtro: Dict[str, Any], nuevos_valores: Dict[str, Any]):
        if self.db:
            resultado = self.db[coleccion].update_one(filtro, {"$set": nuevos_valores})
            print(f"Documentos modificados: {resultado.modified_count}")
            return resultado.modified_count
        else:
            print("Error: No hay conexión a la base de datos.")
            return 0

    def eliminar_documento(self, coleccion: str, filtro: Dict[str, Any]):
        if self.db:
            resultado = self.db[coleccion].delete_one(filtro)
            print(f"Documentos eliminados: {resultado.deleted_count}")
            return resultado.deleted_count
        else:
            print("Error: No hay conexión a la base de datos.")
            return 0