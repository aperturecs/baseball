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

        request = requests.post("http://www.koreabaseball.com/Record/Player/PitcherDetail/Basic.aspx?playerId="+str(player.playerId), data=params,headers=header)

        soup = BeautifulSoup(request.content, 'html.parser')

        try:
            tables = soup.find("div", {"summury" : "2015년 투수성적으로 평균자책점,경기수,완투,완봉,승리,패배,세이브,홀드,승률,타자수,투구수,이닝,피안타,2루타,3루타,홈런을 표시합니다"}).findAll("table")""

        except:
            continue

        for table in tables:
            tbody = table.find("tbody").findAll("tr")

        for content in tbody:
            d = d.findAll("td")
            data = []
            for content in d:
                content = str(content).split("<td>")[1]
                content = content.split("</td>")[0]
                data.append(content)
                print content

                #player.pprofile.append(PitcherProfile(playerId, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23]))
