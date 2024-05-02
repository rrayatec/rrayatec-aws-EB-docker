import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {

  // Declarar un estado para almacenar el mensaje de la API
  const [message, setMessage] = useState('');

  // Función para hacer la solicitud a la API REST
  const fetchMessage = async () => {
    axios
      .get('http://aws-api-prod.us-east-1.elasticbeanstalk.com')
      .then((response) => {
        setMessage(response.data.message);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // Usar useEffect para llamar a fetchMessage cuando el componente se monte
  useEffect(() => {
    fetchMessage();
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>{message}</p>

      </header>
    </div>
  );
}

export default App;

