from backend.src.utils.logger import logging
from backend.src.utils.exception import customException
from backend.src.tools.filesRAG import filesRAG
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
        agent=ReActAgent.from_tools(
            tools=[filetool.process_files()],
            verbose=True
        )
        return agent
    
    except Exception as e:
        logging.error(e)
        raise customException(e,sys)