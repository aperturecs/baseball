     #-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

from pitcherProfile import PitcherProfile
from player import Player


def pitcherProfileParsing(player):

    request = requests.get("http://www.koreabaseball.com/Record/Player/PitcherDetail/Basic.aspx?playerId="+str(player.playerId))
    # print request.content
    soup = BeautifulSoup(request.content, 'html.parser')
    soup = soup.find("div",{"class":"player_records"})

    try:
        first = soup.find("table",{"class":"tData01 tt mgb5"}).find("tbody").find("tr").findAll("td")
        second = soup.findAll("table",{"class":"tData01 tt"})[0].find("tbody").find("tr").findAll("td")
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
    except:
        return None

    player.profile = PitcherProfile(player.playerId, data[0], float(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), int(data[7]), int(data[8]), float(data[9]), int(data[10]), int(data[11]), data[12], int(data[13]), int(data[14]), int(data[15]), int(data[16]), int(data[17]), int(data[18]), int(data[19]), int(data[20]), int(data[21]), int(data[22]), int(data[23]),int(data[24]),int(data[25]),int(data[26]),float(data[27]),float(data[28]),int(data[29]))
    return True
