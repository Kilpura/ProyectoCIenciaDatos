import pandas as pd

def abrir_csv(path, **kwargs):
    '''
    Args:
        path (str): Path relativo al archivo csv
    Returns:
        DataFrame
    '''
    df = pd.read_csv(path)
    return df

def guardar_en_excel(df_filtrado, nombre_archivo):
    '''
    Args:
        df_filtrado: DataFrame con las columnas filtradas
        nombre_archivo (str): nombre del archivo de salida en excel
    '''

    df_filtrado.to_excel(nombre_archivo, index=False)

def guardar_en_csv(df_filtrado, nombre_archivo):
    '''
    Args:
        df_filtrado: DataFrame con las columnas filtradas
        nombre_archivo (str): nombre del archivo de salida en csv
    '''

    df_filtrado.to_csv(nombre_archivo, index=False)