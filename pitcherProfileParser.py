#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

from pitcherGame import PitcherGame
from player import Player


def pitcherProfileParsing(player):

    request = requests.get("http://www.koreabaseball.com/Record/Player/PitcherDetail/Basic.aspx?playerId="+str(player.playerId))
    soup = BeautifulSoup(request.content, 'html.parser')
    soup = soup.find("div",{"class":"player_records"})

    try:
        first = soup.find("table",{"class":"tData01 tt mgb5"}).find("tbody").find("tr").findAll("td")
        second = soup.findAll("table",{"class":"tData01 tt"})[0].find("tbody").find("tr").findAll("td")

    except:
        pass

    data = []
    for t in first:
        t = str(t).split("<td>")[1]
        t = t.split("</td>")[0]
        if t == "-":
            t = 0
        data.append(t)

    for t in second:
        t = str(t).split("<td>")[1]
        t = t.split("</td>")[0]
        if t == "-":
            t = 0
        data.append(t)
    print data

    player.profile.append(PitcherProfile(player.playerId,data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23]))
