from src.utils.exception import customException
from src.utils.logger import logging
from dotenv import load_dotenv
import os
import sys

from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from llama_index.core import StorageContext
from dataclasses import dataclass

@dataclass
class PineConeDBConfig:
    """
    PineconeConfig class is used to store the configuration of Pinecone vector DB
    """
    api_key=os.getenv("PINECONE_API_KEY")
    pc = Pinecone(api_key=api_key)

class PineConeDB:
    def __init__(self):
        self.config = PineConeDBConfig()
        index_name="userdata"
        if index_name not in self.pc.list_indexes():
            try:
                self.config.pc.create_index(index_name=index_name, dimension=768, metric="cosine", spec=ServerlessSpec(cloud="aws", region="us-east-1"))
            except Exception as e:
                raise customException(e,sys)
        
        else:
            print(f"Index {index_name} already exists")

        self.pinecone_index = self.config.pc.Index(index_name)

    def ingest_vectors(self,documents):
        """
        Ingests the embeddings into Pinecone vector DB
        """
        try:
            logging.info("Creating PineCone DB instance...")
            vector_store = PineconeVectorStore(pinecone_index=self.pinecone_index)
            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            index = VectorStoreIndex.from_documents(
            documents, storage_context=storage_context
            )
            logging.info("Successfully, pushed the embeddings to pinecone DB")
            return index
        except Exception as e:
            logging.error(e)
            raise customException(e,sys)