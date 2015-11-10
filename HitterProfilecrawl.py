#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from pprofile import PitcherProfile
from pitcherGame import PitcherGame
from player import Player


def pitcherProfileParsing(player):
    header = {
        "Content-Type":"application/x-www-form-urlencoded",
        "Cache-Control": "no-cache",
    }

        request = requests.post("http://www.koreabaseball.com/Record/Player/PitcherDetail/Basic.aspx?playerId="+str(player.playerId), headers=header)

        soup = BeautifulSoup(request.content, 'html.parser')

        try:
            tables = soup.find("div",{ "class" : "player_records" }).findAll("table")
        except:
            continue

        for table in tables:
            tbody = table.find("tbody").findAll("tr")

            if len(tbody) == 1:
                continue

            for d in tbody:
                d = d.findAll("td")
                data = []
                for content in d:
                    content = str(content).split("<td>")[1]
                    content = content.split("</td>")[0]
                    if content == "-":
                        content = 0
                    data.append(content)

                player.pitcherGames.append(PitcherGame(year,data[0],data[1],data[2],data[3],float(data[4]),int(data[5]),data[6],int(data[7]),int(data[8]),int(data[9]),int(data[10]),int(data[11]),int(data[12]),int(data[13]),float(data[14])))
