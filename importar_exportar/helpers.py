from pathlib import Path
from openpyxl import load_workbook

def crear_carpeta_si_no_existe(carpeta: Path):
  carpeta.mkdir(parents=True, exist_ok=True)

def eliminar_hoja(ruta_archivo, nombre_hoja):
  libro = load_workbook(ruta_archivo)
  if nombre_hoja in libro.sheetnames:
    del libro[nombre_hoja]
    libro.save(ruta_archivo)
