"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import os
import pandas as pd


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    # Definir las rutas de entrada y salida
    input_path = "files/input/solicitudes_de_credito.csv"
    output_path = "files/output/solicitudes_de_credito.csv"
    # Verificar si el directorio de salida existe, si no, crearlo
    if not os.path.exists("files/output"):
        os.makedirs("files/output")

    df = pd.read_csv(input_path, sep=";", index_col=0)
    # Normalizar los nombres de las columnas
    df["sexo"] = df["sexo"].str.strip().str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.strip().str.lower()
    # Normalizar la columna "idea_negocio"
    df["idea_negocio"] = (
        df["idea_negocio"]
        .str.strip().str.lower()
        .str.replace("á", "a").str.replace("é", "e").str.replace("í", "i")
        .str.replace("ó", "o").str.replace("ú", "u")
        .str.replace(" ", "")
        .str.translate(str.maketrans("", "", "-._"))
    )
    # Normalizar la columna "barrio"
    df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")


    # Normalizar la columna "comuna_ciudadano"
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    # Normalizar la columna "fecha_de_beneficio"
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format="mixed")


    # Normalizar la columna "monto_del_credito"
    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.strip().str.strip("$")
        .str.replace(".00", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(int)
    )


    # Normalizar la columna "línea_credito"
    df["línea_credito"] = (
        df["línea_credito"]
        .str.strip()
        .str.lower()
        .str.replace(" ", "")
        .str.translate(str.maketrans("", "", "-._"))
    )


    # Eliminar registros con valores nulos en columnas clave
    df = df.dropna().drop_duplicates()


    df.to_csv(output_path, index=False, sep=";")


    # Retornar el DataFrame limpio
    return df



df2= pregunta_01()
print(df2.sexo.value_counts().to_list())