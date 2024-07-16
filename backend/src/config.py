from backend.src.utils.exception import customException
from backend.src.utils.logger import logging

import os
import sys

from llama_index.core import Settings
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import set_global_handler

class appConfig:
    def __init__(self):
        os.environ['LANGFUSE_SECRET_KEY']=os.getenv("LANGFUSE_SECRET_KEY")
        os.environ['LANGFUSE_PUBLIC_KEY']=os.getenv("LANGFUSE_PUBLIC_KEY")
        os.environ['LANGFUSE_HOST']=os.getenv("LANGFUSE_HOST")
        os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')

    def config():
        """
        Configures the LLM and Embedding settings of LlamaIndex and enables Langfuse tracing
        """
        try:
            logging.info("Initiating Langfuse tracing")
            set_global_handler("langfuse")
            
            logging.info("Configuring llm and embedding settings of llamaindex")
            Settings.llm = Gemini(model="models/gemini-pro",temperature=0.0)
            Settings.embed_model=GeminiEmbedding(model_name="models/embedding-001")

        except Exception as e:
            logging.error(e)
            raise customException(e,sys)