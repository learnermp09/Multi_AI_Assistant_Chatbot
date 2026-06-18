# https://aistudio.google.com/prompts/new_chat?model=gemini-3.5-flash
'''
https://docs.langchain.com/oss/python/integrations/chat/openai

'''
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class Question(BaseModel):
    question: str = Field(
        ...,
        title="User's Question",
        description="Please enter your prompt here",
        examples=["What is Python?"]
    )

prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are helpful AI assistant. Please respond to the user question in clear and concrete way'),
    ('user', 'question:{question}')
])

output_parser = StrOutputParser()

# groq
llm = ChatGroq(model='qwen/qwen3-32b', temperature=0.1)
chain1 = prompt | llm | output_parser
add_routes(app, chain1.with_types(input_type=Question), path='/chatgroq')

# openai
llm = ChatOpenAI(model='gpt-4o', temperature=0.1)
chain2 = prompt | llm | output_parser
add_routes(app, chain2.with_types(input_type=Question), path='/chatopenai')

# gemini
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.1)
chain3 = prompt | llm | output_parser
add_routes(app, chain3.with_types(input_type=Question), path='/chatgeminiai')