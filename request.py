#-*- coding: utf-8 -*-
import parser
import sys
import traceback
import time
from playerCode import PlayerCode
import ErrorCode
reload(sys)
sys.setdefaultencoding('utf-8')

result = []
codes = PlayerCode()
f = open("result2.txt","w")
#f = open("result.txt","w")
errorList = []
errorLists = [61240, 61268, 77229, 76329, 78257, 72749, 72523, 61895, 75138, 72862, 77854, 76822, 74857, 64907, 62920, 62920, 78366, 97571, 62929, 64021, 63512, 76540, 74167, 63935, 72551, 62655, 61411, 95657, 79440, 62919, 65764, 79760, 64764, 62451, 73750, 78760, 62919, 65764, 79760, 64764, 73750, 78760, 62451, 62349, 78823, 71255, 65643, 65639, 65639, 63638, 65658, 65630, 75620, 97336, 76610, 61666, 65659, 61643]

start_time = 0
count = 1


for playerId in errorLists:
    try:
        start_time = time.time()
        request = parser.httpRequest(playerId,2014,"Hitter")
        player = parser.playerParsing(playerId,request)

        if player.position == "투수":
            player.pitcherGames = parser.parsing(player,"Pitcher")
        player.games = parser.parsing(player,"Hitter")

        result.append(player)

        parser.playerSave(f,player)
        print "------------------------------"
        print "선수이름 :"+player.name
        print "선수 포지션 :"+player.position
        print "선수 팀 :"+player.team
        print "타자 출장 :"+str(len(player.games))
        print "투수 출장 :"+str(len(player.pitcherGames))
        print "크롤링 소요 시간 :"+str(round(time.time()-start_time,2))+"초"
        print "진행현황 : "+str(count)+"/"+ str(len(codes.codes))
        print "-------------------------------"
        count +=1
    except:
        print "*******************************"
        print "선수 Id :"+str(playerId) +"에러 발생"
        print "*******************************"
        errorList.append(playerId)
        traceback.print_exc()
        pass
f.close()

print "*********파싱완료*********"
print "에러 리스트 :"+ str(errorList)
