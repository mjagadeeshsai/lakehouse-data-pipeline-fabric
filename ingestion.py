import pandas as pd
import numpy as np
import logging
import os

#Ensure Logs folder exists
os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/pipeline.log',level=logging.INFO)

try:
    logging.info('Ingestion started')

    #Read the dataset
    df=pd.read_csv(r"C:\Users\mjaga\PycharmProjects\FabricProject_pipeline\Data\Raw-Titanic-Dataset.csv")

    #Save to Bronze layer
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/raw.csv', index=False)

    print('Ingestion complete')
    logging.info(f'Rows: {df.shape[0]}')

except Exception as e:
    print('Error',e)
    logging.error(str(e))