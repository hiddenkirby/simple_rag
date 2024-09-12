import chromadb
from functions import readtextfiles, chunksplitter, getembedding

# connect to the local chromadb on docker
chromaclient = chromadb.HttpClient(host="localhost", port=8000)
# local dir with test docs
textdocspath = "./test_data"

# read text files from the given path and return a dictionary with each file name as key and its content as value.
text_data = readtextfiles(textdocspath)

# wipe the collection by name and 
if any(collection.name == collection.name for collection in chromaclient.list_collections()):
  chromaclient.delete_collection("buildragwithpython")

# create a collection with the given name
collection = chromaclient.get_or_create_collection(name="buildragwithpython", metadata={"hnsw:space": "cosine"}  )

# loop over the text data and add each chunk to the collection
for filename, text in text_data.items():
  # split the text into chunks and return a list of chunk texts
  # set the chunk size to 200
  chunks = chunksplitter(text, 200)
  # get the embedding of each chunk and return a list with all embeddings
  embeds = getembedding(chunks)
  # create a list of chunk ids and return the list
  chunknumber = list(range(len(chunks)))
  ids = [filename + str(index) for index in chunknumber]
  metadatas = [{"source": filename} for index in chunknumber]
  # add the chunks to the collection
  collection.add(ids=ids, documents=chunks, embeddings=embeds, metadatas=metadatas)
