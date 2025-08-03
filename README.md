# ImportarExportarDatos

## Descripción
**ImportarExportarDatos** es un paquete de Python que facilita la importación y exportación de datos en formatos Excel y Pickle.  
El paquete está estructurado en módulos orientados a objetos para una mayor flexibilidad y mantenibilidad.  
Incluye funciones para exportar con formatos predefinidos (fechas, anchos de columna, alineación) usando plantillas Excel.

## Instalación

### Instalación local desde el repositorio
Si tienes el repositorio clonado en tu equipo, navega a la carpeta del proyecto y ejecuta:
```bash
pip install -e .

### Instalación desde GitHub
Si el paquete está en GitHub, puedes instalarlo directamente con:
```bash
pip install git+https://github.com/usuario/ImportarExportarDatos.git --upgrade
```

## Uso

### Importar el paquete en tu código
```python
from importar_exportar import Importador, Exportador
```

### Uso por separado (Importador y Exportador)
```python
from importar_exportar import Importador, Exportador

importador = Importador("datos", "archivo.xlsx")
df = importador.excel()

exportador = Exportador("datos", "archivo.xlsx")
exportador.excel(df, sheet_name="Hoja1")
```

## Requisitos
- Python 3.7+
- pandas
- openpyxl

## Autores
- Focht

