# ImportarExportarDatos

## Descripción
**ImportarExportarDatos** es un paquete de Python que facilita la importación y exportación de datos en formatos Excel y Pickle.  
Incluye funciones para configurar formatos en archivos Excel como fechas, anchos de columna y alineación.

## Instalación

### Instalación local desde el repositorio
Si tienes el repositorio clonado en tu equipo, navega a la carpeta del proyecto y ejecuta:
```bash
pip install -e .
```

### Instalación desde GitHub
Si el paquete está en GitHub, puedes instalarlo directamente con:
```bash
pip install git+https://github.com/usuario/ImportarExportarDatos.git --upgrade
```

## Uso

### Importar el paquete en tu código
```python
from importar_exportar import ImportarExportarDatos, exportar_excel
```

### Uso de la clase
```python
ie = ImportarExportarDatos("datos", "archivo.xlsx")
df = ie.importar_excel()
ie.exportar_excel(df, sheet_name="Hoja1")
```

### Uso de la función directa
```python
exportar_excel("datos", "archivo.xlsx", df, sheet_name="Hoja1")
```

## Requisitos
- Python 3.7+
- pandas
- openpyxl

## Autores
- Focht

