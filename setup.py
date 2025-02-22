from setuptools import setup, find_packages

setup(
    name="ImportarExportarDatos",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl"
    ],
    author="F",
    description="Un paquete para importar y exportar datos en Excel y pickle",
)
