from backend.src.utils.exception import customException
from backend.src.utils.logger import logging

import sys

from backend.src.services.pinecone_service import PineConeDB
from llama_index.core import SimpleDirectoryReader
from llama_index.core.memory import ChatMemoryBuffer

class filesRAG:
    def __init__(self):
        pass

    def process_files():
        """
        Returns a fileRAG chatengine used to process the files
        """
        try:
            logging.info("Reading the files")
            documents=SimpleDirectoryReader("data").load_data()
            obj=PineConeDB()
            index=obj.ingest_vectors(documents)
            memory = ChatMemoryBuffer.from_defaults(token_limit=3900)
            files_chat = index.as_chat_engine(chat_mode="best",verbose=True)

            logging.info("Returned fileRAG chat engine")
            return files_chat
        
        except Exception as e:
            logging.error(e)
            raise customException(e,sys)


