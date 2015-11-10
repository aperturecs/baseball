#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import pitcherProfileParser
import playerParser
from player import Player

code = 63938

player = playerParser.playerParsing(code)
pitcherProfileParser.pitcherProfileParsing(player)
# pitcherGameParser.pitcherGameParsing(player)
# print player.name
#
# for game in player.pitcherGames:
#     print game.__dict__
