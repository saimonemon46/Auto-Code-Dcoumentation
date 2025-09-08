from pathlib import Path
from typing import List

from langchain_community.document_loaders import PythonLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


from .config import settings



# load and split ---> read python file and split into chunks

def load_and_store(paths : List[Path]):
    docs = []
    
    for p in paths:
        if p.suffix.lower() == ".py":
            loader = PythonLoader(str(p))
            docs.extend(loader.load())
            
    splitter = RecursiveCharacterTextSplitter(
        chunk_size  = 800,
        chunk_overlap = 100,
        add_start_index = True
    )
    
    docs = splitter.split_documents(docs)
    
    ## id docs empty
    if not docs:
        raise ValueError("No text extracted from the Python file. Check your files.")

    print(f"[INFO] Loaded {len(docs)} dcoument chunks from Python file.")
    return docs



## Embedding for vector store
def get_embedding():
    return HuggingFaceEmbeddings(model_name = settings.EMBEDDING_MODEL)

### Create a new faiss index
def persist_faiss(docs):
    embeddings = get_embedding()
    vs = FAISS.from_documents(docs, embeddings)
    FAISS.save_local(vs, str(settings.INDEX_DIR))
    
# check if faiss index available. if not call persist faiss to create one
def upsert_faiss(docs):
    embeddings = get_embedding()
    
    index_path = settings.INDEX_DIR 
    
    # if faiss index available ---> update 
    if(index_path / "index.faiss").exists() and (index_path / "index.pkl").exists():
        vs = FAISS.load_local(str(index_path), embeddings, allow_dangerous_deserialization=True)
        vs.add_documents(docs)
        FAISS.save_local(vs, str(index_path))
    else:
        # not present --> create
        persist_faiss(docs)
        
        
        
        
## Retrieve 
def get_retriever():
    embedding = get_embedding()
    
    vs = FAISS.load_local(str(settings.INDEX_DIR), embedding, allow_dangerous_deserialization=True)
    return vs.as_retriever(search_kwargs = {"k" : 4})