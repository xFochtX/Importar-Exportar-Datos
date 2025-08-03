from setuptools import setup, find_packages

setup(
    name="ImportarExportarDatos",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl"
    ],
    author="Focht",
    description="Librería para importar y exportar datos en excel, csv y pickle",
    author_email="fabian.chipana@unmsm.edu.pe",
    url="https://github.com/xFochtX/Importar-Exportar-Datos.git",
)
