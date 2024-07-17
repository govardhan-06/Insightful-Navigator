from fastapi import FastAPI, HTTPException
import uvicorn

from backend.src.pipeline.agent_execution_pipeline import Agent_Execution
from backend.src.utils.logger import logging

app=FastAPI()

#Declaring obj globally
obj=None

@app.get("/home")
def home():
    global obj
    if obj is None:
        logging.info('Intiating the agent execution pipeline')
        obj=Agent_Execution()
    return "Welcome to Insightful Navigator"

@app.post("/chat")
def fileChat(query:str):
    global obj
    if obj is None:
        raise HTTPException(status_code=400, detail="Failed to index the documents, visit /home first")
    response=obj.execute_query(query)
    return response
    
if __name__=="__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=5000, reload=True)