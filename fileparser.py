#-*- coding: utf-8 -*-
import sys
import parser

reload(sys)
sys.setdefaultencoding('utf-8')

players = parser.fileParser()

player = players[0]

result = [1]

print player.name
for game in player.games:
    print game.__dict__
    try:
        data = (float(game.H) + float(game.BB) + float(game.HBP)) / (float(game.AB)+float(game.BB)+float(game.HBP))
        # data += (float(game.H) + float(game.B2)*2 + float(game.B3) * 3 + float(game.HR) *4) / float(game.AB)
        final = {"year":game.year,"date":game.date,"OPS":data}
        print final
        result.append(final)
    except :
        print "error"
        pass
