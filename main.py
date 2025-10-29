# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 16:48:40 2025

@author: yoyoi
"""
# main.py
import logging
from datetime import datetime
import os
import pandas as pd

from src.features import feature_engineering_lag
from src.loader import cargar_datos, convertir_clase_ternaria_a_target
from src.optimization import optimizar
from src.config import *

### Configuración de logging ###
os.makedirs("logs", exist_ok=True)
fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nombre_log = f"log_{STUDY_NAME}_{fecha}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s %(lineno)d - %(message)s",
    handlers=[
        logging.FileHandler("logs/" + nombre_log),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Iniciando programa de optimización con log fechado")

### Manejo de Configuración en YAML ###
logger.info("Configuración cargada desde YAML")
logger.info(f"STUDY_NAME: {STUDY_NAME}")
logger.info(f"DATA_PATH: {DATA_PATH}")
logger.info(f"SEMILLA: {SEMILLA}")
logger.info(f"MES_TRAIN: {MES_TRAIN}")
logger.info(f"MES_VALIDACION: {MES_VALIDACION}")
logger.info(f"MES_TEST: {MES_TEST}")
logger.info(f"GANANCIA_ACIERTO: {GANANCIA_ACIERTO}")
logger.info(f"COSTO_ESTIMULO: {COSTO_ESTIMULO}")


### Main ###
def main():
    """Pipeline principal con optimización usando configuración YAML."""
    logger.info("=== INICIANDO OPTIMIZACIÓN CON CONFIGURACIÓN YAML ===")
  
    # 1. Cargar datos
    df = cargar_datos(DATA_PATH)
  
    # 2. Feature Engineering
    atributos = ["mcuentas_saldo", "mtarjeta_visa_consumo", "cproductos"]
    cant_lag = 2
    df_fe = feature_engineering_lag(df, atributos, cant_lag)
    logger.info(f"Feature Engineering completado: {df_fe.shape}")
  
    # 3. Convertir clase_ternaria a binario
    df_fe = convertir_clase_ternaria_a_target(df_fe)
  
    # 4. Ejecutar optimización (función simple)
    study = optimizar(df_fe, n_trials=100)
  
    # 5. Análisis adicional
    logger.info("=== ANÁLISIS DE RESULTADOS ===")
    trials_df = study.trials_dataframe()
    if len(trials_df) > 0:
        top_5 = trials_df.nlargest(5, 'value')
        logger.info("Top 5 mejores trials:")
        for idx, trial in top_5.iterrows():
            logger.info(f"  Trial {trial['number']}: {trial['value']:,.0f}")
  
    logger.info("=== OPTIMIZACIÓN COMPLETADA ===")

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
    
    