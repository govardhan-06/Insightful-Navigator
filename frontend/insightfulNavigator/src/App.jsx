import { useState } from 'react';
import './App.css';
import Filehandler from './components/filehandler';

function App() {
  return (
    <div>
      <h1>Insightful Navigator</h1>
      <h2>Upload your file</h2>
      <Filehandler />
    </div>
  )
}

export default App
