from src.utils.logger import logging
from src.utils.exception import customException
from src.tools.filesRAG import filesRAG
from src.tools.webRAG import webRAG
from llama_index.core.agent import ReActAgent

import os,sys
 
from dotenv import load_dotenv

def defineAgent():
    """
    Returns the agent to be used in the application
    """
    load_dotenv()
    
    try:
        logging.info("Creating the agent")
        filetool=filesRAG()
        webtool=webRAG()
        agent=ReActAgent.from_tools(
            tools=[filetool.process_files()],
            verbose=True
        )
        return agent
    
    except Exception as e:
        logging.error(e)
        raise customException(e,sys)