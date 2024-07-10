from src.utils.exception import customException
from src.utils.logger import logging

import os
import sys

from src.services.chromaDB_service import ChromaDB
from llama_index.core import SimpleDirectoryReader
from llama_index.core.tools import QueryEngineTool, ToolMetadata

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
            obj=ChromaDB()
            files_index=obj.chroma_files(documents)
            query_engine = files_index.as_query_engine()

            logging.info("Creating the tool for handling files")

            files_tool=QueryEngineTool(query_engine=query_engine,metadata=ToolMetadata(name="file_based_RAG_tool",
                                       description=(
                                                    "Use a detailed plain text question as input to the tool."
                                                   ),
                                            ),
                                        )

            logging.info("Returned file handling tool")
            return files_tool
        
        except Exception as e:
            logging.error(e)
            raise customException(e,sys)


