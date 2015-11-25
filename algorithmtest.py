#-*- coding: utf-8 -*-
import algorithm

datas = algorithm.growth(64914)
print algorithm.stat(64914)
for data in datas:
    print str(data["year"])+"."+str(data["month"])+" : " + str(data["growth"])
