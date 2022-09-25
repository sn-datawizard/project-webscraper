import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymongo as pym

def request(x):
	url = x
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
	response = requests.get(url, headers=headers)
	print(response.status_code)
	print(url)
	return BeautifulSoup(response.content, "html.parser")


def upload(x,y):
	client = pym.MongoClient("mongodb+srv://<user>:<password>@<cluster>/database?retryWrites=true&w=majority")
	db = client["database"]
	collection = db[f"{x}"]
	dictonary = pd.DataFrame.to_dict(y, orient="records")
	datadelete = collection.delete_many({})
	dataload = collection.insert_many(dictonary)


def merge(x, y):
	merged = pd.merge(x, y, how="left", on="Country")
	return merged
