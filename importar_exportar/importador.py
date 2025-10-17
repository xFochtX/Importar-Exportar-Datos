import pandas as pd
import pickle
import pdfplumber
import chardet
from .base import ArchivoBase

class Importar(ArchivoBase):
  def pickle(self):
    with open(self.ruta_archivo, "rb") as archivo:
      return pickle.load(archivo)

  def excel(self, **kwargs):
    return pd.read_excel(self.ruta_archivo, **kwargs)

  def csv(self,**kwargs):
    # ✅ Solo detectar encoding si el usuario no lo proporciona
    if 'encoding' not in kwargs:
      with open(self.ruta_archivo, 'rb') as f:
        result = chardet.detect(f.read(50000))
        encoding_detected = result['encoding'] or 'utf-8'
      kwargs['encoding'] = encoding_detected
    # 📥 Leer el archivo CSV con el encoding correspondiente
    return pd.read_csv(self.ruta_archivo, **kwargs)


  def pdf(self, type='table', n_pages='all', table_settings=None):
    """
    Extrae tablas, texto o páginas completas desde un archivo PDF usando pdfplumber.

    Parámetros
    ----------
    type : str
        'table' para tablas,
        'text' para texto plano,
        'page' para retornar directamente las páginas sin procesar.
    n_pages : 'all' o list of int
        'all' para procesar todo el PDF, o lista de páginas (base 1).
    table_settings : dict, opcional
        Configuraciones para extracción de tablas.

    Retorna
    -------
    Tuple (number_pages, information)
    - number_pages: lista de enteros (número de página base 1)
    Si type='page':
      - information: lista de objetos Page (pdfplumber)
    Si type='table':
      - information: lista de DataFrames
    Si type='text':
      - information: lista de strings, uno por cada página
    """
    number_pages = []
    information = []


    with pdfplumber.open(self.ruta_archivo) as pdf:
      pages = pdf.pages if n_pages == 'all' else [pdf.pages[p - 1] for p in n_pages]  # base 1

      for page in pages:
        page_number = page.page_number  # pdfplumber uses base-1 internally
        if type == 'page':
          number_pages.append(page_number)
          information.append(page)
        elif type == 'table':
          extracted = page.extract_tables(table_settings=table_settings)
          for tabla in extracted:
            df = pd.DataFrame(tabla[1:], columns=tabla[0])
            number_pages.append(page_number)
            information.append(df)
        elif type == 'text':
          text = page.extract_text()
          number_pages.append(page_number)
          information.append(text)
        else:
          raise ValueError("El parámetro 'type' debe ser 'page', 'table' o 'text'.")

    return number_pages, information
