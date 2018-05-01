import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import math
from googlemaps import *
import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'


def deg2rad(deg):
    return deg * (3.14159265358979323846264338327950 / 180)


def getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2):
    R = int(6371)
    dLat = float(deg2rad(lat2 - lat1))
    dLon = float(deg2rad(lon2 - lon1))
    a = float(math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(
        dLon / 2) * math.sin(dLon / 2))
    c = float(2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))
    d = int(R * c)
    return d


my_url = "https://in.bookmyshow.com/buytickets/avengers-infinity-war-bengaluru/movie-bang-ET00073462-MT/20180428"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("a", {"class": "__venue-name"})

file = "project.csv"
f = open(file, "w")
headers = "venue, data, distance \n"
f.write(headers)
i = 0
for container in containers:
    if container.strong is None:
        break
    benue = container.strong.text
    print(benue)

    details = page_soup.findAll("div", {"data-online": "Y"})
    detail = details[i]
    bata = detail.a['data-cat-popup']
    i += 1
    print(bata)
    address1 =("electronic city")
    address2 =("chennai")
    url1 = serviceurl + urllib.parse.urlencode({'sensor': 'false', 'address': address1})
    url2 = serviceurl + urllib.parse.urlencode({'sensor': 'false', 'address': address2})
    uh1 = urllib.request.urlopen(url1).read()
    uh2 = urllib.request.urlopen(url2).read()
    tree1 = ET.fromstring(uh1)
    tree2 = ET.fromstring(uh2)
    r1 = tree1.findall('result')
    r2 = tree2.findall('result')
    
    lat1 = r1[0].find('geometry').find('location').find('lat').text
    lon1 = r1[0].find('geometry').find('location').find('lng').text
    lat2 = r2[0].find('geometry').find('location').find('lat').text
    lon2 = r2[0].find('geometry').find('location').find('lng').text
    d = getDistanceFromLatLonInKm(float(lat1), float(lon1), float(lat2), float(lon2))
    print(str(d))

    f.write(benue +","+bata+"\n")
    f.write(str(d))
f.close()










