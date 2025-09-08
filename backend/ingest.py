from pathlib import Path
from .config import settings
from .retrieve import load_and_store, upsert_faiss


def ingest_all():
    # find the python file from directory
    upload_dir : Path = settings.UPLOAD_DIR
    
    py_file = [p for p in upload_dir.glob("**/*") if p.suffix.lower() == ".py"]
    
    if not py_file:
        return {"added" : 0, "message" : "No python file found in uploaded folder."}
    ## if file found
    docs = load_and_store(py_file) # send file for chunkind and embedding
    upsert_faiss(docs) # vector store
    
    return {"added": len(docs), "files": [p.name for p in py_file]}
    