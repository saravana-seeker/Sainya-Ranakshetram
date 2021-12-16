import os
import sys
import elasticsearch
from elasticsearch import Elasticsearch, helpers
import pandas as pd
import json

es = None
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def connect_elasticsearch():
    if es.ping():
        print('Connected ..! ')
    else:
        print(' it could not connect!')
    return es

# creating a index if its not created


def create_index():
    es.indices.create(index='armysearch', ignore=400)
    print("index created..!")


def all_index():
    res = es.indices.get_alias("*")
    for Name in res:
        print(Name)


# deleting index
#es.indices.delete(index=index-Name, ignore=[400, 404])

# read a csv file
# def read_csv_file():
df = pd.read_csv('armysearch.csv')
print(df.head(2))
df.head(2)
print(df.columns)
df2 = df.to_dict('records')
print(df2[0])


def generator(df2):
    for c, line in enumerate(df2):
        yield {
            '_index': 'armysearch',
            '_type': '_doc',
            '_id': line.get('s.no'),
            '_source': {
                'topic': line.get('topic', ""),
                'title': line.get('title', ""),
                'url': line.get('url', ""),
            }
        }


value_to_pass = generator(df2)
print(value_to_pass)
# gen_value=next(value_to_pass)
data = json.dumps(next(value_to_pass), indent=3)
print(data)

try:
    res = helpers.bulk(es, generator(df2))
    print("Fine Uploaded...!")
except Excepting as e:
    pass


# calling the functions
create_index()
connected = connect_elasticsearch()

# all_index()
# read_csv_file()
