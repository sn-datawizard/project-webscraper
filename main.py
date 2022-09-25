import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymongo as pym
import pyodbc
import sqlalchemy

def request(x):
	url = x
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
	response = requests.get(url, headers=headers)
	print(response.status_code)
	print(url)
	return BeautifulSoup(response.content, "html.parser")


def upload(x,y):
	client = pym.MongoClient("mongodb+srv://admin:superadmin@cluster0llc.chzx6.mongodb.net/database?retryWrites=true&w=majority")
	db = client["database"]
	collection = db[f"{x}"]
	dictonary = pd.DataFrame.to_dict(y, orient="records")
	datadelete = collection.delete_many({})
	dataload = collection.insert_many(dictonary)


def merge(x, y):
	merged = pd.merge(x, y, how="left", on="Country")
	return merged

"""
def export(x):
	client = pym.MongoClient("mongodb+srv://admin:superadmin@cluster0llc.chzx6.mongodb.net/database?retryWrites=true&w=majority")
	db = client["database"]
	collection = db[f"{x}"]
	dataselect = collection.find({})
	return pd.DataFrame.from_dict(dataselect).drop("_id", axis=1)
"""

"""
def importsql(x):
	table = x
	engine = sqlalchemy.create_engine('mssql+pyodbc://sa:superadmin@DESKTOP-FRFT9OU/lcc?driver=SQL+Server+Native+Client+11.0')
	#engine = sqlalchemy.create_engine('mssql+pyodbc://sa:superadmin@172.28.128.1,1433/lcc?driver=ODBC+Driver+18+for+SQL+Server')
	df = export(x)
	return df.to_sql(table, engine, if_exists="replace", index=False)
"""