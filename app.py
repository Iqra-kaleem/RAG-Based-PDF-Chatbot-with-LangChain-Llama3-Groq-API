import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader

from dotenv import load_dotenv

load_dotenv()

## load the groq and openai api key
openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv('GROQ_API_KEY')

st.title("RagBot with Llama3")

if not groq_api_key:
    st.warning("GROQ_API_KEY is not set. Add it to .env and restart the app.")

llm = ChatGroq(model="llama-3.1-8b-instant", api_key=groq_api_key)

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

    if "vectors" not in st.session_state:
    
     st.session_state.embeddings= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") ##Embeddings
     st.session_state.loader= PyPDFDirectoryLoader("./Data") ##Data Ingestion
     st.session_state.docs=st.session_state.loader.load() ##Document Loading
     st.session_state.text_splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) ##Chunk Creation
     st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs) ##Splitting
     st.session_state.vectors= FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings) ##vector openai embeddings




prompt1= st.text_input("Enter your question from documents")

if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector Store DB is Ready")

import time

if "vectors" in st.session_state:
        document_chain = create_stuff_documents_chain(llm, prompt)
        retriever = st.session_state.vectors.as_retriever()

        if prompt1:
            start = time.process_time()
            docs = retriever.get_relevant_documents(prompt1)
            response = document_chain.invoke({"context": docs, "input": prompt1})
            print("Response time:", time.process_time() - start)
            st.write(response)

            with st.expander("Document Similarity Search"):
                for i, doc in enumerate(docs):
                    st.write(doc.page_content)
                    st.write("-----------------------")

