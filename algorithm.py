from hitterGame import HitterGame
from query import Query

Query = Query()
queries = query.quering_select("Select * from HitterGames where playerId=79453")

# def __init__(self, playerId, year, date, sideTeam, AVG1, AB, R, H, B2, B3, HR, RBI, SB, CS, BB, HBP, SO, GDP, AVG2):
 # type             ,playerId,year,month,day,sideTeam,AVG1 ,AB,R,H,B2,B3,HR,RBI,SB,CS,BB,HBP,SO,GDP,AVG2  |
games = []

for query in queries:
    game = Game(query[1],query[2],query[3],query[4],query[5],query[6],query[7],query[8],query[9],query[10],query[11],query[12],query[13],query[14],query[15],query[16],query[17],query[18],query[19])
    print game.__dict__
    games.append(game)
