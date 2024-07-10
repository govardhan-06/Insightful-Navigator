from src.utils.exception import customException
from src.utils.logger import logging

import os
import sys

from src.services.pinecone_service import PineConeDB
from llama_index.core import SummaryIndex
from llama_index.readers.web import BrowserbaseWebReader
from llama_index.core.tools import QueryEngineTool

class webRAG:
    def __init__(self):
        os.environ["BROWSERBASE_API_KEY"]=os.getenv("BROWSERBASE_API_KEY")
        os.environ["BROWSERBASE_PROJECT_ID"]=os.getenv("BROWSERBASE_PROJECT_ID")

    def process_Websites(websites:list = ["https://en.wikipedia.org/wiki/SpaceX"]):
        """
        Returns a webRAG tool used to read the websites
        :param websites: list of websites to be read
        """
        try:
            logging.info("Reading the website")
            reader = BrowserbaseWebReader() 
            documents = reader.load_data(urls=websites,text_content=True)
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


