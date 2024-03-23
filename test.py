from langchain_community.chat_models import ChatOllama
import ollama

r = ollama.chat(model='tinyllama', messages=[{'role': 'user', 'content': "what si the context window size of you are capable "}])

print(r)