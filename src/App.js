import React, { useState, useEffect } from 'react';
import './App.css';
import './weatherIcon.css';

function Weather(props) {
	return (
		<>
			<div id="weather-left">
				<div id="weather-icon">
					<i className={getTempIcon(props.weather_info.weather_main)}></i>
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
			<p>Image: </p>
			<img
				src={props.article_info.img_url}
				alt="Article Art"
				width="100"
				height="100"
			></img>
			<p>
				Want More: <a href={props.article_info.web_url}> Click Me!</a>
			</p>
		</>
	);
}

function OpenTripMap(props) {
	return (
		<>
			<h5>Cool locations near {props.city}</h5>
			{props.locations.map((location) => (
				<p data-testid="CityLocation" key={location}>
					{location}
				</p>
			))}
			{props.locationimg.map((img) => (
				<img
					key={img}
					data-testid="CityImages"
					alt="location"
					src={img}
					width="100"
					height="100"
				/>
			))}
		</>
	);
}

function App() {
	const args =
		document.getElementById("data") == null
			? {
					city_list: [
						"Istanbul",
						"Vienna",
						"Madrid",
						"Athens",
						"Nashville",
						"Osaka",
						"Mexico city",
						"Brisbane",
						"Marseille",
						"Dallas",
						"Montreal",
						"Bangkok",
						"Stockholm",
						"Lyon",
						"Auckland",
						"Hong kong",
						"Zurich",
						"Muscat",
						"Kuwait city",
						"New york"
					],
					user_id: "test user_id",
					user_email: "test email",
					user_name: "test",
					user_pic:
						"https://i.pinimg.com/736x/f1/da/a7/f1daa70c9e3343cebd66ac2342d5be3f.jpg"
			  }
			: JSON.parse(document.getElementById("data").text);
	// the base information we need to fill out the panel

	// constants for widget information
	const [city_image, set_city_image] = useState(
		createObject([
			[
				"image_url",
				"https://images.unsplash.com/photo-1575917649705-5b59aaa12e6b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
			]
		])
	);
	const [weather_info, set_weather_info] = useState(
		createObject([
			["weather_main", "lovely"],
			["weather_desc", "love is in the air"],
			["temp", "?"],
			["feels_like", "0"],
			["temp_min", "0"],
			["temp_max", "0"],
			["pressure", "0"],
			["humidity", "0"],
			["clouds", "0"],
			["wind", "0"]
		])
	);
	const [article_info, set_article_info] = useState(
		createObject([
			["nyt_main", "null"],
			["headlines", "null"],
			["abstract", "null"],
			[
				"img_url",
				"https://viki.rdf.ru/media/upload/preview/No-Image-Available_1.jpg"
			],
			["web_url", "null"],
			["lead_paragraph", "null"]
		])
	);
	const [locations, set_locations] = useState(["No Cool Locations"]);
	const [locationimg, set_locationimg] = useState([
		"https://viki.rdf.ru/media/upload/preview/No-Image-Available_1.jpg"
	]);

	// like button constants
	const [buttonsDisabled, setButtonsDisabled] = useState(false);
	const like_img =
		"https://img.icons8.com/material-outlined/64/000000/like--v1.png";
	const dislike_img =
		"https://img.icons8.com/external-becris-lineal-becris/64/000000/external-cancel-mintab-for-ios-becris-lineal-becris.png";

	// loading screen constants
	const [gridContainer, setGridContainer] = useState("grid-container");

	// city constants
	const cityList = args.city_list;
	const [cityIndex, setCityIndex] = useState(0);
	const [city, setCity] = useState(cityList[cityIndex]);

	// when the index changes, change the city, then get that cities info
	useEffect(() => setCity(cityList[cityIndex]), [cityIndex]);
	useEffect(() => getCityInfo(city), [city]);

	return (
		<div>
			<a href="/">
				<h1 id="title">CitySpit</h1>
			</a>

			<div className="page-container">
				<div className="panels-container">
					<Panel city={city} />
				</div>
			</div>
		</div>
	);

	// Component that updates the info about the city everytime there is a new city
	function Panel(props) {
		// weather panel constant
		const weatherPanelColor = changeColor(weather_info.temp);

		return (
			<div id="panel">
				<p id="panel-title" data-testid="CityTitle">
					{props.city}
				</p>

				<div className={gridContainer}>
					<div
						className="loading-panel"
						style={{ display: gridContainer === "grid-container" ? "none" : "block" }}
					>
						<div className="loading"></div>
					</div>

					<div className="citypic-panel">
						<img id="citypic" src={city_image.image_url} alt="city profile pic" />
					</div>

					<div className="like-panel-mobile">
						<div className="button" id="dislike-button">
							<button onClick={updateCityIndex} disabled={buttonsDisabled}>
								<img id="dislike-icon" src={dislike_img} alt="dislike icon" />
							</button>
						</div>

						<div className="button" id="like-button">
							<button onClick={saveCityToDB} disabled={buttonsDisabled}>
								<img id="like-icon" src={like_img} alt="like icon" />
							</button>
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
						<div className="like-panel">
							<div className="button" id="dislike-button">
								<button onClick={updateCityIndex} disabled={buttonsDisabled}>
									<img id="dislike-icon" src={dislike_img} alt="dislike icon" />
								</button>
							</div>

							<div className="button" id="like-button">
								<button onClick={saveCityToDB} disabled={buttonsDisabled}>
									<img id="like-icon" src={like_img} alt="like icon" />
								</button>
							</div>
						</div>

						<div className="weather-panel" id={weatherPanelColor}>
							<Weather weather_info={weather_info} />
						</div>

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
					</div>
				</div>
			</div>
		);
	}

	// function that saves the current city to the users db and then increments the city to the next
	function saveCityToDB(){

		// here is where you make fetch to DB to save to users db
		// just copied pasted. needs to be filled out
		fetch("/save_city", {
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				// fill in what we are passing to flask
			})
		})
			.then((response) => response.json())
			.then((data) => {
				// fill this in if we need anything
			}).catch(function (error) {
				console.log("Caught error while saving city to user's DB: " + error);
			});

		// now increment the city
		updateCityIndex();
	}

	// function to update the value of the city index and make sure it doesnt go out of bounds
	function updateCityIndex() {
		if (cityIndex < cityList.length - 1) {
			// before we set a timer, we update index+1 and disable the like/dislike button again
			setCityIndex(cityIndex + 1);
			setButtonsDisabled(true);
		}
	}

	// function that changes the color of the weather tab according to the temperature
	function changeColor(temp) {
		var className = "average";

		if (temp === null || temp === "") {
			return "average";
		}

		if (temp <= 50) {
			className = "cold";
		} else if (temp >= 51 && temp <= 65) {
			className = "cool";
		} else if (temp >= 66 && temp <= 74) {
			className = "average";
		} else if (temp >= 75 && temp <= 81) {
			className = "warm";
		} else if (temp >= 82) {
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

	// function that will make a fetch request to the server for the information needed from the api's
	function getCityInfo(city) {
		// now lets make the loading div visible while the timer runs
		setGridContainer("grid-container-loading");

		// fetch api call
		fetch("/get_city", {
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify({
				city: city
			})
		})
			.then(handleErrors)
			.then((response) => response.json())
			.then((data) => {
				set_city_image(createObject(data.city_image));
				set_weather_info(createObject(data.weather_info));
				set_article_info(createObject(data.article_info));
				set_locations(data.opentrip);
				set_locationimg(data.opentripimages);
			})

			.catch(function (error) {
				console.log("Caught error while fetching info about the next city: " + error);
			});

		function handleErrors(response) {
			if (!response.ok) {
				throw Error(response.statusText);
			}
			return response;
		}

		// once the timer finishes, it will change these two states
		setTimeout(() => {
			setButtonsDisabled(false);
			setGridContainer("grid-container");
		}, 6000);
	}
}

export default App;