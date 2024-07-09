from src.config import appConfig
from src.agents import defineAgent
from src.utils.logger import logging
from src.utils.exception import customException

def main(query):
    """
    Main function to run the application
    :param query: query to run the application
    :return: response from the agent
    """
    appConfig.config()
    agent=defineAgent()
    response=agent.chat(query)
    logging.info(f"Answer: {response}")


if __name__=="__main__":
    main("what is yolo")