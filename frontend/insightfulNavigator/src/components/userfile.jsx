import React, { useState } from 'react';
import axios from 'axios';

const Userfile = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');
  var fileid='';

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleDownload = async (id) => {
    try {
      const response = await axios.post('http://localhost:5000/filedownload/'+id, {}, {
        headers: {
          'accept': 'application/json'
        }
      });
      console.log('Response:', response.data);
    } catch (error) {
      console.error('Error downloading file:', error);
    }
  };

  const fileEmbed=async ()=>{
    try {
      const response = await axios.get('http://localhost:5000/home', {}, {
        headers: {
          'accept': 'application/json'
        }
      });
      console.log('Response:', response.data);
    } catch (error) {
      console.error('Error embedding file:', error);
    }
  }

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
      fileid=response.data.fileID;
    } catch (error) {
      setMessage('Error uploading file.');
      console.error('Error:', error);
    }
    handleDownload(fileid);
    fileEmbed();
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

export default Userfile;
