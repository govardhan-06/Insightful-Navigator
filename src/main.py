from src.config import appConfig
from src.agents import defineAgent
from src.utils.logger import logging
from src.utils.exception import customException
from dotenv import load_dotenv

def execute_query(query):
    """
    Main function to run the application
    :param query: query to run the application
    :return: response from the agent
    """
    load_dotenv()
    appConfig.config()
    agent=defineAgent()
    logging.info("Querying the agent")
    response=agent.chat(query)
    return response

if __name__=="__main__":
    execute_query("What is yolo?")