import logo from './logo.svg';
import './App.css';
import { useState, useRef } from 'react';

function Weather(props) {
  return (
    <>
      <p>temp: {props.weather_info.temp}</p>
      <p>clouds: {props.weather_info.clouds}</p>
      <p>wind: {props.weather_info.wind}</p>
    </>
  );

}

function Articles(props) {
  return (
    <>
      <p data-testid="article_data1">Headline: {props.article_info.headlines}</p>
      <p>Abstract: {props.article_info.abstract}</p>
      <p>Image: {props.article_info.img_url}</p>
    </>
  )
}

function OpenTripMap(props) {
  return (
    <>
    </>
  )
}

function App() {
  const args = (document.getElementById('data') == null) ? ({
    "city": "test city",
    "weather_info": [
      ["weather_main", "null"],
      ["weather_desc", "null"],
      ["temp", "null"],
      ["feels_like", "null"],
      ["temp_min", "null"],
      ["temp_max", "null"],
      ["pressure", "null"],
      ["humidity", "null"],
      ["clouds", "null"],
      ["wind", "null"],
    ],
    "article_info": [
      ["nyt_main", "null"],
      ["headlines", "null"],
      ["abstract", "null"],
      ["image_url", "null"],
      ["web_url", "null"],
      ["lead_paragraph", "null"],
    ],
    "opentrip": ["No Cool Locations"],
    "opentripimages": ["https://viki.rdf.ru/media/upload/preview/No-Image-Available_1.jpg"],
    "user_id": "test user_id",
    "user_email": "test email",
    "user_name": "test",
  }) : JSON.parse(document.getElementById('data').text);

  const article_info = createObject(args.article_info);
  const weather_info = createObject(args.weather_info);
  let locations = args.opentrip;
  let locationimg = args.opentripimages;

  return (
    <div>

      <div>
        <h1>cityspit</h1>
      </div>

      <div className="page-container">

        <div className="panels-container">

          <div>
            <p data-testid="CityTitle">{args.city}</p>
          </div>

          <div id="weather-panel">
            <Weather weather_info={weather_info} />
          </div>

          <div id="article-panel">
            <Articles article_info={article_info} />
          </div>

          <div id="OpenTripMap-panel">
            <h3> Cool locations near {args.city}</h3>
            {locations.map(location => (
              <p data-testid="CityLocation">{location}</p>
            ))}
            {locationimg.map(img => (
              <img data-testid="CityImages" src={img} width="100" height="100"></img>
            ))}
          </div>

        </div>

        <div id="user-info" data-testid="user-info">
          <p>user id: {args.user_id}</p>
          <p>email: {args.user_email}</p>
          <p>name: {args.user_name}</p>
        </div>

        <div id="logout-link">
          <a id="signup-link" href="logout">
            Logout
          </a>
        </div>

      </div>

    </div>
  );

  // function that takes the weather from the json and transforms it into an easier accessable object
  function createObject(input_array) {

    var arr = {};
    // we need to map each array to its value 
    for (var i = 0; i < input_array.length; i++) {
      var key = input_array[i][0];
      var val = input_array[i][1];
      arr[key] = val;
    }

    return arr;
  }
}

export default App;
