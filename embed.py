import ollama
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_community.embeddings import OllamaEmbeddings


# Load PDF
fpath="p.pdf"
pdf_loader = PyPDFLoader(file_path=fpath)
docs = pdf_loader.load()

# Splitter for the documents
recursive_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)

# Split the documents using the recursive splitter
chunks = recursive_splitter.split_documents(docs)

#embedder
embedder=embeddings.ollama.OllamaEmbeddings(model='nomic-embed-text')


#Convert documents to Embeddings and store them
db = Chroma.from_documents(chunks, embedder,persist_directory="chroma_db")
retriever = db.as_retriever()
