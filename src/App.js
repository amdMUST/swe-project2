import logo from './logo.svg';
import './App.css';
import { useState, useRef } from 'react';

function Weather(props) {

  return (
    <>
    </>
  );

}

function Articles(props) {
  console.log(props.article_info.headlines)
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
    "city": "Test City",
    "article_info": [
      ["nyt_main", "test1"],
      ["headlines", "test1"],
      ["abstract", "null"],
      ["image_url", "null"],
      ["web_url", "null"],
      ["lead_paragraph", "null"],
    ],
    "user_id": "test user_id",
    "user_email": "test email",
    "user_name": "test",
  }) : JSON.parse(document.getElementById('data').text);

  const article_info = createObject(args.article_info);
  console.log(article_info);
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
            {/* <Weather weather_info={weather_info} /> */}
          </div>

          <div id="article-panel">
            <Articles article_info={article_info} />
          </div>

          <div id="OpenTripMap-panel">
            <OpenTripMap />
          </div>

        </div>

        <div id="user-info">
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
