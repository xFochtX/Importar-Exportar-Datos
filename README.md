# ImportarExportarDatos

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.5.0-orange)

## Descripción

**ImportarExportarDatos** es un paquete de Python que facilita la importación y exportación de datos en formatos **Excel**, **CSV**, **Pickle**, **PDF** y formatos geoespaciales.  
Está estructurado en módulos orientados a objetos para mayor flexibilidad y mantenibilidad.  
Incluye funciones para exportar con formatos predefinidos (fechas, anchos de columna, alineación) usando plantillas Excel.

## Instalación

### Instalación local desde el repositorio

```bash
pip install -e .
```

### Instalación desde GitHub

```bash
pip install git+https://github.com/xFochtX/Importar-Exportar-Datos --upgrade
```

> **Nota:**  
> Si necesitas trabajar con datos geoespaciales, instala manualmente la librería `osgeo` siguiendo la [documentación oficial](https://pypi.org/project/GDAL/).

## Requisitos

- Python 3.10+
- pandas
- openpyxl
- pdfplumber
- geopandas
- (Opcional) osgeo

## Uso

### Importar el paquete en tu código

```python
from importar_exportar import Importar, Exportar
```

### Ejemplo de uso

```python
from importar_exportar import Importar, Exportar

# Importar datos desde Excel
importador = Importar("datos", "archivo.xlsx")
df = importador.excel()

# Exportar datos a Excel
exportador = Exportar("datos", "archivo.xlsx")
exportador.excel(df, sheet_name="Hoja1")
```

## Funcionalidades

- Importar y exportar datos en Excel, CSV, Pickle, PDF y formatos geoespaciales.
- Personalización de formatos en exportación (fechas, alineación, anchos de columna).
- Uso de plantillas Excel para exportación avanzada.
- Soporte para procesamiento de datos tabulares y espaciales.

## Contribuciones

¿Te gustaría mejorar este paquete?  
¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request.

## Autor

- **Focht**  
  [fabian.chipana@unmsm.edu.pe](mailto:fabian.chipana@unmsm.edu.pe)
