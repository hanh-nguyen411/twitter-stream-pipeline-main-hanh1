from mongo_config import DB_NAME, MONGO_DB_URL, COLLECTION_NAME
import pymongo
import pandas as pd

myclient = pymongo.MongoClient(MONGO_DB_URL)
mydb = myclient[DB_NAME]
mycol = mydb[COLLECTION_NAME]
items = mycol.find()

items_df = pd.DataFrame(items)
print(items_df)

items_df.to_csv('test.csv', header=False, index=False)
