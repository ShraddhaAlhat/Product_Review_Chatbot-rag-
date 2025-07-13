import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
from pathlib import Path

# Import all required LangChain components
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from Retriever.retrieval import Retriever
from utils.model_loader import ModelLoader
from prompt_library.prompt import PROMPT_TEMPLATES

app = FastAPI()

# Configure paths
BASE_DIR = Path(__file__).parent
static_dir = BASE_DIR / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Configure templates
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

# Initialize components
retriever_obj = Retriever()
model_loader = ModelLoader()

def invoke_chain(query: str):
    try:
        retriever = retriever_obj.load_retriever()
        llm = model_loader.load_llm()
        
        # Ensure the prompt template exists
        if "product_bot" not in PROMPT_TEMPLATES:
            raise ValueError("product_bot template not found in PROMPT_TEMPLATES")
            
        prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATES["product_bot"])
        
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        
        return chain.invoke(query)
    except Exception as e:
        print(f"Error in invoke_chain: {str(e)}")
        return f"Sorry, I encountered an error: {str(e)}"

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Render the chat interface."""
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/get")
async def chat(msg: str = Form(...)):
    try:
        print(f"Received message: {msg}")  # Debug log
        result = invoke_chain(msg)
        print(f"Response: {result}")  # Debug log
        return result
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return "Sorry, I'm having trouble processing your request. Please try again later."