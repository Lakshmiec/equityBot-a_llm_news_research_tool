# **EquityBot: A Powerful News Research Tool for Equity Analysts**

## Overview

EquityBot is a powerful news research tool designed for equity research analysts. This tool leverages LangChain, Google Gemini Pro, and Streamlit to provide an intuitive interface for analyzing news articles and gaining insights for investment decisions. 

## Features

Intuitive User Interface: Streamlit's web framework provides a visually appealing and interactive interface for inputting news article URLs and posing research questions.
Efficient Data Processing: LangChain's UnstructuredURLLoader seamlessly fetches news content from provided URLs, while LangChain's RecursiveCharacterTextSplitter intelligently breaks down the text into manageable chunks.
Advanced Embeddings: Cohere's state-of-the-art embeddings capture the semantic meaning of text, enabling accurate retrieval and analysis.
FAISS Vector Search: FAISS facilitates efficient search within the processed text data, allowing for rapid retrieval of relevant information.
Powerful LLM Integration: Google Gemini Pro, a large language model, analyzes the retrieved information and delivers comprehensive answers to your research queries.


## Technology Stack

- **Programming Language**: Python
- **Web Framework**: Streamlit
- **Natural Language Processing**: LangChain
- **LLM for Data Retrieval**: Google Gemini Pro
- **Embeddings**: Cohere
- **Vector Storage and Retrieval**: FAISS
- **Environment Management**: dotenv

# 🚀 Getting Started

### 1. Prerequisites

- Python 3.x
- Streamlit
- Langchain
- Langchain-Google-GenAI
- Unstructured document loader (e.g., UnstructuredURLLoader)
- Text splitter (e.g., RecursiveCharacterTextSplitter)
- Embedding library (e.g., CohereEmbeddings)
- Vector store (e.g., FAISS)


