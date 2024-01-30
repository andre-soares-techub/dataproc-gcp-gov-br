from pyspark.sql import SparkSession
import unicodedata
import sys 
import pandas as pd
from functools import reduce
import pyspark.sql.functions as F
from pyspark.sql.types import StringType, DateType



GCS_DATA_SOURCE_PATH=sys.argv[1]
GCP_DATA_OUTPUT_PATH=sys.argv[2]
APP_NAME=sys.argv[3]
CHECK_RAW_PATH=sys.argv[4]

print('-------------------------------------------------------------------------')
print(f'GCS_DATA_SOURCE_PATH ===  {GCS_DATA_SOURCE_PATH}')
print(f'GCP_DATA_OUTPUT_PATH ===  {GCP_DATA_OUTPUT_PATH}')
print('-------------------------------------------------------------------------')

def print_info(message, df):
    print(f'{message} ---- Quantidade total de linhas {df.count()}')
    print(f'{message} ---- Colunas da tabela: {df.columns}')
    print(f'{message} ---- Amostras dos dados: {df.show()}')
    print(f'{message} ---- Schema: {df.printSchema()}')

def funcao_normalizar(texto):
    string_velha = str(texto) \
                .lower()\
                .replace(' ','_')\
                .replace('/','-')\
                .replace('"','') \
                .replace('ç','c')\
                .replace('á','a')\
                .replace('ã','a')\
                .replace('é','e')\
                .replace('í','i')\
                .replace('ó','o')\
                .replace('õ','o')\
                .replace('ú','u')
    try:
        string_nova = ''.join(ch for ch in unicodedata.normalize('NFKD', string_velha)
            if not unicodedata.combining(ch))
        return string_nova
    except:
        return string_velha


