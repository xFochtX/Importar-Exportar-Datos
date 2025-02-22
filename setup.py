from setuptools import setup, find_packages

setup(
    name="ImportarExportarDatos",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl"
    ],
    author="Focht",
    description="Un paquete para importar y exportar datos en Excel y pickle",
    author_email="fabian.chipana@unmsm.edu.pe",  # Agregar un correo
    url="https://github.com/xFochtX/Importar-Exportar-Datos.git",  # URL del repositorio de GitHub
)
