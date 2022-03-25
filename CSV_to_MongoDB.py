from pymongo import MongoClient
import pandas as pd
import datetime
import time, jieba

_client = MongoClient('localhost',username='Your_username',password='Your_password',authMechanism='MONGODB-CR')
_db = _client.Your_db_name
_Citys = _db.Your_table_name

countrys = pd.read_csv('./f1452156319799.csv')

for name in countrys['中文名稱']:
	_Citys.insert_one({'city':'Country', 'district': name})

_client.close()
