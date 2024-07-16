from backend.src.config import appConfig
from backend.src.agents import defineAgent
from backend.src.utils.logger import logging
from backend.src.utils.exception import customException
from dotenv import load_dotenv
from backend.src.services.pinecone_service import PineConeDB
from pinecone import Pinecone

import os
import sys

class Agent_Execution:
    """
    This class is used to execute the agent on a query from the user
    """
    def __init__(self):
        load_dotenv()
        try:
            appConfig.config()
            self.agent=defineAgent()
        except Exception as e:
            logging.error(e)
            raise customException(e,sys)

    def execute_query(self,query):
        """
        Main function to run the application
        :param query: query to run the application
        :return: response from the agent
        """
        logging.info("Querying the agent")
        response=self.agent.chat(query)
        return response

if __name__=="__main__":
    obj=Agent_Execution()
    obj.execute_query("What is yolo?")
    api_key=os.getenv("PINECONE_API_KEY")
    pc = Pinecone(api_key=api_key)
    pc.delete_index("userfiles")