import pandas as pd
import pickle
import pdfplumber
from .base import ArchivoBase

class Importador(ArchivoBase):
  def pickle(self):
    with open(self.ruta_archivo, "rb") as archivo:
      return pickle.load(archivo)

  def excel(self, **kwargs):
    return pd.read_excel(self.ruta_archivo, **kwargs)

  def csv(self,**kwargs):
    return pd.read_csv(self.ruta_archivo, **kwargs)

  def pdf(self, type='table', n_pages='all', table_settings=None):
    """
    Extrae tablas o texto desde un archivo PDF usando pdfplumber.

    Parámetros:
    - type: 'table' para tablas o 'text' para texto plano
    - n_pages: 'all' o lista de páginas (base 1)
    - table_settings: configuraciones opcionales para detección de tablas

    Retorna:
    - Si type='table': lista de DataFrames, uno por cada tabla encontrada
    - Si type='text' : lista de strings, uno por cada página
    """
    information = []

    with pdfplumber.open(self.ruta_archivo) as pdf:
      pages = pdf.pages if n_pages == 'all' else [pdf.pages[p] for p in n_pages]

      for page in pages:
        if type == 'table':
          extracted = page.extract_tables(table_settings=table_settings)
          for tabla in extracted:
            df = pd.DataFrame(tabla[1:], columns=tabla[0])
            information.append(df)
        elif type == 'text':
          text = page.extract_text()
          information.append(text)
        else:
          raise ValueError("El parámetro 'type' debe ser 'table' o 'text'.")

    return information
