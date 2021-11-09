import logo from './logo.svg';
import './App.css';
import { useState, useRef } from 'react';


function App() {
  const args = (document.getElementById('data') == null) ? ({
    "city" : "test city",
    "weather_info":{
      "weather_main":"null",
      "weather_desc":"null",
      "temp":"null",
      "feels_like":"null",
      "temp_min":"null",
      "temp_max":"null",
      "pressure":"null",
      "humidity":"null",
      "clouds":"null",
      "wind":"null"
   },
    "user_id": "test user_id",
    "user_email": "test email",
    "user_name": "test",
  }) : JSON.parse(document.getElementById('data').text);

  const weather_info = (JSON.parse(JSON.stringify(args.weather_info)));
  console.log(weather_info);

  return (
    <div>
      <div>
        <h1>City Name: {args.city}</h1>
      </div>
      
      <div id="weather">
        <p>temp: {weather_info.temp}</p>
        <p>clouds: {weather_info.clouds}</p>
        <p>wind: {weather_info.wind}</p>
        
        <p>user id: {args.user_id}</p>
        <p>email: {args.user_email}</p>
        <p>name: {args.user_name}</p>
      </div>

      <div id="articles">

      </div>

      <div id="OpenTripMap">

      </div>
      <div id="logout-link">
        <a id="signup-link" href="logout">
          Logout
        </a>
      </div>
    </div>
  );
}

export default App;
