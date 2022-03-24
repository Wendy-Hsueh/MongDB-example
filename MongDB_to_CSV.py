from pymongo import MongoClient
# import pandas as pd
import datetime, csv, codecs
import time, jieba

_client = MongoClient('localhost:27017',username='Your_username',password='Your_password',authMechanism='MONGODB-CR')
_db = _client..Your_db_name
_message = _db..Your_table_name

i = 0
cursor = _message.find()
with codecs.open('data.csv', 'w', 'utf-8-sig') as outputfile:
	writer = csv.writer(outputfile)
	writer.writerow(['title', 'content', 'time'])
	for data in cursor:
		writer.writerow([data['title'], data['content'], data['datetime']])
		i+=1
		if i == 200:
			break

_client.close()
