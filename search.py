import sys, chromadb, ollama

# connect to local chromadb running on docker
chromaclient = chromadb.HttpClient(host="localhost", port=8000)
# pull named collection
collection = chromaclient.get_or_create_collection(name="buildragwithpython")

# collect query from command line arg
query = " ".join(sys.argv[1:])
# get embeddings for query
queryembed = ollama.embed(model="nomic-embed-text", input=query)['embeddings']

# query the full chromadb collection with your query [embeddings]
relateddocs = '\n\n'.join(collection.query(query_embeddings=queryembed, n_results=10)['documents'][0])
# generate the full prompt for the LLM
prompt = f"{query} - Answer that question using the following text as a resource: {relateddocs}"

# get the answer without rag
noragoutput = ollama.generate(model="llama3.1", prompt=query, stream=False)
print(f"The Answer without RAG: \n{noragoutput['response']}")

print("---")

# get the answer using rag
ragoutput = ollama.generate(model="llama3.1", prompt=prompt, stream=False)
print(f"The Answer with RAG: \n{ragoutput['response']}")