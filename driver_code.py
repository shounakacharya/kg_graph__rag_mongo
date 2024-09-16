from langchain_core.documents import Document
from langchain_community.graphs.graph_document import GraphDocument, Node, Relationship
from pymongo import MongoClient
from pprint import pprint
from nodes_relationships import nodes,links
from data_insert import build_lookup_map, create_mongo_documents, mongo_insert

from find_relevant_chunks import find_chunks, chat_completion_backoff
from do_graphlookup import graph_lookup
from build_graph import  build_graph
from depth_first_search import depth_first_search

if __name__ == "__main__":
    #mongo_insert()
    question = input("Please enter your question ")
    tree_depth = input("What is the maximum tree depth you require for Knowledge graph traversal? ")
    tag_docs = find_chunks(question)
    top_id_idx = 0
    top_tag_score = 0
    top_tag_idx = 0
    i=0
    for doc in tag_docs:
        j=0
        for tag in doc['tags']:
            if tag['score'] > top_tag_score:
                top_tag_score = tag['score']
                top_id_idx = i
                top_tag_idx=j
            j+=1
        i+=1
    print(top_id_idx,top_tag_idx,top_tag_score)
    node_name = tag_docs[top_id_idx]['tags'][top_tag_idx]['tagName']
    print(node_name)
    graph_lookup_docs = graph_lookup(node_name,int(tree_depth))
    level_dict = {}
    for graph_doc in graph_lookup_docs:
        rel_docs = graph_doc['relates_to']
        for rel_doc in rel_docs:
            level_key = rel_doc['distance']
            obj = level_dict.get(level_key,None)
            targets = rel_doc['targets']
            id = rel_doc['_id']
            inner_dict = {"targets":targets}
            if obj != None:
                level_dict[level_key][id] = inner_dict
            else:
                level_dict[level_key]={}
                level_dict[level_key][id] = inner_dict
    pprint(level_dict)
    graph,relationship_names = build_graph(level_dict)
    path,nodes,links = depth_first_search(graph,node_name,relationship_names,'')
    chunk = tag_docs[top_id_idx]['chunks']
    chunk = chunk + f"\n Entity Relationships: {path}"
    prompt = f'''
    You are a doctor who specialises in mental health and psychiatry. Please use the below context to answer {question}
    Please note that the below text has relationship between various entities written after the text Entity Relationships:
    The relationships are written in comma separated sentences with the relationship names between the entities written in brackets. There can be multiple
    entity names which are given by slashes. You can chose any of the names to answer the question. Please only answer the question based upon the relationships
    provided and context given and not from your own previous knowledge.
    '''
    response = chat_completion_backoff(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": prompt},
                            {"role": "user", "content": chunk},
                        ]
                    )
    print("-----------")
    print(response.choices[0].message.content)

