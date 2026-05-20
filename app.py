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

def vector_embedding():

    if "vector" not in st.session_state:
    
     st.session_state.embeddings= OpenAIEmbeddings()
     st.session_state.loader= PyPDFDirectoryLoader("./Data") ##Data Ingestion
     st.session_state.docs=st.session_state.loader.load() ##Document Loading
     st.session_state.text_splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) ##Chunk Creation
     st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs) ##Splitting
     st.session_state.vector= FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings) ##vector openai embeddings




prompt1= st.text_input("Enter your question from documents")

if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector Store DB is Ready")

import time

document_chain= create_stuff_documents_chain(llm,prompt)
retriever= st.session_state.vectors.as_retriever()
retrieval_chain=create_retrieval_chain(retriever, document_chain)

if prompt1:
   start=time.process_time()
   response= retrieval_chain.invoke({'input':prompt1})
   print("Response time:",time.process_time()-start)
   st.write(response['answer'])

   # with a streamlit expander
   with st.expander("Document Similarity Search"):
      # find the relevant chunks
      for i , doc in enumerate(response["context"]):
         st.write(doc.page_content)
         st.write("-----------------------")


