from backend.src.utils.exception import customException
from backend.src.utils.logger import logging

import os
import sys

from backend.src.services.pinecone_service import PineConeDB
from llama_index.core import SimpleDirectoryReader
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine

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
            index=obj.ingest_vectors(documents)

            # configure retriever
            retriever = VectorIndexRetriever(
                index=index,
                similarity_top_k=5,
            )

            # Retrieve top 5 results
            results = retriever.retrieve("What is operator overloading?")
            # Print the results
            for result in results:
                print(result)

            # # assemble query engine
            # query_engine = RetrieverQueryEngine(
            #     retriever=retriever,
            # )

            # files_tool=QueryEngineTool(query_engine=query_engine,metadata=ToolMetadata(name="file_based_RAG_tool",
            #                            description=(
            #                                         "Use a detailed plain text question as input to the tool."
            #                                        ),
            #                                 ),
            #                             )

            logging.info("Returned file handling tool")
            # return files_tool
        
        except Exception as e:
            logging.error(e)
            raise customException(e,sys)


