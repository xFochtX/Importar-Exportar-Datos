import pandas as pd
import pickle
from .base import ArchivoBase
from .helpers import crear_carpeta_si_no_existe, eliminar_hoja
from .config_export_excel import exportar_con_plantilla

class Exportador(ArchivoBase):
  def pickle(self, objeto):
    crear_carpeta_si_no_existe(self.carpeta)
    with open(self.ruta_archivo, "wb") as archivo:
      pickle.dump(objeto, archivo)

  def excel(self, dataframe, sheet_name, rewrite=False, ruta_formato_plantilla=None, **kwargs):
    crear_carpeta_si_no_existe(self.carpeta)

    if rewrite and not self.ruta_archivo.exists():
      with pd.ExcelWriter(self.ruta_archivo, engine='openpyxl', mode='w') as writer:
        pd.DataFrame().to_excel(writer, sheet_name='EmptySheet')

    options = {"mode": "a", "if_sheet_exists": "replace"} if rewrite else {"mode": "w"}

    if ruta_formato_plantilla:
      exportar_con_plantilla(dataframe, ruta_formato_plantilla, self.ruta_archivo, sheet_name)
    else:
      with pd.ExcelWriter(self.ruta_archivo, engine='openpyxl', **options) as writer:
        dataframe.to_excel(writer, sheet_name=sheet_name, **kwargs)

    if rewrite:
      eliminar_hoja(self.ruta_archivo, 'EmptySheet')
