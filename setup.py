from setuptools import setup, find_packages

setup(
    name="importar_exportar",
    version="2.2.6",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "openpyxl",
        "chardet",
        "pdfplumber",
        "geopandas"
    ],
    author="Focht",
    author_email="fabian.chipana@unmsm.edu.pe",
    description="Librería para importar y exportar datos en Excel, CSV, Pickle, PDF y formatos geoespaciales.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xFochtX/Importar-Exportar-Datos.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    include_package_data=True,
)