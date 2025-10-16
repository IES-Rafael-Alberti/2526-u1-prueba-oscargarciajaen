# programa.py
# -*- coding: utf-8 -*-
"""
Radares de tramo — Esqueleto para alumnos
- Lectura de fichero YA resuelta (función leer_casos).
- main() itera sobre las líneas y llama a procesar_linea(linea).
- procesar_linea(linea) está VACÍA; los alumnos deben implementarla.
"""

from typing import List
import sys
from pathlib import Path


def leer_casos(ruta_fichero: str) -> List[str]:
    """
    Lee un fichero de texto con casos de prueba, devolviendo
    una lista de líneas (str) ya limpias, sin la línea de terminación "0 0 0".
    Ignora líneas en blanco y comentarios que empiecen por '#'.

    """
    ruta = Path(ruta_fichero)
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el fichero: {ruta_fichero}")

    casos: List[str] = []
    with ruta.open(encoding="utf-8") as f:
        for raw in f:
            linea = raw.strip()
            if not linea or linea.startswith("#"):
                continue
            if linea == "0 0 0":
                break
            casos.append(linea)
    return casos


def procesar_linea(linea: str) -> str:
    """
    TODO: Implementar por el alumnado.

    Recibe:
        linea (str): cadena con tres enteros: distancia_m, vmax_kmh, tiempo_s,
         separados por espacios.

    Debe devolver uno de los textos EXACTOS:

        - "OK"

        - "MULTA"

        - "PUNTOS"

        - "ERROR"

    Recomendación:

    1) Parsear ints; si hay problema o valores inválidos -> "ERROR".

    2) Calcular la velocidad media y compararla con los umbrales.

    3) Devolver el texto pedido.

    """
  # --- Implementación del alumnado aquí ---

    distancia_m, vmax_kmh, tiempo_s = linea.split()
    distancia_m = int(distancia_m)
    vmax_kmh = int(vmax_kmh)
    tiempo_s = int(tiempo_s)

    try:
        if distancia_m <= 0 or vmax_kmh <= 0 or tiempo_s <= 0:
            return("ERROR")
        else:
        
            velocidad_media = (distancia_m/tiempo_s)*3.6

            if velocidad_media <= vmax_kmh:
                return("OK")
            elif vmax_kmh < velocidad_media and velocidad_media < vmax_kmh*(1.20):
                return("MULTA")
            elif velocidad_media >= vmax_kmh*(1.20):
                return("PUNTOS")
            else:
                return("ERROR")
    
    except ValueError:
        return("ERROR")
    
    
  #  raise NotImplementedError("Función aún no implementada por el alumnado.")


# a main se llama de la siguiente forma  main(sys.argv)
def main(argv: List[str]) -> None:
    if len(argv) < 2:
        print("Uso: python programa.py <ruta_entrada.txt>")
        sys.exit(1)

    ruta = argv[1]
    for linea in leer_casos(ruta):
        resultado = procesar_linea(linea)   # <- llamada a la función de los alumnos
        print(resultado)                     # <- impresión del resultado