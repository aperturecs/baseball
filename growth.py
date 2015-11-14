#coding:utf-8
'''
맨처음 경기 한 달부터 지금까지의 ops성장률
첫번째 ops a1
n번째 ops an
y = an-a1
'''


OPS = [] #매 경기 OPS
ops_y =[] #OPS 성장률 y값
OPS_f = OPS[0] #맨 처음 경기 OPS
del OPS[0]

for i in OPS:
    OPS_growth = OPS[i] - OPS_f #한 경기 OPS - 맨 처음경기 OPS
    ops_y.append(OPS_growth) #ops_y 리스트에 추가

ops_y.insert(0, OPS_f) #0자리에 맨 처음 경기 OPS 삽입

#x축은 시간(경기), y축은 OPS 성장률
