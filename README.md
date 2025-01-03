---
title: Itihas Vachak
emoji: 📖
colorFrom: red
colorTo: green
sdk: gradio
sdk_version: 5.0.1
app_file: app.py
pinned: false
license: mit
short_description: An intelligent QnA system designed to explore Indian history.
---

# 📖 Itihas Vachak

Itihas Vachak is an intelligent question-answering system designed to make exploration of Indian history easy and engaging. Using efficient retrieval techniques and large language models, it provides users with precise and context-rich answers directly from prominent history books.

## 💫 Key Features

- **Comprehensive Knowledge Base**: Leverages multiple history textbooks, covering diverse periods and topics of Indian history.

- **Smart Search System**: Combines classical methods (like BM25) and modern AI-powered retrieval (Sentence-BERT, DPR) for accurate information retrieval.

- **Interactive User Interface**: A user-friendly Gradio-based interface for seamless interaction.

- **Contextual Answers**: Provides concise answers along with references to the source chapters and sections for better understanding.

- **Multi-Document Retrieval**: Handles complex queries spanning multiple textbooks.

## 📁 Project Structure

```bash

Itihas-Vachak/
├── data/
│   ├── processed/                  # Extracted and cleaned text files
│   ├── embeddings/                 # Precomputed embeddings for semantic search
│   ├── database.sqlite             # SQLite database for hierarchical tree and metadata
│   ├── index.faiss
├── src/
│   ├── __init__.py                 # Makes src a Python package
│   ├── extraction/
│   │   ├── __init__.py
│   │   ├── pdf_extractor.py        # Scripts to extract text from PDFs
│   │   ├── text_cleaner.py         # Scripts to preprocess and clean extracted text
│   ├── indexing/
│   │   ├── __init__.py
│   │   ├── hierarchical_tree.py    # Builds and manages the hierarchical tree
│   │   ├── embeddings_indexer.py   # Embedding-based indexing using FAISS
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── bm25_retriever.py       # Classical retrieval with BM25
│   │   ├── semantic_retriever.py   # Semantic retrieval using Sentence-BERT/DPR
│   │   ├── hybrid_retrieval.py     # Combines BM25 and semantic retrieval
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── multi_doc_retriever.py  # Handles multi-document retrieval
│   │   ├── response_generator.py   # Generates answers using an LLM
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── gradio_interface.py     # Gradio app for the user interface
├── .gitignore                      # Files and folders to ignore in version control
├── app.py                          # Entry point
├── LICENSE.md                      # License for the project
├── README.md                       # Project overview and setup instructions
├── requirements.txt                # Dependencies for the project

```

## 💻 Technologies Used

- **FAISS**: Vector store
- **Gradio**: User Interface
- **NLTK**: Natural Language Processing library
- **PyMuPdf**: Library for processing pdf files
- **SQLite**: Database for storing hierarchical data
- **Sentence Transformers**: Library for creating embeddings
- **Pytesseract**: OCR engine (Desktop and Library)

## 📋 Attribution
This project uses the following textbooks as sources for content:  
1. **History of Medieval India** by Satish Chandra  
2. **India’s Ancient Past** by R.S. Sharma  
3. **India Since Independence** by Bipin Chandra  

The content from these books is used solely for educational and non-commercial purposes.

## 🔗 Important Links

- **GitHub Repository**: [Click here](https://github.com/Adm-2005/Itihas-Vachak)
- **Live Demo**: [Click here](https://drive.google.com/file/d/1Pru2GdxzoWUEKt6ZMntkQ1_ncgvjVfwa/view?usp=sharing)
- **Documentation Link**: [Click here](https://docs.google.com/document/d/1Ty88uf5lNP-Ters0yYXM2O-dSdasTWH4/edit?usp=sharing&ouid=103738077583465355360&rtpof=true&sd=true)