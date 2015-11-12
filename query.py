# -*- coding: utf-8 -*-
import MySQLdb as mdb
class Query:
    def __init__(self):
        try:
            self.con = mdb.connect('localhost', 'cpd', '12341234', 'busstation');
            self.cur = self.con.cursor()
            self.cur.execute("SELECT VERSION()")
            ver = cur.fetchone()
            print "Database version : %s " % ver
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

    def quering_add(self,sql):
        try:
            self.cur.execute(sql)
            print cur.fetchone()
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

    def quering_select(self,sql):
        try:
            self.cur.execute(sql)
            return cur.fetchone()
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)
