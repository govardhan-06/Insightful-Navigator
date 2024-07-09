import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.gemini import Gemini

load_dotenv()
os.environ['LANGCHAIN_TRACING_V2']=os.getenv('LANGCHAIN_TRACING_V2')
os.environ['LANGCHAIN_ENDPOINT']=os.getenv('LANGCHAIN_ENDPOINT')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')
os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')

Settings.llm=Gemini(model="models/gemini-pro", temperature=0)

