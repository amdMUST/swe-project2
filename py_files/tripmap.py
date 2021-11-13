from dotenv import find_dotenv, load_dotenv
import os
import requests


def getCoordinates(city):
    load_dotenv(find_dotenv())
    Token = os.getenv("TRIPMAP_API_KEY")
    base_url = "https://api.opentripmap.com/0.1/en/places/geoname?"
    name = "name="
    country = "&country=US&apikey="
    req = base_url + name + city + country + Token
    r = requests.get(req)
    d = r.json()
    lon = d["lon"]
    lat = d["lat"]
    return lon, lat


def getPlaces(lon, lat):
    load_dotenv(find_dotenv())
    Token = os.getenv("TRIPMAP_API_KEY")
    base_url = "https://api.opentripmap.com/0.1/en/places/radius?radius=100&"
    lon = "lon=" + str(lon) + "&"
    lat = "lat=" + str(lat) + "&"
    key = "apikey="
    req = base_url + lon + lat + key + Token
    r = requests.get(req)
    d = r.json()
    length = len(d["features"])
    xid = []
    for i in range(0, length):
        x = d["features"][i]["properties"]["xid"]
        xid.append(x)
    return xid


def getPlacesInfo(xid):
    load_dotenv(find_dotenv())
    length = len(xid)
    info = []
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


def OpenTrip(city):
    return getPlacesInfo(getPlaces(getCoordinates(city)[0], getCoordinates(city)[1]))
