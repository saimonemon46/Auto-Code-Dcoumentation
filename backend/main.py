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
from .retrieve import get_retriever
from .llm import get_chat_model



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



### Generate Structured code documentation ## 
@app.post("/generate_docs")
def generate_docs():
    retriever = get_retriever() #loads the FAISS index and returns a retriever object (top-k retrieval).
    model = get_chat_model()#return your LLM wrapper (Ollama/OpenAI/whatever you use).
    
    prompt = ChatPromptTemplate.from_template(
        """
        You are an AI assistant that generates structured documentation for python code.
        Use ONLY the retrieved context ( uploaded code ).
        
        Output format:
        - **Module Summary**
        - **Classes** (with methods & purpose)
        - **Functions** (inputs, outputs, purpose)
        - **Usage Example** (if available)

    
        Context:{context}            
        
        """
    )
    
    # '''format_docs is a helper function to turn retrieved Document objects into a single text string for the LLM.'''
    def format_docs(docs):
        return "\n\n".join([f"[{d.metadata.get('source', '?')}] {d.page_content}" for d in docs])



    # The input to the pipeline is a dict with a context key.
    # retriever | format_docs means: run the retriever 
    # Effectively: retriever -> format_docs -> prompt -> model.
    chain = (
        {"context" : retriever | format_docs}
        | prompt
        | model
    )
    
    
    answer = chain.invoke("")
    content = getattr(answer, "content", str(answer))
    return {"documentation":content}

