import React, {useState, useRef} from 'react';
import './App.css';
import './weatherIcon.css';

function Weather(props) {

  return (
    <>
			<div id="weather-left">
				<div id="weather-icon">
					<i class={getTempIcon(props.weather_info.weather_main)}></i>
				</div>
				<p id="temp">{props.weather_info.temp} °F</p>
				<div id="weather-highlow">
					<p>{Math.floor(props.weather_info.temp_max)} / </p>
					<p>{Math.floor(props.weather_info.temp_min)}</p>
				</div>
				<p id="weather-feels-like">
					Currently feels like {props.weather_info.feels_like} °F
				</p>
				<p id="weather-desc">{props.weather_info.weather_desc}</p>
				<p id="weather-clouds">{props.weather_info.clouds}% Cloudy</p>
				<p id="weather-humidity">{props.weather_info.humidity}% Humidity</p>
			</div>
		</>
  );

  // function for getting the correct weather icon from our icon list
	function getTempIcon(desc) {
		// set up base weather as sunny
		const base = "wi wi-";
		var weather = "";

		switch (desc) {
			case "Thunderstorm":
				weather = "thunderstorm";
				break;
			case "Drizzle":
				weather = "sprinkle";
				break;
			case "Rain":
				weather = "rain";
				break;
			case "Snow":
				weather = "snow";
				break;
			case "Mist":
				weather = "rain-mix";
				break;
			case "Smoke":
				weather = "owm-711";
				break;
			case "Haze":
				weather = "owm-721";
				break;
			case "Fog":
				weather = "owm-741";
				break;
			case "Sand":
				weather = "sandstorm";
				break;
			case "Dust":
				weather = "dust";
				break;
			case "Ash":
				weather = "volcano";
				break;
			case "Squall":
				weather = "alien";
				break;
			case "Tornado":
				weather = "tornado";
				break;
			case "Clear":
				weather = "day-sunny";
				break;
			case "Clouds":
				weather = "cloudy";
				break;
			default:
				weather = "thermometer";
		}

		var finalClassName = base + weather;
		return finalClassName;
	}

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
      <h3>Cool locations near {props.city}</h3>
      {props.locations.map(location => (
        <p data-testid="CityLocation">{location}</p>
      ))}
      {props.locationimg.map(img => (
        <img data-testid="CityImages" alt="location" src={img} width="100" height="100"></img>
      ))}
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
    "user_pic": "https://i.pinimg.com/736x/f1/da/a7/f1daa70c9e3343cebd66ac2342d5be3f.jpg",
		"city_pic": "https://images.unsplash.com/photo-1575917649705-5b59aaa12e6b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80",
  }) : JSON.parse(document.getElementById('data').text);

  const city = args.city;
  const article_info = createObject(args.article_info);
  const weather_info = createObject(args.weather_info);
  let locations = args.opentrip;
  let locationimg = args.opentripimages;

  const [temp, setTemp] = useState(weather_info.temp)
  const weatherPanelColor = changeColor(temp);

  return (
		<div>
			<div className="wrapper" />

			<a href="/">
				<h1 id="title">CitySpit</h1>
			</a>

			<div className="page-container">
				<div className="panels-container">
					<div id="panel">
						<p id="panel-title" data-testid="CityTitle">
							{city}
						</p>

						<div className="grid-container">
							<div className="citypic-panel">
								<img id="citypic" src={args.city_pic} alt="city profile pic" />
							</div>

							<div className="like-panel">
								<div className="button" id="dislike-button">
									<img
										id="dislike-icon"
										src="https://img.icons8.com/external-becris-lineal-becris/64/000000/external-cancel-mintab-for-ios-becris-lineal-becris.png"
                    alt="dislike icon"
									/>
								</div>

								<div className="button" id="like-button">
									<img
										id="like-icon"
										src="https://img.icons8.com/material-outlined/64/000000/like--v1.png"
                    alt="like icon"
									/>
								</div>
							</div>

							<div className="info-panels">
								<div className="article-panel">
									<Articles article_info={article_info} />
								</div>

								<div className="tripmap-panel">
									<OpenTripMap
										locations={locations}
										locationimg={locationimg}
										city={city}
									/>
								</div>
							</div>
							<div className="interaction-panels">
								<div className="userinfo-panel">
									<div id="user-info" data-testid="user-info">
										<br></br>
										<img id="profile-pic" src={args.user_pic} alt="profile pic" />

										<p>Welcome back {args.user_name}!</p>

										<div className="button">
											<a id="button-link" href="profile">
												View your Likes!
											</a>
										</div>
									</div>
									<br></br>

									<div className="button">
										<a id="button-link" href="logout">
											Logout
										</a>
									</div>
								</div>
								<div className="weather-panel" id={weatherPanelColor}>
									<Weather weather_info={weather_info} />
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	);

  // function that changes the color of the weather tab according to the temperature
  function changeColor(temp){
    var className = "average"

    if( temp === null || temp === ""){
      return "average";
    }

    if( temp <= 50 ){
      className = "cold";
    }
    else if( temp >= 51 && temp <= 65 ){
      className = "cool";
    }
    else if( temp >= 66 && temp <= 74 ){
      className = "average";
    }
    else if( temp >= 75 && temp <= 81 ){
      className = "warm";
    }
    else if( temp >= 82 ){
      className = "hot";
    }

    return className;
  }

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