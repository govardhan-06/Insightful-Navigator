import React, { useState } from 'react';
import axios from 'axios';

const UserfileUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage('Please select a file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file, file.name);

    try {
      const response = await axios.post('http://localhost:5000/fileupload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          'accept': 'application/json'
        }
      });
      setMessage('File uploaded successfully.');
      console.log('Response:', response.data);
    } catch (error) {
      setMessage('Error uploading file.');
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>File Upload</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default UserfileUpload;
