# Insightful Navigator

Insightful Navigator is a chat-with-document web application designed to facilitate seamless interaction with documents. Built using React Vite and FastAPI, it leverages advanced AI technologies to provide efficient document querying and management.

## Features

- **Document Chat Interface**: Engage in interactive chat sessions with your documents for quick information retrieval.
- **Advanced Querying**: Utilize Gemini for powerful and accurate document querying.
- **Embeddings Storage**: Store and manage document embeddings with Pinecone for efficient and scalable data handling.
- **File Management**: Upload and store your documents using the Google Drive API.
- **Activity Tracking**: Monitor and analyze user interactions with Langfuse tracking.
- **RAG Framework**: Implement the Retrieval-Augmented Generation (RAG) framework using LlamaIndex for enhanced document processing.

## Technologies Used

- **Frontend**: React Vite
- **Backend**: FastAPI
- **Querying**: Gemini
- **Embeddings Storage**: Pinecone
- **File Storage**: Google Drive API
- **Tracking**: Langfuse
- **RAG Framework**: LlamaIndex

## Installation

### Prerequisites

- Node.js
- Python 3.x
- FastAPI
- Access to Gemini, Pinecone, Google Drive API, and Langfuse

### Setup

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your-username/insightful-navigator.git
   cd insightful-navigator
   ```

2. **Install frontend dependencies**:

   ```sh
   cd frontend
   npm install
   ```

3. **Install backend dependencies**:

   ```sh
   cd ..
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file in the `backend` directory and add the necessary API keys and configuration settings:

   ```env
   LANGFUSE_HOST='https://cloud.langfuse.com'
   LANGFUSE_SECRET_KEY=""
   LANGFUSE_PUBLIC_KEY=""
   GOOGLE_API_KEY=""
   PINECONE_API_KEY=""
   COHERE_API_KEY=""
   SERVICE_ACCOUNT_KEY=""
   ```

5. **Run the backend server**:

   ```sh
   python run application.py
   ```

6. **Run the frontend development server**:

   ```sh
   cd ../frontend
   npm run dev
   ```

## Usage

1. **Upload Documents**: Use the upload feature to add your documents to the system.
2. **Chat with Documents**: Engage in interactive chat sessions to retrieve information from your documents.
3. **Track Interactions**: Monitor user interactions and analyze data through Langfuse tracking.

## Contributing

We welcome contributions to enhance Insightful Navigator. Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact Govardhan A R at govardhanar06@gmail.com.
