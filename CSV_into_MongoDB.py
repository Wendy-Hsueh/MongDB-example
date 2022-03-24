from pymongo import MongoClient
import pandas as pd
import datetime
import time, jieba

_client = MongoClient('localhost:27017',username='KddEoc414o6',password='eS414o6kdd',authMechanism='MONGODB-CR')
_db = _client.eoc
_Citys = _db.Citys


countrys = pd.read_csv('./f1452156319799.csv')

for name in countrys['中文名稱']:
	_Citys.insert_one({'city':'Country', 'district': name})

_client.close()