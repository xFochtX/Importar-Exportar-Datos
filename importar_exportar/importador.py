import pandas as pd
import pickle
from .base import ArchivoBase

class Importador(ArchivoBase):
  def pickle(self):
    with open(self.ruta_archivo, "rb") as archivo:
      return pickle.load(archivo)

  def excel(self, **kwargs):
    return pd.read_excel(self.ruta_archivo, **kwargs)
