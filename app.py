import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader

from dotenv import load_dotenv

load_dotenv()

## load the groq and openai api key
openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv('GROQ_API_KEY')

st.title("RagBot with Llama3")

llm=ChatGroq(model="Llama3-8b-8192")

prompt=ChatPromptTemplate.from_template(
"""
Answer the question based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
</context>
Question: {input}

"""    
)
