#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import hitterProfileParser
import playerParser
from player import Player

code = 64914

player = playerParser.playerParsing(code)
hitterProfileParser.hitterProfileParsing(player)
# pitcherGameParser.pitcherGameParsing(player)
# print player.name
#
# for game in player.pitcherGames:
#     print game.__dict__
