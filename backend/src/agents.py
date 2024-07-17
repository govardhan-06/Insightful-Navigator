from backend.src.utils.logger import logging
from backend.src.utils.exception import customException
from backend.src.tools.filesRAG import filesRAG

import sys
 
from dotenv import load_dotenv

def defineAgent():
    """
    Returns the chat engine to be used in the application
    """
    load_dotenv()
    
    try:
        logging.info("Retreiving the engine")
        filechat=filesRAG.process_files()
        return filechat
    
    except Exception as e:
        logging.error(e)
        raise customException(e,sys)