from pathlib import Path
from openpyxl import load_workbook

def ensure_folder(carpeta: Path):
  carpeta.mkdir(parents=True, exist_ok=True)

def delete_sheet(ruta_archivo, nombre_hoja):
  libro = load_workbook(ruta_archivo)
  if nombre_hoja in libro.sheetnames:
    del libro[nombre_hoja]
    libro.save(ruta_archivo)
