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

      
