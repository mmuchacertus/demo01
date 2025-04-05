# etl.py para procesar el archivo input.csv y generar el archivo output.csv
import pandas as pd

df = pd.read_csv('input.csv')
df['processed'] = df['value'] * 1000
df.to_csv('output4.csv', index=False)
print("ETL completado.")
