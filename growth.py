#coding:utf-8
'''
맨처음 경기 한 달부터 지금까지의 ops성장률
첫번째 ops a1
n번째 ops an
y = an-a1
'''




# 1. 모든 게임 정보
#     -> 디비에서 긁어오고, 클래스화 시키고, 넘기기
# 2. 월단위로 줄이고
#     -> 다 더하기
# 3. 성장률 구하기
#     -> 알고리즘 돌리기

Games = []



OBP = (H + BB + HBP)/(AB + BB + SF + HBP)
SLG = TB/AB
OPS = OBP + SLG



OPS_A = [] #매 경기 OPS
ops_y =[] #OPS 성장률 y값
OPS_f = OPS[0] #맨 처음 경기 OPS

for i in OPS:
    OPS_growth = OPS_A[i] - OPS_f #한 경기 OPS - 맨 처음경기 OPS
    ops_y.append(OPS_growth) #ops_y 리스트에 추가


#x축은 시간(경기), y축은 OPS 성장률
