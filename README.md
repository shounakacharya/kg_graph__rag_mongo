# kg_graph__rag_mongo
<<<<<<< HEAD
<<<<<<< HEAD
Test
=======
Test
>>>>>>> 43d628c (Changes to readme)
=======
This guide explores how to leverage MongoDB's capabilities to create and manipulate graph representations using both Python and Node.js. By utilizing these two popular programming languages, we can demonstrate the versatility of MongoDB in different development environments, showcasing how to perform essential Graph RAG to represent and analyze graphs can provide valuable insights into complex relationships and interactions within data combining the Graph and RAG data in MongoDB. 


Prep Steps
1. Set Up Your MongoDB Database:

    Set up a Atlas cloud-based MongoDB instance of MongoDB. (https://www.mongodb.com/docs/atlas/tutorial/create-new-cluster/)

2. Install Required Libraries:
    For Python: 
    You can setup a conda environment using the doc for running the python code (https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) 
                                                OR
    You can do a pip install <required-packages>
    For Node.js: 
    For the Node JS files we have a package.json and you will be able to use npm install to install all the packages needed.

    OPENAI_API_KEY1=
    ATLAS_CONNECTION_STRING=
    PDF = 

3. Vectorise the documents and store in MongoDB:
    Provide - ATLAS_CONNECTION_STRING and OPENAI_API_KEY in the environment file or the js file.
    Run node addEmbeddings.js to generate the embeddings with your PDF files.
    This will generate vector embeddings in you Mongodb Atlas (rename the collections as per your requirement).

4. Create vector index on the Atlas UI.
    Once the data is updated we need to create the vector indexes on the Atlas or using Compass.
    Sample: 
    {
        "fields": [ {
            "type": "vector",
            "path": "plot_embedding",
            "numDimensions": 1536,
            "similarity": "euclidean"
        } ]
    }
    https://www.mongodb.com/docs/compass/current/indexes/create-vector-search-index/#:~:text=You%20can%20create%20Atlas%20Vector,identifying%20the%20most%20similar%20vectors.

5. Run the python file to update nodes Shounak to update.

6. Once we have both the collections one with the RAG data and the nodes and relationship data we run node addTags.js in order
   to add the tags back to the collection with the vector embeddings.

Running the application

1. Run driver_code.py
    
>>>>>>> 6447527 (update the readme)
