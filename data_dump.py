from pymongo import MongoClient
import pandas as pd 
import pymongo
import json

uri= "mongodb+srv://sekar:sekar1234@cluster0.ftumn94.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


DATA_FILE_PATH=(r"/Users/vallirajasekar/Desktop/Shipment_Price_prediction/shipmentprice_prediction/DATA/train.csv")
DATABASE='ML'
COLLECTION_NAME='DATASET'

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns of our Data:{df.shape}")
    
    # convert dataframe to the list of dictionaries (JSON RECORDS)
    json_records=json.loads(df.to_json(orient="records"))
    print(json_records[0])
    
    client=pymongo.MongoClient(uri)
    db=client[DATABASE]
    collection=db[COLLECTION_NAME]
    collection.insert_many(json_records)
    client.close()