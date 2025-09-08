### Scan code files (Python, JS, etc.).

# Use RAG to fetch relevant examples or best practices from open-source repos.

# Generate structured documentation (functions, classes, modules, usage).

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


## file management
from .config import settings 
from .ingest import ingest_all



app = FastAPI()

## Middle ware 
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = True
)



@app.get("/")
def hello():
    return {"message" : "Welcome."}


## Upload python files
@app.post("/upload")
async def upload(files: List[UploadFile] = File(...)):
    saved_files = []
    for file in files:
        ## Check .py file or not
        if not file.filename.lower().endswith(".py"):
            raise HTTPException(status_code=400, detail="Invalid file type. only python code accepted.")
        # save the file in upload directory
        dest = settings.UPLOAD_DIR / file.filename
        
        with open(dest, "wb") as out_data:
            out_data.write(await file.read())
            
        saved_files.append(file.filename)
        
    return {"filename" : saved_files}




### ingest document
@app.post("/ingest")
def ingest():
    return ingest_all()







