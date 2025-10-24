# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 16:48:40 2025

@author: yoyoi
"""
import pandas as pd
import os
import datetime
import logging

from src.loader import cargar_datos
from src.features import feature_engineering_lag

#revisa qeu exista la carpeta logs
os.makedirs("logs", exist_ok=True)

fecha= datetime.datetime.now().strptime("%Y-%m-%d %H:%M:%S")
nombre_log= f"logs/{fecha}.log"
logging.basicConfig(
    filename=f"logs/{nombre_log}",
    level=logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(name)s - %(lineno)d- %(message)s",
    handlers=[
        logging.FileHandler(f"logs/{nombre_log}", mode="w", encoding="utf-8"),
        logging.StreamHandler()
    ]
    )
logger = logging.getLogger(__name__)


def main():
    logger.info("Inicio de ejecucion.")

    #00 Cargar datos
    os.makedirs("data", exist_ok=True)
    path = "data/competencia_01.csv"
    df = cargar_datos(path)   

    #01 Feature Engineering
    atributos = ["ctrx_quarter"]
    cant_lag = 2
    df = feature_engineering_lag(df, columnas=atributos, cant_lag=cant_lag)
  
    #02 Guardar datos
    path = "data/competencia_01_lag.csv"
    df.to_csv(path, index=False)
  
    logger.info(f">>> Ejecución finalizada. Revisar logs para mas detalles.{nombre_log}")

if __name__ == "__main__":
    main()

#def cargar_datos(path: str) -> pd.DataFrame:
 #   '''
  #  Carga un CSV desde 'path' y retorna un pandas.DataFrame.
   # '''
    #df = pd.read_csv(path)
    #return df


#if __name__ == "__main__":
 #   df = cargar_datos("data/competencia_01.csv")
  #  print(df.head())
    
    # el entorno virtual tiene las librerías y las versiones que utiliza nuestro proyecto en particular
    #por ejemplo si por algun motivo usa una librería en versión vieja, cuando la actualizo en mi compu no se rompe todo el proyecto
    # el collab hace lo mismo cuando le pongo conectar
    
    