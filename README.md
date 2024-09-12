# simple rag

- search.py - main rag script
- functions.py - useful rag functions
- importdocs.py - imports any *.txt documents from the test_data/ directory into chroma

## developer setup

1.  create a test_data/ directory and place as many *.txt files in as you'd like
2.  run `docker run -d -p 8000:8000 -v chrome-data:/chromadb/data chromadb/chroma` to spin up chroma in a docker container daemon
3.  ensure Ollama is installed
4.  ensure llama3.1 is downloaded on Ollama
5.  run `python3 -m venv .venv`
6.  run `source .venv/bin/activate`
7.  run `pip install -U -r requirements.txt`
8.  run `python importdocs.py` to import any *.txt documents from the test_data/ directory into chroma
9.  run `python search.py "<query>"` to run RAG query against llama3.1 with relavent context from chroma.

## chromadb

Docs can be found http://localhost:8000/docs/
