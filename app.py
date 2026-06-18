from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "running",
        "service": "Multi AI Assistant API"
    }

class Question(BaseModel):
    question: str = Field(
        ...,
        title="User's Question",
        description="Please enter your prompt here",
        examples=["What is Python?"]
    )

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI assistant. Please respond to the user question in a clear and concrete way."
    ),
    (
        "user",
        "question:{question}"
    )
])

output_parser = StrOutputParser()

# --------------------------------------------------
# Groq
# --------------------------------------------------
llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0.1
)

chain1 = prompt | llm | output_parser

add_routes(
    app,
    chain1.with_types(input_type=Question),
    path="/chatgroq"
)

# --------------------------------------------------
# OpenAI
# --------------------------------------------------
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.1
)

chain2 = prompt | llm | output_parser

add_routes(
    app,
    chain2.with_types(input_type=Question),
    path="/chatopenai"
)

# --------------------------------------------------
# Gemini
# --------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.1
)

chain3 = prompt | llm | output_parser

add_routes(
    app,
    chain3.with_types(input_type=Question),
    path="/chatgeminiai"
)