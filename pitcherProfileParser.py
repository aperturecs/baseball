#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from pprofile import PitcherProfile
from pitcherGame import PitcherGame
from player import Player


def pitcherProfileParsing(player):

    request = requests.get("http://www.koreabaseball.com/Record/Player/PitcherDetail/Basic.aspx?playerId="+str(player.playerId))
    soup = BeautifulSoup(request.content, 'html.parser')
    soup = soup.find("div",{"class":"player_records"})

    try:
        first = soup.find("table", {"summary" : "2015년 투수성적으로 평균자책점,경기수,완투,완봉,승리,패배,세이브,홀드,승률,타자수,투구수,이닝,피안타,2루타,3루타,홈런을 표시합니다"}).find("tr").findAll("td")
        second = soup.find("table",{"summary" : "2015성적"}).find("tr").findAll("td")
    except:
        continue

    temp = []
    for t in first:
        t = str(t).split("<td>")[1]
        t = t.split("</td>")[0]
        if t == "-":
            t = 0
        temp.append(temp)
    first = temp

    temp.clear()
    for t in second:
        t = str(t).split("<td>")[1]
        t = t.split("</td>")[0]
        if t == "-":
            t = 0
        temp.append(temp)
    second = temp

        
    print first
    print second

        #player.pprofile.append(PitcherProfile(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23]))
