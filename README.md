# RAG-Based PDF Chatbot with LangChain, Llama 3 and Groq API

This repository implements a retrieval-augmented generation (RAG) chatbot for PDF documents using Streamlit, LangChain, Groq, and Hugging Face embeddings.

## What this app does

- Loads PDF files from the `Data/` folder
- Splits documents into chunks for retrieval
- Builds a FAISS vector store using sentence-transformers embeddings
- Uses Groq's `llama-3.1-8b-instant` model via `langchain_groq`
- Answers questions from the uploaded PDF content with a Streamlit interface

## Key improvements in this branch

- Updated imports to match the currently installed LangChain ecosystem
- Replaced obsolete `langchain.text_splitter` and `langchain.chains` imports with supported `langchain_classic` APIs
- Fixed retrieval logic so the app uses `retriever.get_relevant_documents(...)` and passes results into `create_stuff_documents_chain(...)`
- Added `GROQ_API_KEY` warning when not configured in `.env`

## Setup

1. Create a Python virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the following values:

```ini
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

4. Place PDF files in the `Data/` folder.

## Run the app

Use Streamlit to launch the app:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

## Notes

- The app currently uses `langchain_groq` for the Llama 3 model.
- Session state is required for vector loading in Streamlit, so run via `streamlit run` rather than `python app.py`.
- The current branch is intended as a patch to fix compatibility issues with the installed package versions.

## License

This repository is provided under the original project license.
