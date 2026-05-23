# 🤖 RAG-Based PDF Chatbot with LangChain, Llama3 & Groq API

An intelligent PDF chatbot application that lets users upload documents and interact with them through natural language conversations. Built with **Retrieval-Augmented Generation (RAG)**, it extracts relevant information from PDFs and delivers accurate, context-aware responses in real time — powered by Meta's **Llama 3** via the **Groq API**.

---

## ✨ Features

- 📄 **PDF Document Ingestion** — Load and process multiple PDFs from a local directory
- 🔍 **Semantic Search with FAISS** — Efficient similarity-based document retrieval using a vector store
- 🧠 **Llama 3 (via Groq)** — Ultra-fast LLM inference for context-aware Q&A
- 🔗 **LangChain RAG Pipeline** — End-to-end retrieval and generation chain
- 📐 **HuggingFace Embeddings** — Uses `sentence-transformers/all-MiniLM-L6-v2` for embedding documents
- 🖥️ **Streamlit UI** — Clean, interactive web interface for querying documents
- 🔎 **Document Similarity Expander** — See which document chunks were used to generate each answer

---

## 🏗️ Architecture

```
PDF Files (./Data)
      │
      ▼
PyPDFDirectoryLoader         ← Document Ingestion
      │
      ▼
RecursiveCharacterTextSplitter  ← Chunking (1000 chars, 200 overlap)
      │
      ▼
HuggingFace Embeddings       ← Vectorization (all-MiniLM-L6-v2)
      │
      ▼
FAISS Vector Store           ← Semantic Retrieval
      │
      ▼
LangChain Retrieval Chain    ← RAG Pipeline
      │
      ▼
Llama 3 via Groq API         ← LLM Response Generation
      │
      ▼
Streamlit UI                 ← User Interface
```

---

## 🗂️ Project Structure

```
RAG-Based-PDF-Chatbot/
│
├── Data/                   # Place your PDF files here
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not committed to version control)
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A [Groq API key](https://console.groq.com/) (free tier available)

### 1. Clone the Repository

```bash
git clone https://github.com/Iqra-kaleem/RAG-Based-PDF-Chatbot-with-LangChain-Llama3-Groq-API.git
cd RAG-Based-PDF-Chatbot-with-LangChain-Llama3-Groq-API
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here   # Optional
```

### 4. Add Your PDF Documents

Place your PDF files inside the `Data/` folder. The app will automatically load all PDFs from this directory.

### 5. Run the Application

```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`.

---

## 🧭 How to Use

1. Launch the app with `streamlit run app.py`
2. Click **"Documents Embedding"** to process and index the PDFs in the `Data/` folder
3. Wait for the confirmation message: *"Vector Store DB is Ready"*
4. Type your question in the input field and press Enter
5. The chatbot will retrieve relevant chunks and generate an answer using Llama 3
6. Expand **"Document Similarity Search"** to view the source document chunks used

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| LLM | Llama 3.1 8B (via Groq API) |
| Framework | LangChain |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` |
| Vector Store | FAISS (CPU) |
| PDF Loader | `PyPDFDirectoryLoader` |
| UI | Streamlit |
| Language | Python |

---

## 📦 Dependencies

```
streamlit
langchain
langchain-groq
langchain-community
faiss-cpu
python-dotenv
ollama
beautifulsoup4
sentence-transformers
langchain-openai
openai
pypdf
```

Install all with:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

You can tune the following parameters in `app.py` to fit your use case:

| Parameter | Default | Description |
|---|---|---|
| `chunk_size` | `1000` | Number of characters per document chunk |
| `chunk_overlap` | `200` | Overlap between consecutive chunks |
| `model` | `llama-3.1-8b-instant` | Groq-hosted Llama 3 model |
| `embeddings model` | `all-MiniLM-L6-v2` | HuggingFace sentence transformer |

---

## 🔐 Security Notes

- Never commit your `.env` file — it is already included in `.gitignore`
- Keep your Groq API key private and rotate it if accidentally exposed

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Iqra Kaleem**  
[GitHub](https://github.com/Iqra-kaleem)