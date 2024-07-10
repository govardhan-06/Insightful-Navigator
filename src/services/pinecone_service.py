from src.utils.exception import customException
from src.utils.logger import logging

import os
import sys
import re

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
        files_index_name="userfiles"
        web_index_name="userwebsites"
        logging.info(list(self.config.pc.list_indexes()))
        l=list(self.config.pc.list_indexes())

        #Files index
        if len(list(self.config.pc.list_indexes())) == 0 or files_index_name not in [i['name'] for i in l]:
            try:
                self.config.pc.create_index(name=files_index_name, dimension=768, metric="euclidean", spec=ServerlessSpec(cloud="aws", region="us-east-1"))
            
            except Exception as e:
                raise customException(e,sys)
        
        else:
            logging.info(f"Index {files_index_name} already exists")
        
        #Website index
        if len(list(self.config.pc.list_indexes())) == 0 or web_index_name not in [i['name'] for i in l]:
            try:
                self.config.pc.create_index(name=web_index_name, dimension=768, metric="euclidean", spec=ServerlessSpec(cloud="aws", region="us-east-1"))
            
            except Exception as e:
                raise customException(e,sys)
        
        else:
            logging.info(f"Index {web_index_name} already exists")

        self.pinecone_index_files = self.config.pc.Index(files_index_name)
        self.pinecone_index_web = self.config.pc.Index(web_index_name)


    def clean_up_text(self,content: str) -> str:
        """
        Remove unwanted characters and patterns in text input.

        :param content: Text input.
        
        :return: Cleaned version of original text input.
        """

        # Fix hyphenated words broken by newline
        content = re.sub(r'(\w+)-\n(\w+)', r'\1\2', content)

        # Remove specific unwanted patterns and characters
        unwanted_patterns = [
            "\\n", "  —", "——————————", "—————————", "—————",
            r'\\u[\dA-Fa-f]{4}', r'\uf075', r'\uf0b7'
        ]
        for pattern in unwanted_patterns:
            content = re.sub(pattern, "", content)

        # Fix improperly spaced hyphenated words and normalize whitespace
        content = re.sub(r'(\w)\s*-\s*(\w)', r'\1-\2', content)
        content = re.sub(r'\s+', ' ', content)

        return content

    def clean_up_docs(self,documents,content_type):
        """
        Clean up documents and adds metadata before indexing them.
        :param documents: Documents read from the files
        :param content_type: Type of content, either "files" or "websites"
        :return: Cleaned documents
        """
        cleaned_docs = []
        for d in documents: 
            cleaned_text = self.clean_up_text(d.text)
            d.text = cleaned_text
            cleaned_docs.append(d)
        logging.info(cleaned_docs[0].metadata)

        if content_type=='files':
            title=(cleaned_docs[0].metadata['file_name']).split('.')[0]
        
            metadata_additions = {"title": f"{title}"}

            # Update dict in place
            [cd.metadata.update(metadata_additions) for cd in cleaned_docs]

        return cleaned_docs

    def ingest_vectors(self,documents,content_type):
        """
        Return the index containing the vector embeddings
        :param documents: content from the files provided by the user
        :param content_type: type of content (files or web)
        :return: index containing the vector embeddings
        """
        try:
            logging.info("Creating PineCone DB instances...")
            cleaned_docs=self.clean_up_docs(documents,content_type)
            logging.info(cleaned_docs[0].metadata)
            
            if content_type=="files":
                files_vector_store = PineconeVectorStore(pinecone_index=self.pinecone_index_files)
                files_storage_context = StorageContext.from_defaults(vector_store=files_vector_store)

                file_index = VectorStoreIndex.from_documents(
                cleaned_docs, storage_context=files_storage_context
                )
                logging.info("Successfully, pushed file data embeddings to pinecone DBs")

                return file_index

            elif content_type=="websites":
                web_vector_store = PineconeVectorStore(pinecone_index=self.pinecone_index_web)
                web_storage_context = StorageContext.from_defaults(vector_store=web_vector_store)

                web_index = VectorStoreIndex.from_documents(
                cleaned_docs, storage_context=web_storage_context
                )
                logging.info("Successfully, pushed website data embeddings to pinecone DBs")
                
                return web_index
            
        except Exception as e:
            logging.error(e)
            raise customException(e,sys)