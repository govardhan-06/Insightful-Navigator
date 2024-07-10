from src.utils.exception import customException
from src.utils.logger import logging

import os
import sys

from src.services.pinecone_service import PineConeDB
from llama_index.core import SimpleDirectoryReader
from llama_index.core.tools import QueryEngineTool

class filesRAG:
    def __init__(self):
        pass

    def process_files(self):
        """
        Returns a fileRAG tool used to process the files
        """
        try:
            logging.info("Reading the files")
            documents=SimpleDirectoryReader("data").load_data()
            obj=PineConeDB()
            index=obj.ingest_vectors(documents,"files")
            logging.info(index)
            query_engine=index.as_query_engine()

            logging.info("Creating the tool for handling files")
            files_tool=QueryEngineTool.from_defaults(
                query_engine,
                name='files_RAG',
                description='This tool processes documents from a specified directory, ingests them into Pinecone as vectors, and creates a query engine for retrieving information from the ingested documents efficiently.'
            )

            logging.info("Returned file handling tool")
            return files_tool
        
        except Exception as e:
            logging.error(e)
            raise customException(e,sys)


