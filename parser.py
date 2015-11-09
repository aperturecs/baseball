#-*- coding: utf-8 -*-
import requests
import codecs
from game import Game
from pitcherGame import PitcherGame
from player import Player
from bs4 import BeautifulSoup
import json
import sys
import ast

def HitterParsing(request):
    records = []
    soup = BeautifulSoup(request.content, 'html.parser')
    try:
        player_records_html = soup.find("div",{ "class" : "player_records" }).findAll("tbody")
    except Exception,e:
        print e
        return None

    for text in player_records_html:
        text = text.findAll("tr")

        if len(text) == 1:
            return []

        for data in text:
            data = data.findAll("td")
            records.append(data)

    return records

def PitcherParsing(request):
    records = []
    soup = BeautifulSoup(request.content, 'html.parser')

    try:
        tables = soup.find("div",{ "class" : "player_records" }).findAll("table")
    except:
        return None


    for table in tables:
        tbody = table.find("tbody").findAll("tr")

        if len(tbody) == 1:
            return []

        for data in tbody:
            data = data.findAll("td")
            records.append(data)

    return records



def playerParsing(playerId, request):
    soup = BeautifulSoup(request.content, 'html.parser')
    player_info_html = soup.find("div",{"class" :  "player_info"})
    player_name = player_info_html.find(id="cphContainer_cphContents_playerProfile_lblName").string
    player_team = player_info_html.h4.string
    player_position = player_info_html.find(id="cphContainer_cphContents_playerProfile_lblPosition").string
    player_position = player_position.split("(")[0]
    player = Player(playerId,player_name,player_team,player_position)
    if player_position == "투수":
        player.type = "Pitcher"
    return player

def httpRequest(playerId, year, position):
    params = None

    if position == "Hitter":
        params = {
            "__EVENTTARGET" : "ctl00$ctl00$cphContainer$cphContents$ddlYear",
            "__EVENTARGUMENT" : "",
            "__LASTFOCUS" : "",
            "__VIEWSTATE" : "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ATEBMAExATAFMC4zNzVkAgUPZBYCZg8VEQUwNC4wOQNLSUEFMS4wMDABNQExATUBMgExATEBMgExATABMAEwATABMAUwLjQ4M2QCBg9kFgJmDxURBTA0LjEwAlNLBTAuMDAwATMBMAEwATABMAEwATABMAEwATEBMAExATAFMC40MzhkAgcPZBYCZg8VEQUwNC4xMQJTSwUwLjUwMAEyATEBMQEwATABMAExATEBMAEyATABMAEwBTAuNDQxZAIID2QWAmYPFREFMDQuMTICU0sFMC4yNTABNAExATEBMAEwATEBMgEwATABMAEwATIBMAUwLjQyMWQCCQ9kFgJmDxURBTA0LjE0Buuhr+uNsAUwLjY2NwEzATEBMgEwATABMAEwATABMAEyATABMAEwBTAuNDM5ZAIKD2QWAmYPFREFMDQuMTUG66Gv642wBTAuMDAwATMBMAEwATABMAEwATABMQEwATEBMAExATAFMC40MDlkAgsPZBYCZg8VEQUwNC4xNgbroa/rjbAFMC41MDABNAEwATIBMAEwATABMgEwATABMQEwATEBMAUwLjQxN2QCDA9kFgJmDxURBTA0LjE3Bu2VnO2ZlAUwLjI1MAE0ATEBMQEwATABMQEzATABMAEwATEBMAEwBTAuNDA0ZAIND2QWAmYPFREFMDQuMTgG7ZWc7ZmUBTAuNTAwATQBMgEyATABMAEwATABMQEwATABMAEwATAFMC40MTFkAg4PZBYCZg8VEQUwNC4yMQbsgrzshLEFMC4wMDABMwEwATABMAEwATABMAEwATABMAEwATEBMAUwLjM5MGQCDw9kFgJmDxURBTA0LjIyBuyCvOyEsQUwLjAwMAEzATABMAEwATABMAEwATABMAExATABMQEwBTAuMzcxZAIQD2QWAmYPFREFMDQuMjMG7IK87ISxBTAuMjUwATQBMQExATEBMAEwATEBMAEwATABMAEwATAFMC4zNjRkAhEPZBYCZg8VEQUwNC4yNAJMRwUwLjAwMAEzATABMAEwATABMAEwATABMAEwATEBMAEwBTAuMzQ4ZAISD2QWAmYPFREFMDQuMjUCTEcFMC4yNTABNAEwATEBMAEwATABMAEwATABMAEwATIBMAUwLjM0MmQCEw9kFgJmDxURBTA0LjI2AkxHBTAuNjY3ATMBMwEyATEBMAExATEBMAEwATEBMAEwATAFMC4zNTVkAhQPZBYCZg8VEQUwNC4yOAJTSwUwLjIwMAE1ATABMQEwATABMAEwATABMAEwATABMQEwBTAuMzQ2ZAIVD2QWAmYPFREFMDQuMzACU0sFMC4zMzMBMwExATEBMAEwATABMAExATABMgEwATABMAUwLjM0NWQCAg9kFgZmDxUBATVkAgEPFgIfAAXIATx0cj48dGggY29sc3Bhbj0iMiI+7ZWp6rOEPC90aD48dGg+MC4zNTM8L3RoPjx0aD44NTwvdGg+PHRoPjI3PC90aD48dGg+MzA8L3RoPjx0aD45PC90aD48dGg+MTwvdGg+PHRoPjk8L3RoPjx0aD4yOTwvdGg+PHRoPjg8L3RoPjx0aD4xPC90aD48dGg+MjE8L3RoPjx0aD4wPC90aD48dGg+MjE8L3RoPjx0aD4zPC90aD48dGg+MC4zNDk8L3RoPjwvdHI+ZAIDDxYCHwECGhY0Zg9kFgJmDxURBTA1LjAxAmt0BTAuMDAwATMBMAEwATABMAEwATABMAEwATABMAExATAFMC4zMzNkAgEPZBYCZg8VEQUwNS4wMgJrdAUwLjAwMAEzATEBMAEwATABMAEwATABMAExATABMAEwBTAuMzIyZAICD2QWAmYPFREFMDUuMDMCa3QFMS4wMDABMwExATMBMQEwATEBNQExATABMgEwATABMAUwLjM0NGQCAw9kFgJmDxURBTA1LjA1A0tJQQUwLjAwMAExATABMAEwATABMAEwATABMAEwATABMQEwBTAuMzQwZAIED2QWAmYPFREFMDUuMDYDS0lBBTAuMzMzATMBMgExATABMAExATEBMQEwATIBMAExATAFMC4zNDBkAgUPZBYCZg8VEQUwNS4wNwNLSUEFMC4wMDABMgEwATABMAEwATABMAEwATABMgEwATEBMQUwLjMzM2QCBg9kFgJmDxURBTA1LjA4Buuhr+uNsAUwLjMzMwEzATABMQEwATABMAEwATABMAExATABMAEwBTAuMzMzZAIHD2QWAmYPFREFMDUuMDkG66Gv642wBTAuNTAwATIBMQExATEBMAEwATEBMAEwATEBMAExATAFMC4zMzdkAggPZBYCZg8VEQUwNS4xMAbroa/rjbAFMC4wMDABMQEyATABMAEwATABMAEyATEBMwEwATABMAUwLjMzM2QCCQ9kFgJmDxURBTA1LjEzAkxHBTAuMDAwATEBMAEwATABMAEwATABMAEwATABMAExATAFMC4zMzBkAgoPZBYCZg8VEQUwNS4xNAJMRwUwLjI1MAE0ATABMQEwATABMAEwATABMAExATABMgEwBTAuMzI3ZAILD2QWAmYPFREFMDUuMTUG7IK87ISxBTAuMjUwATQBMAExATEBMAEwATABMAEwATEBMAExATAFMC4zMjVkAgwPZBYCZg8VEQUwNS4xNgbsgrzshLEFMC40MDABNQExATIBMAEwATEBMgEwATABMAEwATEBMAUwLjMyOGQCDQ9kFgJmDxURBTA1LjE3BuyCvOyEsQUwLjQwMAE1ATABMgEyATABMAExATABMAEwATABMAEwBTAuMzMxZAIOD2QWAmYPFREFMDUuMTkCa3QFMC4yNTABNAEwATEBMQEwATABMAEwATABMAEwATMBMAUwLjMyOGQCDw9kFgJmDxURBTA1LjIwAmt0BTAuMDAwATQBMQEwATABMAEwATEBMQEwATABMAExATAFMC4zMThkAhAPZBYCZg8VEQUwNS4yMQJrdAUwLjAwMAEzATEBMAEwATABMAEwATABMAExATABMgEwBTAuMzExZAIRD2QWAmYPFREFMDUuMjIG64Sl7IS8BTAuNjAwATUBMgEzATABMAEyATQBMQEwATABMAEwATAFMC4zMjFkAhIPZBYCZg8VEQUwNS4yMwbrhKXshLwFMC40MDABNQExATIBMQExATABMgEwATABMAEwATEBMQUwLjMyNGQCEw9kFgJmDxURBTA1LjI0BuuEpeyEvAUwLjc1MAE0ATQBMwExATABMAExATABMAExATABMAEwBTAuMzM2ZAIUD2QWAmYPFREFMDUuMjYG65GQ7IKwBTAuNzUwATQBMwEzATABMAEzATgBMAEwATABMAExATAFMC4zNDZkAhUPZBYCZg8VEQUwNS4yNwbrkZDsgrAFMC41MDABNAExATIBMAEwATABMQExATABMAEwATEBMAUwLjM1MGQCFg9kFgJmDxURBTA1LjI4BuuRkOyCsAUwLjAwMAExATIBMAEwATABMAEwATEBMAEzATABMAExBTAuMzQ4ZAIXD2QWAmYPFREFMDUuMjkDS0lBBTAuMzMzATMBMAExATABMAEwATABMAEwATAB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FgJmDxURBTA3LjAxBuuhr+uNsAUwLjUwMAE0ATIBMgEwATABMQExATEBMAEwATABMQEwBTAuMzQzZAIBD2QWAmYPFREFMDcuMDIG66Gv642wBTAuMDAwATMBMAEwATABMAEwATABMAEwATEBMAExATAFMC4zMzlkAgIPZBYCZg8VEQUwNy4wMwbtlZztmZQFMC40MDABNQEyATIBMAEwATEBMgExATABMAEwATIBMAUwLjM0MGQCAw9kFgJmDxURBTA3LjA0Bu2VnO2ZlAUwLjIwMAE1ATABMQEwATABMAEwATABMAEwATABMgEwBTAuMzM3ZAIED2QWAmYPFREFMDcuMDkCa3QFMC43NTABNAEzATMBMQEwATEBMgEwATABMAEwATABMAUwLjM0NGQCBQ9kFgJmDxURBTA3LjEwBuuEpeyEvAUxLjAwMAEyATEBMgEwATABMQEyATEBMAEwATEBMAEwBTAuMzQ5ZAIGD2QWAmYPFREFMDcuMTEG64Sl7IS8BTAuNzUwATQBMwEzATIBMAExATMBMAEwATEBMAExATAFMC4zNTVkAgcPZBYCZg8VEQUwNy4xNAJTSwUwLjI1MAE0ATEBMQEwATABMQEyATABMAEwATEBMAEwBTAuMzUzZAIID2QWAmYPFREFMDcuMTUCU0sFMC42NjcBMwExATIBMgEwATABMQEwATABMgEwATABMAUwLjM1N2QCCQ9kFgJmDxURBTA3LjE2AlNLBTAuNjY3ATMBMAEyATABMAEwATEBMQExATMBMAEwATAFMC4zNjBkAgoPZBYCZg8VEQUwNy4yMQbroa/rjbAFMC4wMDABMgEwATABMAEwATABMAEwATABMQExATEBMAUwLjM1OGQCCw9kFgJmDxURBTA3LjIyBuuhr+uNsAUwLjAwMAEzATABMAEwATABMAExATABMAExATABMgEwBTAuMzU0ZAIMD2QWAmYPFREFMDcuMjMG66Gv642wBTAuMzMzATMBMwExATABMAEwATABMQEwATIBMAExATAFMC4zNTRkAg0PZBYCZg8VEQUwNy4yNAbrkZDsgrAFMC42NjcBMwEwATIBMAEwATABMQEwATEBMQEwATABMAUwLjM1N2QCDg9kFgJmDxURBTA3LjI1BuuRkOyCsAUxLjAwMAEzATIBMwExATABMAEwATEBMAExATABMAEwBTAuMzY0ZAIPD2QWAmYPFREFMDcuMjYG65GQ7IKwBTAuMjAwATUBMAExATABMAEwATEBMAEwATABMAEzATAFMC4zNjFkAhAPZBYCZg8VEQUwNy4yOAbsgrzshLEFMC4wMDABNAEwATABMAEwATABMAEwATABMAEwATABMAUwLjM1NmQCEQ9kFgJmDxURBTA3LjI5BuyCvOyEsQUwLjMzMwEzATEBMQEwATABMQExATABMAEwATABMAExBTAuMzU2ZAISD2QWAmYPFREFMDcuMzAG7IK87ISxBTAuNDAwATUBMgEyATEBMAExATIBMAEwATABMAEwATAFMC4zNTZkAhMPZBYCZg8VEQUwNy4zMQbrhKXshLwFMC41MDABNAEwATIBMQEwATABMAEwATABMAEwATABMQUwLjM1OGQCBQ9kFgZmDxUBAThkAgEPFgIfAAXIATx0cj48dGggY29sc3Bhbj0iMiI+7ZWp6rOEPC90aD48dGg+MC40MzY8L3RoPjx0aD43ODwvdGg+PHRoPjIzPC90aD48dGg+MzQ8L3RoPjx0aD44PC90aD48dGg+MTwvdGg+PHRoPjg8L3RoPjx0aD4xODwvdGg+PHRoPjg8L3RoPjx0aD4yPC90aD48dGg+MTY8L3RoPjx0aD4zPC90aD48dGg+MTc8L3RoPjx0aD4wPC90aD48dGg+MC4zNzQ8L3RoPjwvdHI+ZAIDDxYCHwECGBYwZg9kFgJmDxURBTA4LjAxBuuEpeyEvAUwLjAwMAExATIBMAEwATABMAExATIBMAEyATEBMAEwBTAuMzU3ZAIBD2QWAmYPFREFMDguMDIG64Sl7IS8BTEuMDAwATIBMgEyATEBMAExATEBMQEwATIBMAEwATAFMC4zNjFkAgIPZBYCZg8VEQUwOC4wNAJMRwUwLjAwMAE0ATEBMAEwATABMAEwATABMAExATABMQEwBTAuMzU3ZAIDD2QWAmYPFREFMDguMDUCTEcFMC43NTABNAEzATMBMAEwATEBMgExATABMQEwATABMAUwLjM2MmQCBA9kFgJmDxURBTA4LjA2Buuhr+uNsAUxLjAwMAE0ATQBNAExATABMgEzATABMAEwATABMAEwBTAuMzcwZAIFD2QWAmYPFREFMDguMDcG66Gv642wBTAuNzUwATQBMQEzATABMAExATIBMAEwATABMAEwATAFMC4zNzRkAgYPZBYCZg8VEQUwOC4wOANLSUEFMC4zMzMBMwExATEBMAEwATABMAEwATABMgEwATABMAUwLjM3NGQCBw9kFgJmDxURBTA4LjA5A0tJQQUwLjMzMwEzATABMQEwATABMAEwATABMAExATABMAEwBTAuMzczZAIID2QWAmYPFREFMDguMTEG64Sl7IS8BTEuMDAwATUBMwE1ATEBMQExATIBMAExATEBMAEwATAFMC4zODNkAgkPZBYCZg8VEQUwOC4xMgbrhKXshLwFMC43NTABNAEyATMBMAEwATEBMgExATABMQEwATEBMAUwLjM4N2QCCg9kFgJmDxURBTA4LjEzBuuRkOyCsAUwLjAwMAE0ATABMAEwATABMAEwATABMAEwATABMgEwBTAuMzgzZAILD2QWAmYPFREFMDguMTQG65GQ7IKwBTAuMjUwATQBMAExATEBMAEwATEBMAEwATEBMAExATAFMC4zODFkAgwPZBYCZg8VEQUwOC4xNQJrdAUwLjMzMwEzATABMQEwATABMAExATABMAEwATABMgEwBTAuMzgxZAIND2QWAmYPFREFMDguMTYCa3QFMC4wMDABNAEwATABMAEwATABMAEwATABMAEwATIBMAUwLjM3NmQCDg9kFgJmDxURBTA4LjE4Bu2VnO2ZlAUwLjAwMAEzATABMAEwATABMAEwATABMAExATABMQEwBTAuMzczZAIPD2QWAmYPFREFMDguMTkG7ZWc7ZmUBTAuMDAwATEBMAEwATABMAEwATABMAEwATABMAExATAFMC4zNzJkAhAPZBYCZg8VEQUwOC4yMQbsgrzshLEBLQEwATABMAEwATABMAEwATABMAExATABMAEwBTAuMzcyZAIRD2QWAmYPFREFMDguMjICU0sFMC4yMDABNQExATEBMAEwATABMAEwATABMAEwATEBMAUwLjM3MGQCEg9kFgJmDxURBTA4LjIzAlNLBTAuNTAwATIBMAExATABMAEwATABMAEwATABMgExATAFMC4zNzFkAhMPZBYCZg8VEQUwOC4yNgJMRwUwLjAwMAE0ATABMAEwATABMAExATABMAEwATABMQEwBTAuMzY3ZAIUD2QWAmYPFREFMDguMjcG7ZWc7ZmUBTAuMDAwATIBMAEwATABMAEwATABMAEwATABMAExATAFMC4zNjVkAhUPZBYCZg8VEQUwOC4yOAbtlZztmZQFMS4wMDABNAExATQBMAEwATEBMgEyATABMAEwATABMAUwLjM3MWQCFg9kFgJmDxURBTA4LjI5Buuhr+uNsAUwLjYwMAE1ATEBMwEzATABMAEwATABMAEwATABMQEwBTAuMzc0ZAIXD2QWAmYPFREFMDguMzAG66Gv642wBTAuMzMzATMBMQExATEBMAEwATABMQExATIBMAExATAFMC4zNzRkAgYPZBYGZg8VAQE5ZAIBDxYCHwAFxwE8dHI+PHRoIGNvbHNwYW49IjIiPu2VqeqzhDwvdGg+PHRoPjAuNDI3PC90aD48dGg+NzU8L3RoPjx0aD4yMTwvdGg+PHRoPjMyPC90aD48dGg+NzwvdGg+PHRoPjA8L3RoPjx0aD44PC90aD48dGg+MjU8L3RoPjx0aD43PC90aD48dGg+MTwvdGg+PHRoPjIyPC90aD48dGg+NDwvdGg+PHRoPjk8L3RoPjx0aD4wPC90aD48dGg+MC4zODM8L3RoPjwvdHI+ZAIDDxYCHwECGBYwZg9kFgJmDxURBTA5LjAxBuyCvOyEsQUwLjAwMAE0ATABMAEwATABMAEwATABMAEwATABMQEwBTAuMzcwZAIBD2QWAmYPFREFMDkuMDIG7IK87ISxBTAuNTAwATIBMAExATEBMAEwATABMAEwATABMAExATAFMC4zNzFkAgIPZBYCZg8VEQUwOS4wMwbrkZDsgrAFMC44MDABNQE0ATQBMQEwATIBNgExATABMQEwATABMAUwLjM3NmQCAw9kFgJmDxURBTA5LjA0BuuRkOyCsAUwLjY2NwEzATEBMgEwATABMQExATABMQExATABMAEwBTAuMzc4ZAIED2QWAmYPFREFMDkuMDUCa3QFMC4wMDABMQEwATABMAEwATABMAEwATABMQEwATABMAUwLjM3OGQCBQ9kFgJmDxURBTA5LjA2Amt0BTAuNTAwATIBMQExATABMAEwATIBMQEwATIBMQExATAFMC4zNzhkAgYPZBYCZg8VEQUwOS4wOANLSUEFMC4zMzMBMwExATEBMAEwATABMAEwATABMgEwATEBMAUwLjM3OGQCBw9kFgJmDxURBTA5LjA5A0tJQQUwLjI1MAE0ATABMQEwATABMAEwATABMAEwATABMAEwBTAuMzc3ZAIID2QWAmYPFREFMDkuMTAG64Sl7IS8BTAuMDAwATIBMQEwATABMAEwATABMQEwATMBMAEwATAFMC4zNzVkAgkPZBYCZg8VEQUwOS4xMQbrhKXshLwFMS4wMDABNQEwATUBMwEwATABNAExATABMAEwATABMAUwLjM4MmQCCg9kFgJmDxURBTA5LjEyAlNLBTAuMzMzATMBMAExATABMAEwATABMAEwATIBMAEwATAFMC4zODJkAgsPZBYCZg8VEQUwOS4xMwJTSwUwLjAwMAEzATABMAEwATABMAEwATABMAEwATABMAEwBTAuMzc5ZAIMD2QWAmYPFREFMDkuMTUCa3QFMC4wMDABMwEyATABMAEwATABMAEwATABMgEwATEBMAUwLjM3NmQCDQ9kFgJmDxURBTA5LjE3Bu2VnO2ZlAUwLjY2NwEzATQBMgEwATABMQExATABMAEyATABMAEwBTAuMzc5ZAIOD2QWAmYPFREFMDkuMTgG7ZWc7ZmUBTAuNTAwATQBMQEyATABMAExATEBMAEwATABMAEwATAFMC4zODBkAg8PZBYCZg8VEQUwOS4yMAbrhKXshLwFMC42NjcBMwExATIBMAEwATABMAEwATABMAEyATABMAUwLjM4MmQCEA9kFgJmDxURBTA5LjIxBuuEpeyEvAUwLjAwMAEzATABMAEwATABMAEwATEBMAExATABMAEwBTAuMzc5ZAIRD2QWAmYPFREFMDkuMjIG7IK87ISxBTAuMzMzATMBMAExATABMAEwATABMAEwATEBMAEyATAFMC4zNzlkAhIPZBYCZg8VEQUwOS4yNANLSUEFMC41MDABMgEyATEBMAEwATEBNAEwATABMAExATEBMAUwLjM3OWQCEw9kFgJmDxURBTA5LjI1AkxHBTAuNzUwATQBMQEzATABMAExATMBMQEwATABMAEwATAFMC4zODNkAhQPZBYCZg8VEQUwOS4yNwbroa/rjbAFMC4zMzMBMwEwATEBMQEwATABMAEwATABMQEwATEBMAUwLjM4MmQCFQ9kFgJmDxURBTA5LjI4Bu2VnO2ZlAUwLjMzMwEzATABMQExATABMAEwATABMAExATABMAEwBTAuMzgyZAIWD2QWAmYPFREFMDkuMjkG64Sl7IS8BTAuMjAwATUBMAExATABMAEwATABMAEwATABMAEwATAFMC4zODBkAhcPZBYCZg8VEQUwOS4zMAbrkZDsgrAFMS4wMDABMgEyATIBMAEwATEBMwExATABMgEwATABMAUwLjM4M2QCBw9kFgZmDxUBAjEwZAIBDxYCHwAFwwE8dHI+PHRoIGNvbHNwYW49IjIiPu2VqeqzhDwvdGg+PHRoPjAuMzMzPC90aD48dGg+MTI8L3RoPjx0aD4xPC90aD48dGg+NDwvdGg+PHRoPjE8L3RoPjx0aD4wPC90aD48dGg+MTwvdGg+PHRoPjU8L3RoPjx0aD4xPC90aD48dGg+MDwvdGg+PHRoPjE8L3RoPjx0aD4wPC90aD48dGg+NDwvdGg+PHRoPjA8L3RoPjx0aD4wLjM4MTwvdGg+PC90cj5kAgMPFgIfAQIEFghmD2QWAmYPFREFMTAuMDECTEcFMC4wMDABMwEwATABMAEwATABMQEwATABMAEwATABMAUwLjM4MGQCAQ9kFgJmDxURBTEwLjAyAlNLBTAuNTAwATQBMQEyATABMAExATQBMQEwATEBMAExATAFMC4zODFkAgIPZBYCZg8VEQUxMC4wMwJTSwUwLjAwMAExATABMAEwATABMAEwATABMAEwATABMQEwBTAuMzgwZAIDD2QWAmYPFREFMTAuMDUCa3QFMC41MDABNAEwATIBMQEwATABMAEwATABMAEwATIBMAUwLjM4MWRkplIbmWyX3yJ+sGTJZdDfRKmHqyU2nDqx0H6MIExqakE="
            ,"__VIEWSTATEGENERATOR":"07340454"
            ,"__EVENTVALIDATION" : "/wEdAAl+WYCou6kTiSErfGvfu0PSEG4FQbqeMQMc81CqbOAKuwJ3fDlphD/8+kBKsg6066H+U6yDvKKS7Q2/wix8rDYWVCz/NUuC/D4JkSA6UUtGOasWmV6pb+DNfkkyPJe4qAeZkDbfGaIsMikG06rlk7O+7yLKEf2GqF9x+CCR9rpurcCo6/8f4k+kxf++tERcpN7a9MutFC6MESj7MjLZyFwBiFhSWjiUJaN6CcuMxp7JeA==",
            "ctl00$ctl00$txtSearchWord":"",
            "ctl00$ctl00$cphContainer$cphContents$ddlYear":str(year)
        }

    if position == "Pitcher":
        params = {
            "__EVENTTARGET" : "ctl00$ctl00$cphContainer$cphContents$ddlYear",
            "__EVENTARGUMENT" : "",
            "__LASTFOCUS" : "",
            "__VIEWSTATE" : "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"
            ,"__VIEWSTATEGENERATOR":"7D7013E0"
            ,"__EVENTVALIDATION" : "/wEdAAm7FZAHoLV3k051FvVC6rVMEG4FQbqeMQMc81CqbOAKuwJ3fDlphD/8+kBKsg6066H+U6yDvKKS7Q2/wix8rDYWVCz/NUuC/D4JkSA6UUtGOasWmV6pb+DNfkkyPJe4qAeZkDbfGaIsMikG06rlk7O+7yLKEf2GqF9x+CCR9rpurcCo6/8f4k+kxf++tERcpN4f/Lq4Lx6ZVw8qcIX1t+WEMGQc1wsXqpkX73Jx/x+Xzg=="
            ,"ctl00$ctl00$txtSearchWord":"",
            "ctl00$ctl00$cphContainer$cphContents$ddlYear":str(year)
        }

    header = {
        "Content-Type":"application/x-www-form-urlencoded",
        "Cache-Control": "no-cache",
    }

    try:
        request = requests.post("http://www.koreabaseball.com/Record/Player/"+position+"Detail/Daily.aspx?playerId="+str(playerId), data=params, headers=header)
    except:
        print "네트워크 요청에 실패하였습니다."
        sys.exit()
    return request


def splitData(data):
    d = str(data).split("<td>")[1]
    d = d.split("</td>")[0]
    return d

def dataParsing(datas):
    array = []
    for data in datas:
        data_array=[]
        for temp in data:
            data_array.append(splitData(temp))
        array.append(data_array)

    return array


def gameDataParsing(year,datas):
    if datas == None:
        return []
    datas = dataParsing(datas)
    games = []
    for d in datas:
        game = Game(year,d[0],d[1],d[2],d[3],d[4],d[5],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13],d[14],d[15])
        games.append(game)
    return games

def pitcherGameDataParsing(year,datas):
    if len(datas) == 0:
        return []
    datas = dataParsing(datas)
    games = []
    for d in datas:
        game = PitcherGame(year,d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13],d[14])
        games.append(game)
    return games

def playerSave(f,player):
    f.write(str({"playerId":player.playerId,"name":player.name,"type":player.type,"team":player.team,"position":player.position})+"\n")
    for game in player.games:
        f.write(str(game.__dict__)+"\n")
    for game in player.pitcherGames:
        f.write(str(game.__dict__)+"\n")
    f.write("\n")

def fileParser():
    with codecs.open("result2.txt",'r',encoding='utf8') as f:
        lines = f.readlines()

    players = []
    current_Player = None
    flag =0

    for line in lines:

        if line == "\n":
            players.append(current_Player)
            flag = 0
            continue

        line = line.split("\n")[0]

        if flag == 0:
            j = ast.literal_eval(line)
            current_Player = Player(j["playerId"],j["name"],j["team"],j["position"])
            current_Player.type = j["type"]
            flag = 1

        else:
            if current_Player == None:
                continue

            d = ast.literal_eval(line)
            if d["type"]=="Hitter":
                game = Game(d["year"],d["date"],d["sideTeam"],d["AVG1"],d["AB"],d["R"],d["H"],d["B2"],d["B3"],d["HR"],d["RBI"],d["SB"],d["CS"],d["BB"],d["HBP"],d["SO"],d["GDP"],d["AVG2"])
                current_Player.games.append(game)
            else :
                game = PitcherGame(d["year"],d["date"],d["sideTeam"],d["postion"],d["result"],d["ERA1"],d["TBF"],d["IP"],d["H"],d["HR"],d["BB"],d["HBP"],d["SO"],d["R"],d["ER"],d["ERA2"])
                current_Player.pitcherGames.append(game)


    return players

def parsing(player,postion):
    games= []

    for year in range(2010,2016):
        request = httpRequest(player.playerId,year,postion)

        if player.type == "Hitter":
            datas = HitterParsing(request)
            for game in gameDataParsing(year,datas):
                games.append(game)

        if player.type == "Pitcher":
            datas = PitcherParsing(request)
            for game in pitcherGameDataParsing(year,datas):
                games.append(game)

    return games
