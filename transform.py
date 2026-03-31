import pandas as pd
import logging

logging.basicConfig(filename='logs/pipeline.log',level=logging.INFO)

try:
    logging.info('Transformation started')
    df=pd.read_csv(r"C:\Users\mjaga\PycharmProjects\FabricProject_pipeline\Scripts\data\raw.csv")

    #Validation
    assert df.shape[0] >0, "Dataset is emptpy"

    #Handle missing value
    df=df.dropna()

    #feature engineering
    df['FamilySize']=df['SibSp']+df['Parch']

# Encode categorical column
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

    # Save to Silver layer
    df.to_csv("data/clean.csv", index=False)

    print("Transformation done")

    logging.info(f"Rows after cleaning: {df.shape[0]}")

except Exception as e:
    print("Error:", e)
    logging.error(str(e))

