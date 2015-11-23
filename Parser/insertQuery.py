from query import Query

f = open("sql.txt","r")
lines = f.readlines()
query = Query()

for line in lines:
    line = line.split("\n")[0]
    query.quering_add(line)

query.end()
