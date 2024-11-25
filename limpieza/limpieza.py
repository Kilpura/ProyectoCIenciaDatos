import funciones
import os

path_excel_original = os.path.join('datos_originales.xlsx')

df = funciones.abrir_excel(path_excel_original)
df_filtrado = funciones.eliminar_columnas(df)

#guardado en excel

funciones.guardar_en_excel(df_filtrado, 'datos_filtrados.xlsx')

#guardado en csv

funciones.guardar_en_csv(df_filtrado, 'datos_filtrados.csv')

