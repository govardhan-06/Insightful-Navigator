from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload,MediaIoBaseDownload
from dataclasses import dataclass

from backend.src.utils.logger import logging
import os,io

@dataclass
class GoogleDriveConfig:
    """
    Setting up the configuration for google drive client
    """
    try:
        SCOPES = ['https://www.googleapis.com/auth/drive.file']  #authorization scope
        SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_KEY")
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
        drive=build('drive','v3',credentials=credentials)

    except HttpError as e:
        logging.info(f"Drive Error: {e}")

class GoogleDrive:
    def __init__(self):
        self.config = GoogleDriveConfig()
    
    def upload_file(self,file_location,file_metadata,file_content_type):
        '''
        Uploads the file to google drive
        :param file_location: uploaded file location
        :param file_metadata: uploaded file metadata
        :param file_content_type: uploaded file content type
        :return: uploaded file id
        '''
        try:
            media = MediaFileUpload(file_location, mimetype=file_content_type)

            file=self.config.drive.files().create(body=file_metadata, media_body=media, fields='id').execute()

        except HttpError as e:
            logging.info(f"Drive Error: {e}")
            file=None
        
        return file.get('id')

    def download_file(self,file_id):
        '''
        Downloads the file from google drive
        :param file_id: file id to be downloaded
        :return: downloaded file disk location
        '''
        try:
            file_metadata=self.config.drive.files().get(fileId=file_id).execute()
            filename=file_metadata['name']
            os.makedirs("data",exist_ok=True)

            request=self.config.drive.files().get_media(fileId=file_id)

            file_location=f"data/{filename}"
            file=io.FileIO(file_location,'wb')
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                logging.info(f"Download {int(status.progress() * 100)}%.")

            return {"file_path": file_location}
        
        except HttpError as e:
            logging.info(f"Drive Error: {e}")

