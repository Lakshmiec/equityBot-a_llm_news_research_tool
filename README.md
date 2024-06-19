# **📈 EquityBot: A Powerful News Research Tool for Equity Analysts**

![Alt text](Images/EquityBot Tool.png)

## Overview

EquityBot is a powerful news research tool designed for equity research analysts. This tool leverages LangChain, Google Gemini Pro, and Streamlit to provide an intuitive interface for analyzing news articles and gaining insights for investment decisions. 


## 🎯 Features

Intuitive User Interface: Streamlit's web framework provides a visually appealing and interactive interface for inputting news article URLs and posing research questions.
Efficient Data Processing: LangChain's UnstructuredURLLoader seamlessly fetches news content from provided URLs, while LangChain's RecursiveCharacterTextSplitter intelligently breaks down the text into manageable chunks.
Advanced Embeddings: Cohere's state-of-the-art embeddings capture the semantic meaning of text, enabling accurate retrieval and analysis.
FAISS Vector Search: FAISS facilitates efficient search within the processed text data, allowing for rapid retrieval of relevant information.
Powerful LLM Integration: Google Gemini Pro, a large language model, analyzes the retrieved information and delivers comprehensive answers to your research queries.


## 🏗️ Technology Stack

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

### 2. Installation

#### 2.1 Clone the repository:

```bash
git clone https://github.com/Lakshmiec/EquityBot-NewsResearch-Tool-LLM.git
cd EquityBot-NewsResearch-Tool-LLM
```
#### 2.2 Navigate to th eproject repository

```bash
cd EquityBot-NewsResearch-Tool-LLM
```

#### 2.3 Install Dependencies

```bash
pip install -r requirements.txt
```

#### 2.4 Setup Environment Variables:

Create a file named `secrets.toml` in the `.streamlit` directory and and add your Google Gemini Pro and Cohere API keys with the following content:

```toml
GOOGLE_API_KEY = "your-google-api-key"
COHERE_API_KEY=  "your-cohere-api-key"
```
#### 2.5 Run the Application:

```bash
streamlit run main.py
```


## Example Usage

1. Access EquityBot in your web browser (usually at http://localhost:8501).
2. In the side panel, paste the URLs of relevant news articles (up to 3).
3. Click the "Analyse Articles" button to process the data.
4. When processing is complete, enter your research question in the main area.
5. Click the " Search" button to retrieve an answer based on the processed news articles.

