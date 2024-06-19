# import necessary files
import os
import streamlit as st
from  dotenv import load_dotenv
import pickle
import time
import langchain
from langchain_google_genai  import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from streamlit_extras.app_logo import add_logo
from langchain.embeddings import CohereEmbeddings


from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially google and cohere api key)
st.title("Welcome to EquityBot : A News Research Tool📈")
st.write("Analyze news articles and gain insights for your investment decisions.")

# st.image("Images/EquityBot_Logo.jpeg", caption="EquityBot Logo", use_column_width=True)
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Analyse Articles")

file_path = "faiss.pkl"

main_placeholder = st.empty()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.9,max_output_tokens=500, google_api_key=st.secrets["GOOGLE_API_KEY"])

if process_url_clicked:
    #load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()

     # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )

    main_placeholder.text("Text Splitter...Started...✅✅✅")

    docs = text_splitter.split_documents(data)
    # create embeddings and save it to FAISS index
    embeddings = CohereEmbeddings(cohere_api_key= st.secrets["COHERE_API_KEY"])

    # Pass the documents and embeddings inorder to create FAISS vector index
    FAISS_Vector_Databse = FAISS.from_documents(docs, embeddings)

    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    # Storing FAISS vector index create in local
    FAISS_Vector_Databse.save_local("FAISS_Vector_Databse")

    
    query = main_placeholder.text_input("Question: ")
    submit = st.button("🔍 Search")

    if submit:
        if query:
            vectorIndex = FAISS.load_local("FAISS_Vector_Databse", embeddings, allow_dangerous_deserialization=True)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorIndex.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
                # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            st.header("Answer")
            st.subheader(result["answer"])