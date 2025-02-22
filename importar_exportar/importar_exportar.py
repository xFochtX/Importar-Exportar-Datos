import pandas as pd
import pickle
from pathlib import Path
from openpyxl import load_workbook
from configExportExcel import config_fecha, config_width_col, config_align_col

# Clase para importar y exportar datos
class ImportarExportarDatos():
  def __init__(self, carpeta, nombre_archivo):
    self.carpeta = Path(carpeta)
    self.nombre_archivo = nombre_archivo
    self.ruta_archivo = self.carpeta / self.nombre_archivo

  # Método que permite importar datos de objeto pickle
  def importar_pickle(self):
    with open(self.ruta_archivo, "rb") as archivo:  # Abre el archivo en modo binario
      base_datos_pickle = pickle.load(archivo)
    return base_datos_pickle

  # Método que permite importar datos de archivo excel
  def importar_excel(self,**kwargs):
    dataFrame = pd.read_excel(self.ruta_archivo, **kwargs)  # Usa ruta completa con pathlib
    return dataFrame

  # Método que permite exportar datos a objeto pickle
  def exportar_pickle(self, objeto):
    with open(self.ruta_archivo, "wb") as archivo:  # Usa el método `open` de `Path` para abrir el archivo en modo binario
      pickle.dump(objeto, archivo)

  # Método que permite exportar datos a archivo excel
  def exportar_excel(self, df, sheet_name, rewrite=False, col_fecha=None, width_col=None, align_col=None, **kwargs):
    """Exporta un DataFrame a una hoja específica de un archivo Excel."""
    self.carpeta.mkdir(parents=True, exist_ok=True)  # Asegurar que la carpeta existe

    mode = 'w' if rewrite else 'a'  # Modo de escritura ('w' = sobrescribir, 'a' = agregar)

    with pd.ExcelWriter(self.ruta_archivo, engine='openpyxl', mode=mode) as writer:
      df.to_excel(writer, sheet_name=sheet_name, **kwargs)

    # Aplicar configuraciones adicionales si están definidas
    if col_fecha or width_col or align_col:
      book = load_workbook(self.ruta_archivo)
      if col_fecha:
        config_fecha(book, col_fecha)
      if width_col:
        config_width_col(book, width_col)
      if align_col:
        config_align_col(book, align_col)
      book.save(self.ruta_archivo)




'''
  # Método que permite exportar datos a archivo excel
  def exportar_excel(self, data, nombre_hoja_excel, rewrite = False, col_fecha = None, width_col = None, align_col = None, **kwargs):
    if isinstance(data, pd.DataFrame):
      if rewrite:
        try:
          # Intentar cargar el libro existente
          book = load_workbook(self.ruta_archivo)
          # Eliminar la hoja si ya existe
          if self.nombre_archivo in book.sheetnames:
            sheet = book[nombre_hoja_excel]
            book.remove(sheet)
          # Crear una nueva hoja con el DataFrame
          with pd.ExcelWriter(self.ruta_archivo, engine='openpyxl', mode='a') as writer: # Mode append
            #writer.book = book
            data.to_excel(writer, sheet_name=nombre_hoja_excel, **kwargs)
            sheet = writer.sheets[nombre_hoja_excel]
        except FileNotFoundError: # Si el archivo no existe, crear un nuevo libro
          with pd.ExcelWriter(self.ruta_archivo, engine='openpyxl') as writer:
            data.to_excel(writer, sheet_name=nombre_hoja_excel, **kwargs)
      else:
        # Exportando el dataframe a archivo excel
        with pd.ExcelWriter(self.ruta_archivo) as writer:
          data.to_excel(writer, sheet_name=nombre_hoja_excel, **kwargs)
    elif isinstance(data, dict):
      with pd.ExcelWriter(self.ruta_archivo, engine='xlsxwriter', mode='w') as writer:
        for sheet, df in data.items():
          df.to_excel(writer, sheet_name=sheet, **kwargs)
        del writer
    else:
      print('Los datos son de un tipo que no se puede exportar a excel')
    # Realizando configuraciones específicas
    if col_fecha or width_col or align_col:
      book = load_workbook(self.ruta_archivo)
      if col_fecha:
        config_fecha(book, col_fecha)
      if width_col:
        config_width_col(book, width_col)
      if align_col:
        config_align_col(book, align_col)
      book.save(self.ruta_archivo)

'''