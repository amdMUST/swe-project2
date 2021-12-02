# CitySpit

Have you ever been on dating apps, like tinder and bumble? Have you ever wanted to go on vacation, but don't know where to go? 
Well, look no further! Introducing CitySpit, a web application where you can like or dislike location based on cool things to do there 
interesting news articles, or even if the weather is just not for you. You as a user have your very own account where you can like a city
and it well be saved to your profile so you can take a look at you city at another time with real live updates!

## Contributors
Ahmed Mustafa<br>
Michael Dinh<br>
Joan Galicia<br>
Mehmet Filik<br>

## Installation

On your command line you should enter this 
```bash
git clone git@github.com:amdMUST/swe-project2.git
```
to clone my github repo, which should contain almost every file you need to get started

Perfect! Now, the only files left to make is the .env files which contains your API tokens
```bash
touch .env
```
```bash
code .env
```
The first things you'll need is a Google Client ID and Google Secrect ID so you can use the google login fuctions.

Should look like this.
```bash
GOOGLE_CLIENT_ID='YourClientHere'
GOOGLE_CLIENT_SECRET='YourSecretHere'
```

Next you need your New York Times Creditials so you can access the articles of the cities.
```bash
export NYT_API_KEY='YourKeyHere'
export NYT_API_SECRET='YourSecretHere'
```

Moving on to the OpenTripMap, This API get cool locations in that particular city.
```bash
export TRIPMAP_API_KEY='YourAPIKey'
```

Now for the Weather API which tells you weather information about the city.
```bash
export WEATHER_API_KEY='YourAPIKeyHere'
```

Now your DataBase URL
```bash
export DATABASE_URL='YourDATABASEUrl'
```

Finally, Your Unsplash API keys, which this api would send back a photo of the city.
```bash
export UNSPLASH_ACCESS_KEY='YourAccessKeyHere'
export UNSPLASH_SECRET_KEY='YourSecretKeyHere'
```

After you run that you need to install npm to start a build for that enter this command
```bash
npm install -d npm
```

then you would want to go to the folder and enter this command to build it 
```bash
npm run build
```

Now you should be good to go to run app.py! ENJOY!


## Feedback
What Didn't Go Well:
<ol>
    <li>
        For this project, we as a group didn't run into alot of issues. This only issues we had were minor bugs fixes.
        Some of the bugs consists of, city names like New York and San Jose were only passing like New and San and the other APIs does not
        recognize New and San as cities. Another bug was when we were getting images from url links, some of the links do not have image on their database, so we have to check for that and catch it so we could load a default picture.
    </li>
    <li>
        Merging was another minor issue. We only covered it in class but really didn't go in super details. We're glad that we had that lesson in class, but there were issues such as reading merge conflicts that we were not fluent at.
    </li>
    <li>
        Since we all have a busy schedule, it was really hard to find a day in a week where we would meet to discuss about our codes and do merges.
    </li>
</ol>

What Did Go Well:
<ol>
    <li>
        We were always on the same page, no matter what conflicts we ran into. we resolved it in a fast and efficient manner.
    </li>
    <li>
        Since working together under one repository, there will be merging conflicts. So what we did was, we would schedule a meeting with each other and made a pull request for each of our branches and resovled any conflicts or errors.
    </li>
    <li>
        Each of us had a set of task we needed to do before our deadline and everyone got on top of it and didn't wait last minute, so we could resovle any issues that any of our code had.
    </li>
</ol>

## APIs
API Used:
<ol>
    <li>
        OpenTripMap
    </li>
    <li>
        Google Login
    </li>
    <li>
        New York Times
    </li>
    <li>
        OpenWeather
    </li>
    <li>
        Unsplash
    </li>
</ol>

## Heroku
We had 2 sprints for our project the first heroku link could be found here

Sprint 1 = http://cityspit.herokuapp.com/

Sprint 2 = http://cityspit2.herokuapp.com/