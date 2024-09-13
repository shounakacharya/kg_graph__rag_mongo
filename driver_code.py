from langchain_core.documents import Document
from langchain_community.graphs.graph_document import GraphDocument, Node, Relationship
from pymongo import MongoClient
from pprint import pprint
import os
import json
from nodes_relationships import nodes,links
from data_insert import build_lookup_map, create_mongo_documents, mongo_insert



if __name__ == "__main()__":
    mongo_insert()
