from src.utils.exception import customException
from src.utils.logger import logging

import os
import sys

from llama_index.core import Settings
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding

class appConfig:
    def __init__(self):
        os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')

    def config():
        """
        Configures the LLM and Embedding settings of LlamaIndex and enables Langsmith tracing
        """
        try:
            logging.info("Initiating Langsmith tracing")
            os.environ['LANGCHAIN_TRACING_V2']=os.getenv('LANGCHAIN_TRACING_V2')
            os.environ['LANGCHAIN_ENDPOINT']=os.getenv('LANGCHAIN_ENDPOINT')
            os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
            os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')
            
            logging.info("Configuring llm and embedding settings of llamaindex")
            Settings.llm = Gemini(model="models/gemini-pro",temperature=0.0)
            Settings.embed_model=GeminiEmbedding(model_name="models/embedding-001")

        except Exception as e:
            logging.error(e)
            raise customException(e,sys)