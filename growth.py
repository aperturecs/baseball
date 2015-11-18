#coding:utf-8
from hitterProfile import HitterProfile
from hitterGame import HitterGame


# 맨처음 경기 한 달부터 지금까지의 ops성장률
# 첫번째 ops a1
# n번째 ops an
# y = an-a1


# 1. 모든 게임 정보
#     -> 디비에서 긁어오고, 클래스화 시키고, 넘기기
# 2. 월단위로 줄이고
#     -> 다 더하기
# 3. 성장률 구하기
#     -> 알고리즘 돌리기

Games = [] #전체 경기 데이터
OPS_A = [] #매월 경기 OPS


for game in Games:
    OBP = (game.H + game.BB + game.HBP)/(game.AB + game.BB + game.SF + game.HBP)
    SLG = game.TB/game.AB
    OPS = OBP + SLG
    OPS_A.append(OPS)

OPS_y =[] #OPS 성장률 y값
OPS_f = OPS_A[0] #맨 처음 경기 OPS

for OPS_Element in OPS_A:
    OPS_growth = OPS_Element - OPS_f #한 경기 OPS - 맨 처음경기 OPS
    ops_y.append(OPS_growth) #ops_y 리스트에 추가


#x축은 시간(경기), y축은 OPS 성장률
