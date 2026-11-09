import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de redes sociales con 4 elementos por lista
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# creamos una lista de listas (conformando la tabla)
lista_redes_sociales=[fb ,twt, ig, wsp, tel, lkn]
# print(lista_redes_sociales)
# utilizar pandapara organizar la tabla (dataframe)
# a cad columna le ponemos nombre
df_redes_sociales=pd.DataFrame(lista_redes_sociales,columns=["nombre","cantidad","Es_fb","año"])
print(df_redes_sociales)
# creamos el archivo CSV y lo guardamos en  CSV
df_redes_sociales.to_csv("redessociales.csv",index=False)
# crear grafica de lineas
# donde x es Nombre en el eje horizontal
# donde Y es candidad en el eje vertical
plt.plot(df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.title("grafica redes sociales 0070")
plt.xlabel("Nombe de las redes")
plt.ylabel("cantidad de usuarios")
plt.show()
# creamos una grafica de puntos
plt.scatter (df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
plt.show()
# Grafica de barras
plt.bar (df_redes_sociales["nombre"],df_redes_sociales["cantidad"])
# Añadir título y etiquetas a los ejes
plt.title("Redes sociales 0070")
plt.xlabel("las redes")
plt.ylabel("cantidad usuarios")
# Mostrar la gráfica
plt.show()
# ordenar la grafica de barras de manera descendente
# de la mas grande a la mas pequeña
df_rs_ordenar=df_redes_sociales.sort_values("cantidad",ascending=False)
plt.bar(df_rs_ordenar["nombre"],df_rs_ordenar["cantidad"])
plt.show()
# coloreando la grafica
df_rs_ordenar=df_redes_sociales.sort_values("cantidad",ascending=False)
plt.bar(df_rs_ordenar["nombre"],df_rs_ordenar["cantidad"],
        color=["b","g","c","m","y","r"])
plt.show()

# Grafica de pastel
# plt.plot(df_rs_ordenar["nombre"],df_redes_sociales["cantidad"])
plt.pie(df_redes_sociales["cantidad"],labels=df_redes_sociales["nombre"])
plt.show()