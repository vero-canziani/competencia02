# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 18:32:31 2025

@author: yoyoi
"""

import yaml
import os
import logging

logger = logging.getLogger(__name__)

#Ruta del archivo de configuracion
PATH_CONFIG = os.path.join(os.path.dirname(os.path.dirname(__file__)), "conf.yaml")

try:
    with open(PATH_CONFIG, "r") as f:
        _cfgGeneral = yaml.safe_load(f)
        _cfg = _cfgGeneral["competencia01"]

        STUDY_NAME = _cfgGeneral.get("STUDY_NAME", "Wendsday")
        DATA_PATH = _cfg.get("DATA_PATH", "../data/competencia.csv")
        SEMILLA = _cfg.get("SEMILLA", [42])
        MES_TRAIN = _cfg.get("MES_TRAIN", "202102")
        MES_VALIDACION = _cfg.get("MES_VALIDACION", "202103")
        MES_TEST = _cfg.get("MES_TEST", "202104")
        GANANCIA_ACIERTO = _cfg.get("GANANCIA_ACIERTO", None)
        COSTO_ESTIMULO = _cfg.get("COSTO_ESTIMULO", None)
        
        
        # Configuración para entrenamiento final
        FINAL_TRAIN = _cfg.get("FINAL_TRAIN", ["202101", "202102", "202103", "202104"])
        FINAL_PREDIC = _cfg.get("FINAL_PREDIC", "202106")

except Exception as e:
    logger.error(f"Error al cargar el archivo de configuracion: {e}")
    raise
