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
    Extrae tablas, texto o páginas completas desde un archivo PDF usando pdfplumber.

    Parámetros
    ----------
    type : str
        'table' para tablas,
        'text' para texto plano,
        'pdf' para retornar directamente las páginas sin procesar.
    n_pages : 'all' o list of int
        'all' para procesar todo el PDF, o lista de páginas (base 1).
    table_settings : dict, opcional
        Configuraciones para extracción de tablas.

    Retorna
    -------
    list
        - Si type='table': lista de DataFrames.
        - Si type='text' : lista de strings (uno por página).
        - Si type='page'  : lista de objetos Page (pdfplumber).
    """
    information = []

    with pdfplumber.open(self.ruta_archivo) as pdf:
      pages = pdf.pages if n_pages == 'all' else [pdf.pages[p] for p in n_pages]

      for page in pages:
        if type == 'page':
          information.append(page)
        elif type == 'table':
          extracted = page.extract_tables(table_settings=table_settings)
          for tabla in extracted:
            df = pd.DataFrame(tabla[1:], columns=tabla[0])
            information.append(df)
        elif type == 'text':
          text = page.extract_text()
          information.append(text)
        else:
          raise ValueError("El parámetro 'type' debe ser 'page', 'table' o 'text'.")

    return information
