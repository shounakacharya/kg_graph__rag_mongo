from openai import OpenAI
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)
load_dotenv()
<<<<<<< HEAD
open_ai_key = os.getenv("OPENAI_API_KEY1")
print(f"----OpenAI Key in find chunks is {open_ai_key}")
openai_client = OpenAI(api_key=open_ai_key)


'''
=======
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

>>>>>>> e8e0a41 (After adding all Python Codes and JS Codes)
@retry(wait=wait_random_exponential(min=1, max=1), stop=stop_after_attempt(6))
def chat_completion_backoff(**kwargs):
    return openai_client.chat.completions.create(**kwargs)

@retry(wait=wait_random_exponential(min=1, max=1), stop=stop_after_attempt(6))
def embedding_create_backoff(**kwargs):
    return openai_client.embeddings.create(**kwargs)
<<<<<<< HEAD
'''
=======
>>>>>>> e8e0a41 (After adding all Python Codes and JS Codes)

def find_chunks(question):
    docs = []
    min_chunk_size = 500
    max_chunk_size = 2000
    delimiter = '. '
    #openai_client = OpenAI()

    k = 3
    multiplier = 10

<<<<<<< HEAD
#    embeddings = embedding_create_backoff(
#                    input=question,
#                    model="text-embedding-ada-002"
#                )

    embeddings = openai_client.embeddings.create(
                    input=question,
                    model="text-embedding-ada-002"
                )
=======
    embeddings = embedding_create_backoff(
                    input=question,
                    model="text-embedding-ada-002"
                )

>>>>>>> e8e0a41 (After adding all Python Codes and JS Codes)
    query_vector = embeddings.data[0].embedding

    agg_pipeline = [
                {
                "$vectorSearch": {
                    "index":'vector_index',
                    "path": "embedding",
                    "queryVector": query_vector,
                    "limit": k,
                    "numCandidates": k * multiplier,
                    },
                },
                {
                "$project": {"embedding": 0} 
                }
    ]

    tag_docs = []

    try:
        uri = os.getenv("ATLAS_CONNECTION_STRING")
        client = MongoClient(uri)
        database = client["langchain_db"]
        collection = database["knowledge_graph"]
        cursor = collection.aggregate(agg_pipeline)
        for tag in cursor:
            tag_docs.append(tag)
    except Exception as e:
        print(e)
    finally:
        client.close()
    return tag_docs