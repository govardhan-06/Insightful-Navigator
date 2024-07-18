from fastapi import FastAPI, HTTPException, UploadFile
import uvicorn,os

from backend.src.pipeline.agent_execution_pipeline import Agent_Execution
from backend.src.services.pinecone_service import PineConeDB
from backend.src.services.google_drive import GoogleDrive
from backend.src.utils.logger import logging

app=FastAPI()

#Declaring variables globally
obj=None
uploadedFileID=None

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

@app.post('/fileupload')
async def userFileUpload(file: UploadFile):
    gdrive_obj=GoogleDrive()
    metadata={'name':file.filename}
    content_type=file.content_type
    file_location=f'temp/{file.filename}'
    os.makedirs('temp',exist_ok=True)

    content=await file.read()

    with open(file_location,'wb') as f:
        f.write(content)
        
    global uploadedFileID
    uploadedFileID=gdrive_obj.upload_file(file_location,metadata,content_type)
    if(uploadedFileID):
        os.remove(file_location)
        return {"message":"File uploaded successfully","fileID":uploadedFileID}
    else:
        return {"message":"File upload failed"}

@app.post('/filedownload/{fileID}')
async def userFileDownload(fileID:str):
    gdrive_obj=GoogleDrive()
    file_location=gdrive_obj.download_file(fileID)
    if(file_location):
        return {"message":"File downloaded successfully","fileID":f"Disk location: {file_location}"}
    else:
        return {"message":"File download failed"}

@app.post("/destroy")
def removeIndex():
    db_obj=PineConeDB()
    db_obj.destroy_index()
    
if __name__=="__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=5000, reload=True)