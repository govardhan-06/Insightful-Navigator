from src.utils.exception import customException
from src.utils.logger import logging

import os
import sys

from src.services.chromaDB_service import ChromaDB
from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core.tools import QueryEngineTool, ToolMetadata

class webRAG:
    def __init__(self):
        pass

    def process_Websites(websites:list):
        """
        Returns a webRAG tool used to read the websites
        :param websites: list of websites to be read
        """
        try:
            logging.info("Reading the website")
            websites=["https://en.wikipedia.org/wiki/International_Space_Station"]
            documents = SimpleWebPageReader(html_to_text=True).load_data(websites)
            obj=ChromaDB()
            index=obj.chroma_websites(documents)
            query_engine=index.as_query_engine()

            logging.info("Creating the tool for handling websites")
            web_tool=QueryEngineTool(
                query_engine,metadata=ToolMetadata(name="website_based_RAG_tool",
                                       description=(
                                                    "Use a detailed plain text question as input to the tool."
                                                   ),
                                            ),
                                        )

            logging.info("Returned website handling tool")
            return web_tool
        
        except Exception as e:
            logging.error(e)
            raise customException(e,sys)


