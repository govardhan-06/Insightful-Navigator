from src.utils.exception import customException
from src.utils.logger import logging

import os
import sys

from src.services.pinecone_service import PineConeDB
from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core.tools import QueryEngineTool

class webRAG:
    def __init__(self):
        pass

    def process_Websites(websites:list = ["https://en.wikipedia.org/wiki/SpaceX"]):
        """
        Returns a webRAG tool used to read the websites
        :param websites: list of websites to be read
        """
        try:
            logging.info("Reading the website")
            documents = SimpleWebPageReader(html_to_text=True).load_data(websites)
            logging.info(documents[0])
            obj=PineConeDB()
            index=obj.ingest_vectors(documents)
            query_engine=index.as_query_engine()

            logging.info("Creating the tool for handling files")
            web_tool=QueryEngineTool.from_defaults(
                query_engine,
                name='web_RAG',
                description='This tool processes data from a specified website, ingests them into Pinecone as vectors, and creates a query engine for retrieving information from the ingested documents efficiently.'
            )

            logging.info("Returned website handling tool")
            return web_tool
        
        except Exception as e:
            logging.error(e)
            raise customException(e,sys)


