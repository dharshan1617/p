import ollama
from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama


#embedder
embedder=embeddings.ollama.OllamaEmbeddings(model='nomic-embed-text')



# load from disk
db = Chroma(persist_directory="chroma_db", embedding_function=embedder)

retriever = db.as_retriever()


#formatting the docs 
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


#define the ollama model 
def ollama_llm(question, context):
    formatted_prompt = f"Question: {question}\n\nContext: {context}"
    response = ollama.chat(model='tinyllama', messages=[{'role': 'user', 'content': formatted_prompt}])
    return response['message']['content']


# Define the RAG chain
def rag_chain(question):
    retrieved_docs = retriever.invoke(question)
    formatted_context = format_docs(retrieved_docs)
    return ollama_llm(question, formatted_context)

# Use the RAG chain
result = rag_chain("can u explain the concept of find a string in a string ")
print(result)



