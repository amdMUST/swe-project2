from dotenv import find_dotenv, load_dotenv
import os
import requests


def getCoordinates(city):
    load_dotenv(find_dotenv())
    Token = os.getenv("TRIPMAP_API_KEY")
    base_url = "https://api.opentripmap.com/0.1/en/places/geoname?"
    name = "name="
    country = "&apikey="
    req = base_url + name + city + country + Token
    r = requests.get(req)
    d = r.json()
    try:
        lon = d["lon"]
        lat = d["lat"]
    except:
        lon = 0
        lat = 0
    return lon, lat


def getPlaces(lon, lat):
    load_dotenv(find_dotenv())
    Token = os.getenv("TRIPMAP_API_KEY")
    base_url = "https://api.opentripmap.com/0.1/en/places/radius?radius=200&"
    lon = "lon=" + str(lon) + "&"
    lat = "lat=" + str(lat) + "&"
    key = "apikey="
    req = base_url + lon + lat + key + Token
    r = requests.get(req)
    d = r.json()
    length = len(d["features"])
    xid = []
    if length == 0:
        x = "Nothing"
        xid.append(x)
    else:
        if length > 3:
            for i in range(0, 3):
                y = d["features"][i]["properties"]["name"]
                if y == "":
                    print("places skip 0-3")
                else:
                    x = d["features"][i]["properties"]["xid"]
                    xid.append(x)
        else:
            for i in range(0, length):
                y = d["features"][i]["properties"]["name"]
                if y == "":
                    print("places skip 0-len")
                else:
                    x = d["features"][i]["properties"]["xid"]
                    xid.append(x)
    return xid


def getPlacesName(xid):
    load_dotenv(find_dotenv())
    length = len(xid)
    info = []
    if xid[0] == "Nothing":
        x = "This Place Sucks; Nothing To Do Here"
        info.append(x)
    else:
        for i in range(0, length):
            Token = os.getenv("TRIPMAP_API_KEY")
            base_url = "https://api.opentripmap.com/0.1/en/places/xid/"
            id = xid[i]
            key = "?apikey="
            req = base_url + id + key + Token
            r = requests.get(req)
            d = r.json()
            name = d["name"]
            info.append(name)
    return info


def getPlacesImages(xid):
    load_dotenv(find_dotenv())
    length = len(xid)
    info = []
    if xid[0] == "Nothing":
        x = "https://www.drodd.com/images14/white7.jpg"
        info.append(x)
    else:
        for i in range(0, length):
            Token = os.getenv("TRIPMAP_API_KEY")
            base_url = "https://api.opentripmap.com/0.1/en/places/xid/"
            id = xid[i]
            key = "?apikey="
            req = base_url + id + key + Token
            r = requests.get(req)
            d = r.json()
            x = d.keys()
            if "preview" in x:
                image = d["preview"]["source"]
                info.append(image)
            else:
                image = "https://image.freepik.com/free-icon/set-of-buildings-in-a-city_318-41262.jpg"
                info.append(image)
    return info


def OpenTrip(city):
    return getPlacesName(getPlaces(getCoordinates(city)[0], getCoordinates(city)[1]))


def OpenTripImages(city):
    return getPlacesImages(getPlaces(getCoordinates(city)[0], getCoordinates(city)[1]))
