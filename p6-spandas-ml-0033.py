# Keyla Paola NC = 0033 | Fecha 29/octubre/2026
import pandas as pd
import numpy as np

serie_amigos= ["Alonso","Catherine","Caleb","Pedro","Andres","Valeria","Arriaga"]
print(" -- serie instalado en amigos  -- NC =0033")
amigos = pd.Series(serie_amigos)
print(amigos)

print("  ")
serie_billetes=[20,50,100, 200, 500, 1000]
print(" -- serie instalado en billetes  -- NC =0033")
billetes = pd.Series(serie_billetes)
print(billetes)

# Diccionario DataFrame 
# Diccionario de valor monedas y nombre
print(" --- Datos de diccionario a DataFrame en Pandas --- NC = 0033")
dic_monedas = {
    "serie_Billetes":[20,50,100, 200, 500, 1000],
    "serie_bietras":["Veinte","Cincuenta","Cien","Docientos","Quinientos","Mil"]
}

tablabiletes = pd.DataFrame(dic_monedas, index= ["A","B","C","D","E","F"])
print(tablabiletes)
print(" Casa de Cambio de Keyla Paola NC = 0033")


print("   ")
serie_billetes=[20,50,100,200,500,1000]
serie_biletras=["Veinte","Cincuenta","Cien","Docientos","Quinientos","Mil"]
print(" -- serie listado nombre y valor de billetes MX -- NC =0033")
tabla_billetes = pd.Series(serie_billetes,serie_biletras)
print(tabla_billetes)
print("Keyla Paola NC = 0033 | Fecha 29/octubre/2026")