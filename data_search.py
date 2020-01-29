from elasticsearch import Elasticsearch
import clipboard
import json

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

print(es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}}))
clipboard.copy(json.dumps(es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})))