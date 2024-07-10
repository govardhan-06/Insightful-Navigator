import chromadb
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext

class ChromaDB:
    def __init__(self):
        self.db = chromadb.PersistentClient(path="./chroma_db")
        self.files_chroma_collection = self.db.get_or_create_collection("userfiles")
        self.web_chroma_collection = self.db.get_or_create_collection("userwebsites")

    def chroma_files(self,docs):
        """
        Returns vector store index after push the file embeddings to chromaDB
        :docs :documents extracted from the files
        """
        files_vector_store = ChromaVectorStore(chroma_collection=self.files_chroma_collection)
        files_storage_context = StorageContext.from_defaults(vector_store=files_vector_store)

        files_index = VectorStoreIndex.from_documents(
            docs, storage_context=files_storage_context
        )

        return files_index
    
    def chroma_websites(self,docs):
        """
        Returns vector store index after push the website embeddings to chromaDB
        :docs :documents extracted from the files
        """
        web_vector_store = ChromaVectorStore(chroma_collection=self.web_chroma_collection)
        web_storage_context = StorageContext.from_defaults(vector_store=web_vector_store)

        web_index = VectorStoreIndex.from_documents(
            docs, storage_context=web_storage_context
        )

        return web_index
