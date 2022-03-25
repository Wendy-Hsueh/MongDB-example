from pymongo import MongoClient
# import pandas as pd
import datetime, csv, codecs
import time, jieba

_client = MongoClient('localhost:27017',username='Your_username',password='Your_password',authMechanism='MONGODB-CR')
_db = _client..Your_db_name
_message = _db..Your_table_name
timeRange = {'$gte': '2021-10-14 00:00', '$lt': '2021-10-15 12:00'}
cursor = _message.find({'datetime': timeRange}).sort('datetime', 1)

with codecs.open('data.csv', 'w', 'utf-8-sig') as outputfile:
	writer = csv.writer(outputfile)
	writer.writerow(['title', 'content', 'time'])
	for data in cursor:
    writer.writerow([data['title'], data['content'], data['datetime']])

_client.close()
