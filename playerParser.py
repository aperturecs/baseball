#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

from player import Player

def playerParsing(playerId):
    request = requests.post("http://www.koreabaseball.com/Record/Player/HitterDetail/Daily.aspx?playerId="+str(playerId))
    soup = BeautifulSoup(request.content, 'html.parser')
    player_info_html = soup.find("div",{"class" :  "player_info"})
    player_name = player_info_html.find(id="cphContainer_cphContents_playerProfile_lblName").string
    player_team = player_info_html.h4.string
    player_position = player_info_html.find(id="cphContainer_cphContents_playerProfile_lblPosition").string
    player_postion_detail = player_position.split("(")[1].split(")")[0]
    player_position = player_position.split("(")[0]
    player_img = player_info_html.find(id="cphContainer_cphContents_playerProfile_imgProgile")["src"]
    player_img = "http://www.koreabaseball.com"+player_img
    player = Player(playerId,player_name,player_team,player_position,player_postion_detail,player_img)
    if player_position == "투수":
        player.type = "Pitcher"
    return player
