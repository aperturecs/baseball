#-*- coding: utf-8 -*-
import pitcherGameParser
import playerParser
from pitcherGame import PitcherGame
from player import Player
import sys
# from parser.dataStructure.hitterGame import

reload(sys)
sys.setdefaultencoding('utf-8')

code = 77637

player = playerParser.playerParsing(code)
pitcherGameParser.pitcherGameParsing(player)
print player.name

for game in player.pitcherGames:
    print game.__dict__
