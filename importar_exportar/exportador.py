import pandas as pd
import pickle
from osgeo import ogr
from .base import ArchivoBase
from .helpers import ensure_folder, delete_sheet
from .config_export_excel import export_with_template

class Exportar(ArchivoBase):
  def pickle(self, objeto):
    ensure_folder(self.carpeta)
    with open(self.ruta_archivo, "wb") as archivo:
      pickle.dump(objeto, archivo)

  def excel(self, dataframe, sheet_name, rewrite=False, path_template=None, **kwargs):
    ensure_folder(self.carpeta)

    if rewrite and not self.ruta_archivo.exists():
      with pd.ExcelWriter(self.ruta_archivo, engine='openpyxl', mode='w') as writer:
        pd.DataFrame().to_excel(writer, sheet_name='EmptySheet')

    options = {"mode": "a", "if_sheet_exists": "replace"} if rewrite else {"mode": "w"}

    if path_template:
      export_with_template(dataframe, path_template, self.ruta_archivo, sheet_name)
    else:
      with pd.ExcelWriter(self.ruta_archivo, engine='openpyxl', **options) as writer:
        dataframe.to_excel(writer, sheet_name=sheet_name, index=False, **kwargs)

    if rewrite:
      delete_sheet(self.ruta_archivo, 'EmptySheet')
  
  def shapefile(self, gdf, columnas_hiperenlace=None):
    """
    Exporta el GeoDataFrame como Shapefile, permitiendo especificar una o varias columnas
    que se mantendrán como atributos (por ejemplo, hiperenlaces).

    Parámetros:
      gdf: GeoDataFrame a exportar.
      columnas_hiperenlace: str o lista de str, nombres de las columnas a mantener como atributos.
    """
    ensure_folder(self.carpeta)
    if columnas_hiperenlace is None:
      gdf.to_file(self.ruta_archivo, index=False)
    else:
      if isinstance(columnas_hiperenlace, str): # Asegura que sea lista
        columnas_hiperenlace = [columnas_hiperenlace]
      gdf.to_file(self.ruta_archivo, index=False, keep_attributes=columnas_hiperenlace)

  def kml(self, gdf, column_name=None):
    ensure_folder(self.carpeta)

    driver = ogr.GetDriverByName('KML')  # Obtener el driver KML
    data_source = driver.CreateDataSource(self.ruta_archivo)  # Crear el DataSource
    srs = None  # Definir el sistema de referencia si es necesario
    # Crear una nueva capa en el DataSource
    layer = data_source.CreateLayer(self.nombre_archivo, srs, ogr.wkbPoint)
    layer_defn = layer.GetLayerDefn()

    # Agregar atributos
    for field in gdf.columns:
      field_defn = ogr.FieldDefn(field, ogr.OFTString)
      layer.CreateField(field_defn)
    
    # Agregar geometrías
    for index, row in gdf.iterrows():
      feature = ogr.Feature(layer_defn)
      feature.SetGeometry(ogr.CreateGeometryFromWkt(row['geometry'].wkt))
      for field in gdf.columns:
        feature.SetField(field, str(row[field]))
      # Establecer el nombre visual
      if column_name and column_name in gdf.columns:
        feature.SetField('Name', str(row[column_name]))
      layer.CreateFeature(feature)
      feature = None
    # Cerrar el data source
    data_source = None


