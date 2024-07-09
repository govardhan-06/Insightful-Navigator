from src.utils.logger import logging
from src.utils.exception import customException
from src.tools.filesRAG import filesRAG
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
        agent=ReActAgent.from_tools(
            tools=[filesRAG.process()],
            verbose=True
        )
        return agent
    
    except Exception as e:
        logging.error(e)
        raise customException(e,sys)