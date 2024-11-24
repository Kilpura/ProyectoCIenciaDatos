import pandas as pd

def abrir_excel(path):
    '''
    Args:
        path (str): Path relativo al archivo excel
    Returns:
        DataFrame
    '''
    df = pd.read_excel(path)
    return df

def eliminar_columnas(df):
    '''
    Args:
        df : DataFrame con todas las columnas
    Returns:
        DataFrame solo con las columnas esenciales
    '''

    columnas_esenciales = [
        'AÑO', 
        'TOTAL MATRICULADOS', 
        'MATRICULADOS MUJERES POR PROGRAMA', 
        'MATRICULADOS HOMBRES POR PROGRAMA',
        'TOTAL MATRICULADOS PRIMER AÑO', 
        'MATRICULADOS MUJERES PRIMER AÑO',
        'MATRICULADOS HOMBRES PRIMER AÑO', 
        'REGIÓN', 
        'PROVINCIA', 
        'COMUNA', 
        'NOMBRE CARRERA', 
        'ÁREA DEL CONOCIMIENTO', 
        'ÁREA CARRERA GENÉRICA'
    ]
    
    df_filtrado = df[columnas_esenciales]
    
    return df_filtrado

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